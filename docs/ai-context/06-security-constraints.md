# Security Constraints

| Area | Constraint |
|---|---|
| Sensitive areas | `.env`, Firestore credentials, OpenAI keys, Pinecone keys, SMTP credentials, Google Sheets credentials. |
| Authentication | Chat endpoints are public; admin endpoints must not be expanded without real auth. |
| Authorization | Admin password gate exists, but it is temporary and weak. |
| Rate limiting | `RATE_LIMIT_PER_MINUTE` is configured; do not assume enforced throttling unless implemented in code. |
| Input validation | Sanitize user input before processing; keep length limits and HTML escaping intact. |
| Secrets handling | Keep secrets out of source and docs; use environment variables or secret storage only. |

| Bot protection | Cloudflare Turnstile may be enabled via `ENABLE_TURNSTILE`. When enabled the server verifies tokens server-side using `TURNSTILE_SECRET_KEY` and the verification service in `app/logic/turnstile_service.py`. Do not log secret values or full tokens. |

| Logging | Turnstile verification emits concise success/failure logs containing `session_id` and the first 8 chars of `visitor_id` (example: `Turnstile success | session=%s | visitor=%s`). Keep logs free of secrets. |

Regression risk:
- Loosening cutoff scope, admin access, or input validation can expose data or broaden behavior beyond the college-only domain.