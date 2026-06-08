"""Cloudflare Turnstile verification helper."""

from __future__ import annotations

import asyncio
import json
import logging
from dataclasses import dataclass, field
from typing import Any
from urllib import parse, request as urlrequest

from app.config import get_settings

logger = logging.getLogger(__name__)

TURNSTILE_VERIFY_URL = "https://challenges.cloudflare.com/turnstile/v0/siteverify"


@dataclass(frozen=True)
class TurnstileVerificationResult:
    success: bool
    error_codes: list[str] = field(default_factory=list)
    raw_response: dict[str, Any] = field(default_factory=dict)


def _post_verification(payload: dict[str, str]) -> dict[str, Any]:
    data = parse.urlencode(payload).encode("utf-8")
    req = urlrequest.Request(
        TURNSTILE_VERIFY_URL,
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    with urlrequest.urlopen(req, timeout=5) as response:
        body = response.read().decode("utf-8")
        return json.loads(body or "{}")


async def verify_turnstile_token(token: str, remote_ip: str | None = None) -> TurnstileVerificationResult:
    settings = get_settings()
    if not settings.ENABLE_TURNSTILE:
        return TurnstileVerificationResult(success=True)

    if not token:
        logger.warning("Turnstile verification failed: missing token")
        return TurnstileVerificationResult(success=False, error_codes=["missing-input-response"])

    if not settings.TURNSTILE_SECRET_KEY:
        logger.warning("Turnstile verification failed: missing secret key")
        return TurnstileVerificationResult(success=False, error_codes=["missing-secret-key"])

    payload = {
        "secret": settings.TURNSTILE_SECRET_KEY,
        "response": token,
    }
    if remote_ip:
        payload["remoteip"] = remote_ip

    try:
        result = await asyncio.to_thread(_post_verification, payload)
    except Exception as exc:  # pragma: no cover - network failure path
        logger.warning("Turnstile verification error: %s", exc)
        return TurnstileVerificationResult(success=False, error_codes=["verification-error"])

    success = bool(result.get("success"))
    error_codes = [str(code) for code in (result.get("error-codes") or [])]

    if success:
        logger.info("Turnstile verification success for ip=%s", remote_ip or "unknown")
    else:
        logger.warning(
            "Turnstile verification failure for ip=%s errors=%s",
            remote_ip or "unknown",
            error_codes,
        )

    return TurnstileVerificationResult(success=success, error_codes=error_codes, raw_response=result)