"""Shared abuse-prevention helpers for the public chatbot."""

from __future__ import annotations

import asyncio
import hashlib
import hmac
import logging
import re
import secrets
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Sequence

from fastapi import Request

from app.config import Settings, get_settings

try:
    import redis.asyncio as redis_async
except Exception:  # pragma: no cover - optional dependency
    redis_async = None

try:
    import tiktoken
except Exception:  # pragma: no cover - fallback path
    tiktoken = None

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class AbuseIdentity:
    visitor_id: str
    visitor_token: str
    issued_new_cookie: bool
    client_ip: str
    session_id: str
    user_agent: str = ""
    origin: str = ""
    referer: str = ""


@dataclass(frozen=True)
class AbuseDecision:
    allowed: bool
    status_code: int = 200
    reason: str = ""
    retry_after: int = 0
    challenge_required: bool = False
    headers: dict[str, str] = field(default_factory=dict)


class _CounterStore:
    async def increment(self, key: str, amount: int, ttl_seconds: int) -> int:
        raise NotImplementedError


class _MemoryCounterStore(_CounterStore):
    def __init__(self) -> None:
        self._values: dict[str, tuple[int, int]] = {}
        self._lock = asyncio.Lock()

    async def increment(self, key: str, amount: int, ttl_seconds: int) -> int:
        now = int(time.time())
        async with self._lock:
            current = self._values.get(key)
            if current is None or current[1] <= now:
                count = amount
                self._values[key] = (count, now + ttl_seconds)
                return count

            count = current[0] + amount
            self._values[key] = (count, current[1])
            return count


class _RedisCounterStore(_CounterStore):
    def __init__(self, client: Any) -> None:
        self._client = client

    async def increment(self, key: str, amount: int, ttl_seconds: int) -> int:
        pipeline = self._client.pipeline()
        pipeline.incrby(key, amount)
        pipeline.expire(key, ttl_seconds)
        count, _ = await pipeline.execute()
        return int(count)


@dataclass(frozen=True)
class _WindowRule:
    scope: str
    limit: int
    window_seconds: int
    kind: str = "count"


class AbuseGuard:
    """Rate-limit and abuse-prevention helper for chat endpoints."""

    _PROMPT_PROBE_PATTERNS = (
        re.compile(r"ignore\s+previous", re.IGNORECASE),
        re.compile(r"disregard\s+previous", re.IGNORECASE),
        re.compile(r"system\s+prompt", re.IGNORECASE),
        re.compile(r"developer\s+message", re.IGNORECASE),
        re.compile(r"reveal\s+(?:your|the)\s+(?:prompt|instructions)", re.IGNORECASE),
        re.compile(r"show\s+(?:your|the)\s+instructions", re.IGNORECASE),
        re.compile(r"jailbreak", re.IGNORECASE),
        re.compile(r"bypass\s+safety", re.IGNORECASE),
        re.compile(r"api\s*key", re.IGNORECASE),
        re.compile(r"secret\s+key", re.IGNORECASE),
        re.compile(r"what\s+is\s+your\s+prompt", re.IGNORECASE),
        re.compile(r"repeat\s+the\s+prompt", re.IGNORECASE),
    )

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        self._memory_store = _MemoryCounterStore()
        self._redis_store: _RedisCounterStore | None = None
        self._redis_lock = asyncio.Lock()
        self._encoding = None
        self._runtime_secret = (
            self.settings.VISITOR_COOKIE_SECRET.strip() or secrets.token_urlsafe(32)
        )

    async def resolve_identity(self, request: Request) -> AbuseIdentity:
        client_ip = self._extract_client_ip(request)
        user_agent = request.headers.get("user-agent", "").strip()
        origin = request.headers.get("origin", "").strip()
        referer = request.headers.get("referer", "").strip()
        session_id = self._safe_session_id(request.query_params.get("session_id", "default"))

        raw_cookie = request.cookies.get(self.settings.VISITOR_COOKIE_NAME, "")
        visitor_id, issued_new_cookie = self._parse_or_create_visitor_id(raw_cookie)
        visitor_token = self._sign_visitor_id(visitor_id)

        return AbuseIdentity(
            visitor_id=visitor_id,
            visitor_token=visitor_token,
            issued_new_cookie=issued_new_cookie,
            client_ip=client_ip,
            session_id=session_id,
            user_agent=user_agent,
            origin=origin,
            referer=referer,
        )

    def apply_cookie(self, response: Any, identity: AbuseIdentity, request: Request) -> None:
        if not identity.issued_new_cookie:
            return

        secure_cookie = self.settings.FORCE_SECURE_COOKIES or request.url.scheme == "https"
        response.set_cookie(
            key=self.settings.VISITOR_COOKIE_NAME,
            value=identity.visitor_token,
            max_age=self.settings.VISITOR_COOKIE_MAX_AGE_SECONDS,
            httponly=True,
            secure=secure_cookie,
            samesite="lax",
            path="/",
        )

    async def evaluate_chat_request(
        self,
        request: Request,
        session_id: str,
        user_message: str,
        chat_history: Sequence[Any] | None = None,
    ) -> AbuseDecision:
        identity = getattr(request.state, "abuse_identity", None)
        if identity is None:
            identity = await self.resolve_identity(request)
            request.state.abuse_identity = identity

        normalized_message = re.sub(r"\s+", " ", (user_message or "").strip())
        estimated_tokens = self._estimate_request_tokens(normalized_message, chat_history)
        session_id = self._safe_session_id(session_id or identity.session_id)

        checks = [
            _WindowRule("visitor", self.settings.RATE_LIMIT_VISITOR_PER_10_SECONDS, 10),
            _WindowRule("visitor", self.settings.RATE_LIMIT_VISITOR_PER_MINUTE, 60),
            _WindowRule("visitor", self.settings.RATE_LIMIT_VISITOR_PER_HOUR, 3600),
            _WindowRule("visitor", self.settings.RATE_LIMIT_VISITOR_PER_DAY, 86400),
            _WindowRule("burst", self.settings.BURST_LIMIT_PER_10_SECONDS, 10),
            _WindowRule("session", self.settings.RATE_LIMIT_SESSION_PER_30_SECONDS, 30),
            _WindowRule("session", self.settings.RATE_LIMIT_SESSION_PER_10_MINUTES, 600),
            _WindowRule("session", self.settings.RATE_LIMIT_SESSION_PER_HOUR, 3600),
            _WindowRule("ip", self.settings.RATE_LIMIT_IP_PER_10_MINUTES, 600),
            _WindowRule("ip", self.settings.RATE_LIMIT_IP_PER_HOUR, 3600),
            _WindowRule("ip", self.settings.RATE_LIMIT_IP_PER_DAY, 86400),
        ]

        store = await self._get_store()
        bucket_context = {
            "visitor": identity.visitor_id,
            "burst": identity.visitor_id,
            "session": session_id,
            "ip": identity.client_ip,
        }

        ip_soft_signal = False
        for rule in checks:
            identifier = bucket_context[rule.scope]
            current = await store.increment(
                self._window_key(rule.scope, identifier, rule.kind, rule.window_seconds),
                1,
                rule.window_seconds + 5,
            )
            if current > rule.limit:
                if rule.scope == "ip":
                    ip_soft_signal = True
                    continue

                retry_after = self._retry_after(rule.window_seconds)
                return self._deny(
                    reason="Too many requests. Please wait and try again.",
                    retry_after=retry_after,
                    challenge_required=self.settings.ENABLE_TURNSTILE,
                )

        token_rules = [
            _WindowRule("visitor", self.settings.TOKEN_BUDGET_PER_HOUR, 3600, "tokens"),
            _WindowRule("visitor", self.settings.TOKEN_BUDGET_PER_DAY, 86400, "tokens"),
            _WindowRule("ip", self.settings.TOKEN_BUDGET_IP_PER_HOUR, 3600, "tokens"),
            _WindowRule("ip", self.settings.TOKEN_BUDGET_IP_PER_DAY, 86400, "tokens"),
        ]

        for rule in token_rules:
            identifier = bucket_context[rule.scope]
            current = await store.increment(
                self._window_key(rule.scope, identifier, rule.kind, rule.window_seconds),
                estimated_tokens,
                rule.window_seconds + 5,
            )
            if current > rule.limit:
                retry_after = self._retry_after(rule.window_seconds)
                return self._deny(
                    reason="Token budget exceeded. Please slow down.",
                    retry_after=retry_after,
                    challenge_required=self.settings.ENABLE_TURNSTILE,
                )

        if self._looks_like_prompt_probe(normalized_message):
            probe_count = await store.increment(
                self._window_key("probe", identity.visitor_id, "count", 86400),
                1,
                86400 + 5,
            )
            if probe_count >= self.settings.RATE_LIMIT_PROMPT_PROBE_PER_DAY:
                return self._deny(
                    reason="Suspicious request pattern detected. Please try again later.",
                    retry_after=600,
                    challenge_required=True,
                )

        if ip_soft_signal and self._looks_like_prompt_probe(normalized_message):
            return self._deny(
                reason="Suspicious request pattern detected. Please try again later.",
                retry_after=300,
                challenge_required=True,
            )

        return AbuseDecision(
            allowed=True,
            headers={
                "X-Visitor-Id": identity.visitor_id,
            },
        )

    async def _get_store(self) -> _CounterStore:
        if not self.settings.REDIS_URL or redis_async is None:
            return self._memory_store

        if self._redis_store is not None:
            return self._redis_store

        async with self._redis_lock:
            if self._redis_store is not None:
                return self._redis_store

            try:
                client = redis_async.from_url(
                    self.settings.REDIS_URL,
                    encoding="utf-8",
                    decode_responses=True,
                )
                await client.ping()
                self._redis_store = _RedisCounterStore(client)
                logger.info("Abuse guard connected to Redis backend")
            except Exception as exc:  # pragma: no cover - fallback path
                logger.warning("Redis unavailable for abuse guard, using memory store: %s", exc)
                self._redis_store = None
                return self._memory_store

        return self._redis_store or self._memory_store

    def _deny(self, reason: str, retry_after: int, challenge_required: bool) -> AbuseDecision:
        headers = {
            "Retry-After": str(max(retry_after, 1)),
            "X-Abuse-Reason": reason,
        }
        if challenge_required:
            headers["X-Challenge-Required"] = "1"

        return AbuseDecision(
            allowed=False,
            status_code=429,
            reason=reason,
            retry_after=retry_after,
            challenge_required=challenge_required,
            headers=headers,
        )

    def _window_key(self, scope: str, identifier: str, kind: str, window_seconds: int) -> str:
        bucket = int(time.time()) // window_seconds
        identifier_hash = hashlib.sha256(identifier.encode("utf-8")).hexdigest()[:16]
        return f"{self.settings.REDIS_KEY_PREFIX}:{scope}:{kind}:{window_seconds}:{bucket}:{identifier_hash}"

    def _retry_after(self, window_seconds: int) -> int:
        now = int(time.time())
        return max((window_seconds - (now % window_seconds)), 1)

    def _looks_like_prompt_probe(self, text: str) -> bool:
        if not text:
            return False
        normalized = text.lower()
        return any(pattern.search(normalized) for pattern in self._PROMPT_PROBE_PATTERNS)

    def _estimate_request_tokens(
        self,
        user_message: str,
        chat_history: Sequence[Any] | None = None,
    ) -> int:
        tokens = self._count_tokens(user_message)
        tokens += self.settings.CHAT_COMPLETION_MAX_OUTPUT_TOKENS

        if chat_history:
            for turn in list(chat_history)[-8:]:
                content = getattr(turn, "content", "") or ""
                role = getattr(turn, "role", "") or ""
                if role.lower() not in {"user", "assistant"}:
                    continue
                tokens += self._count_tokens(content)

        return max(tokens + 32, 1)

    def _count_tokens(self, text: str) -> int:
        if not text:
            return 0

        encoding = self._get_encoding()
        return len(encoding.encode(text))

    def _get_encoding(self):
        if self._encoding is not None:
            return self._encoding

        if tiktoken is None:
            class _FallbackEncoding:
                @staticmethod
                def encode(text: str) -> list[str]:
                    return re.findall(r"\w+|[^\w\s]", text, flags=re.UNICODE)

            self._encoding = _FallbackEncoding()
            return self._encoding

        try:
            self._encoding = tiktoken.encoding_for_model(self.settings.OPENAI_MODEL)
        except Exception:
            self._encoding = tiktoken.get_encoding("cl100k_base")
        return self._encoding

    def _safe_session_id(self, session_id: str) -> str:
        cleaned = re.sub(r"[^a-zA-Z0-9._:-]", "-", (session_id or "default").strip())
        return cleaned[:128] or "default"

    def _parse_or_create_visitor_id(self, raw_cookie: str) -> tuple[str, bool]:
        if raw_cookie:
            parsed = self._verify_visitor_token(raw_cookie)
            if parsed:
                return parsed, False

        return uuid.uuid4().hex, True

    def _sign_visitor_id(self, visitor_id: str) -> str:
        signature = hmac.new(
            self._runtime_secret.encode("utf-8"),
            visitor_id.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        return f"{visitor_id}.{signature}"

    def _verify_visitor_token(self, token: str) -> str | None:
        if "." not in token:
            return None

        visitor_id, signature = token.rsplit(".", 1)
        expected = hmac.new(
            self._runtime_secret.encode("utf-8"),
            visitor_id.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        if hmac.compare_digest(signature, expected):
            return visitor_id
        return None

    def _extract_client_ip(self, request: Request) -> str:
        headers = request.headers
        forwarded_for = headers.get("x-forwarded-for", "").split(",", 1)[0].strip()
        if forwarded_for:
            return forwarded_for

        return (
            headers.get("cf-connecting-ip")
            or headers.get("x-real-ip")
            or (request.client.host if request.client else "unknown")
            or "unknown"
        )


_ABUSE_GUARD: AbuseGuard | None = None


def get_abuse_guard() -> AbuseGuard:
    global _ABUSE_GUARD
    if _ABUSE_GUARD is None:
        _ABUSE_GUARD = AbuseGuard()
    return _ABUSE_GUARD
