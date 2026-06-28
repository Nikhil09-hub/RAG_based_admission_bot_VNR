from dataclasses import dataclass
from enum import Enum


class MetaIntent(Enum):
    IDENTITY = "identity"
    CAPABILITIES = "capabilities"
    LANGUAGES = "languages"
    CREATOR = "creator"
    AI = "ai"
    UNKNOWN = "unknown"


@dataclass
class MetaResponse:
    response: str
    intent: str = "meta"

# Identity questions
_IDENTITY_KEYWORDS = [
    "who are you",
    "what are you",
    "introduce yourself",
    "tell me about yourself",
]

# Capability questions
_CAPABILITY_KEYWORDS = [
    "what can you do",
    "how can you help",
    "what questions can i ask",
    "what all can you do",
    "what services do you provide",
    "how do you help",
]

# Language questions
_LANGUAGE_KEYWORDS = [
    "what languages do you support",
    "which languages do you support",
    "can you speak",
    "can you understand",
    "which language",
]

# Creator questions
_CREATOR_KEYWORDS = [
    "who created you",
    "who made you",
    "who built you",
    "who developed you",
]

# AI questions
_AI_KEYWORDS = [
    "are you ai",
    "are you an ai",
    "are you chatgpt",
    "are you a bot",
    "are you human",
]

def classify_meta(query: str) -> MetaIntent:
    """
    Classify the type of meta question asked by the user.
    """
    q = query.strip().lower()

    if any(keyword in q for keyword in _IDENTITY_KEYWORDS):
        return MetaIntent.IDENTITY

    if any(keyword in q for keyword in _CAPABILITY_KEYWORDS):
        return MetaIntent.CAPABILITIES

    if any(keyword in q for keyword in _LANGUAGE_KEYWORDS):
        return MetaIntent.LANGUAGES

    if any(keyword in q for keyword in _CREATOR_KEYWORDS):
        return MetaIntent.CREATOR

    if any(keyword in q for keyword in _AI_KEYWORDS):
        return MetaIntent.AI

    return MetaIntent.UNKNOWN


def _identity_response() -> str:
    return (
        "I am the official VNRVJIET Admissions Assistant. 🎓\n\n"
        "I'm here to help prospective students and parents with information "
        "about admissions, cutoff ranks, fee structure, hostel facilities, "
        "placements, scholarships, required documents, and campus life."
    )

def _capability_response() -> str:
    return (
        "I can help you with:\n\n"
        "• Admission process\n"
        "• Eligibility\n"
        "• Cutoff ranks\n"
        "• Fee structure\n"
        "• Hostel information\n"
        "• Placements\n"
        "• Scholarships\n"
        "• Required documents\n"
        "• Campus facilities\n"
        "• Clubs and student activities"
    )

def _language_response() -> str:
    return (
        "I currently support conversations in:\n\n"
        "• English\n"
        "• Telugu\n"
        "• Hindi\n"
        "• Tamil\n"
        "• Kannada\n"
        "• Marathi\n"
        "• Bengali\n"
        "• Gujarati"
    )
def _creator_response() -> str:
    return (
        "I was developed as the official VNRVJIET Admissions Assistant "
        "to help students and parents quickly access admission-related information."
    )
def _ai_response() -> str:
    return (
        "Yes! I am an AI-powered admissions assistant designed to answer "
        "questions related to VNRVJIET admissions and campus information."
    )

def _unknown_response() -> str:
    return (
        "I'm here to answer questions about myself and how I can help with "
        "VNRVJIET admissions."
    )
def handle_meta_query(query: str) -> MetaResponse:
    """
    Handle meta questions about the chatbot.
    """
    meta_intent = classify_meta(query)

    if meta_intent == MetaIntent.IDENTITY:
        return MetaResponse(response=_identity_response())

    if meta_intent == MetaIntent.CAPABILITIES:
        return MetaResponse(response=_capability_response())

    if meta_intent == MetaIntent.LANGUAGES:
        return MetaResponse(response=_language_response())

    if meta_intent == MetaIntent.CREATOR:
        return MetaResponse(response=_creator_response())

    if meta_intent == MetaIntent.AI:
        return MetaResponse(response=_ai_response())

    return MetaResponse(response=_unknown_response())