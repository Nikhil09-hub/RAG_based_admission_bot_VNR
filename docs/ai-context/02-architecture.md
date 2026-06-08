# Architecture

| Area | Details |
|---|---|
| High-level design | Two FastAPI apps: main chatbot on port 8000 and admissions site wrapper on port 8001. |
| Main request path | `/api/chat` handles normalization, guided flows, intent classification, then routes to cutoff or RAG. |
| Major components | `app/main.py`, `app/api/chat.py`, `app/api/admin.py`, `app/classifier`, `app/logic`, `app/rag`, `app/data`, `app/utils`. |
| Data flow | User message -> session/language state -> intent/rule checks -> Firestore or Pinecone/local fallback -> response finalization. |
| External integrations | OpenAI, Pinecone, Firestore, SMTP, Google Sheets. |
| Auth flow | No user auth for chat. Admin actions use a password gate only; treat as temporary and weak. |

Key architectural constraint:
- Cutoff results are exact lookups from cache-backed Firestore data; the system should not invent or approximate ranks.