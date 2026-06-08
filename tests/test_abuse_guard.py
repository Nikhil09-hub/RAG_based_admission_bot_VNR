from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_public_requests_receive_visitor_cookie():
    response = client.get("/api/config/languages")

    assert response.status_code == 200
    assert "vnrvjiet_vid=" in response.headers.get("set-cookie", "")


def test_streaming_chat_returns_429_when_guard_blocks(monkeypatch):
    import app.api.chat as chat_api

    class FakeIdentity:
        issued_new_cookie = False

    class FakeGuard:
        async def resolve_identity(self, request):
            return FakeIdentity()

        def apply_cookie(self, response, identity, request):
            return None

        async def evaluate_chat_request(self, request, session_id, user_message, chat_history=None):
            from app.logic.abuse_guard import AbuseDecision

            return AbuseDecision(
                allowed=False,
                status_code=429,
                reason="Too many requests. Please wait and try again.",
                retry_after=60,
                headers={"Retry-After": "60", "X-Abuse-Reason": "test"},
            )

    monkeypatch.setattr(chat_api, "get_abuse_guard", lambda: FakeGuard())

    response = client.post(
        "/api/chat/stream",
        json={"message": "hello", "session_id": "abuse-test", "language": "en"},
    )

    assert response.status_code == 429
    assert response.headers.get("x-abuse-reason") == "test"
