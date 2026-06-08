# Data and API

## Data Layer

| Area | Details |
|---|---|
| Cutoff model | Branch, category/caste, year, round, gender, quota, cutoff/first/last rank, optional PH type. |
| Contact model | Name, email, phone, programme, query type, message, status, timestamp. |
| Retrieval | Cache-first Firestore query path with snapshot fallback and embedded seed fallback. |
| Storage | Firestore collection `cutoffs` for rank data; `contact_requests` for lead capture. |
| Performance | Startup hydration is important; keep request-time lookup lightweight. |

## API Layer

| Group | Endpoints |
|---|---|
| Chat | `POST /api/chat`, `POST /api/chat/stream`, `POST /api/chat/reset`, `GET /api/config/languages`, `GET /api/health` |
| Admin | `GET /admin/contacts`, `GET /admin/contacts/export`, `POST /admin/refresh-cutoff-cache`, `GET /admin/cutoff-cache-stats` |

Request/response expectations:
- Chat responses must preserve `response`, `intent`, `metadata`, and `options`.
- Final output must normalize URLs, list formatting, and language leakage before returning.