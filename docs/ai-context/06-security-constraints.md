# Security Constraints

| Area | Constraint |
|---|---|
| Sensitive areas | `.env`, Firestore credentials, OpenAI keys, Pinecone keys, SMTP credentials, Google Sheets credentials. |
| Authentication | Chat endpoints are public; admin endpoints must not be expanded without real auth. |
| Authorization | Admin password gate exists, but it is temporary and weak. |
| Rate limiting | `RATE_LIMIT_PER_MINUTE` is configured; do not assume enforced throttling unless implemented in code. |
| Input validation | Sanitize user input before processing; keep length limits and HTML escaping intact. |
| Secrets handling | Keep secrets out of source and docs; use environment variables or secret storage only. |

Regression risk:
- Loosening cutoff scope, admin access, or input validation can expose data or broaden behavior beyond the college-only domain.