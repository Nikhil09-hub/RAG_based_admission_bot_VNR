from __future__ import annotations

import pytest

import app.api.chat as chat_api
import app.logic.abuse_guard as abuse_guard_module
from app.classifier.intent_classifier import ClassificationResult, IntentType


@pytest.fixture(autouse=True)
def reset_chatbot_state():
    def force_info(_: str) -> ClassificationResult:
        return ClassificationResult(
            intent=IntentType.INFORMATIONAL,
            confidence=1.0,
            reason="forced informational behavior",
        )

    chat_api.classify = force_info
    chat_api._DOCUMENT_FLOW_STATE_BY_SESSION.clear()
    chat_api._DOCUMENT_SLOT_MEMORY_BY_SESSION.clear()
    chat_api._SESSION_LANGUAGE_BY_ID.clear()
    chat_api._SESSION_CONTEXT_BY_ID.clear()
    chat_api._SESSION_CUTOFF_SLOT_MEMORY_BY_SESSION.clear()
    abuse_guard_module._ABUSE_GUARD = None
    yield
    chat_api._DOCUMENT_FLOW_STATE_BY_SESSION.clear()
    chat_api._DOCUMENT_SLOT_MEMORY_BY_SESSION.clear()
    chat_api._SESSION_LANGUAGE_BY_ID.clear()
    chat_api._SESSION_CONTEXT_BY_ID.clear()
    chat_api._SESSION_CUTOFF_SLOT_MEMORY_BY_SESSION.clear()
    abuse_guard_module._ABUSE_GUARD = None
