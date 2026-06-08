# Repository Organization

| Path | Responsibility | Notes |
|---|---|---|
| `app/main.py` | Main FastAPI app | Registers routes, CORS, startup hydration, fullscreen chatbot page. |
| `app/site_app.py` | Admissions site wrapper | Serves the VNR page and injects the floating chatbot widget. |
| `app/api/chat.py` | Chat orchestration | Session memory, guided flows, final formatting, streaming. |
| `app/api/admin.py` | Admin dashboard | Contact requests and cutoff-cache management. |
| `app/classifier/intent_classifier.py` | Intent routing | Keyword-first, multilingual LLM fallback. |
| `app/logic/cutoff_engine.py` | Cutoff logic | Exact rank lookup, normalization, eligibility, branch/category lists. |
| `app/logic/cutoff_cache.py` | In-memory cache | Hydrates from Firestore, snapshot, or seed data. |
| `app/logic/contact_requests.py` | Lead capture | Firestore persistence and optional notifications. |
| `app/rag/retriever.py` | Knowledge retrieval | Pinecone + translation + local-doc fallback. |
| `app/data/init_db.py` | Firestore bootstrap | Seeds the cutoff collection and initializes Firebase. |
| `app/utils/*` | Parsing and multilingual helpers | Branch/category/gender extraction, language labels, sanitization, token tools. |
| `docs/` | Source docs and local text corpus | Also used as a fallback retrieval corpus. |
| `tests/` | Regression coverage | Focuses on context handling, link formatting, and site routes. |

Dependency direction:
- `api` depends on `classifier`, `logic`, `rag`, and `utils`; `logic` depends on `data`, `config`, and `utils`; `rag` depends on `config` and `utils`.