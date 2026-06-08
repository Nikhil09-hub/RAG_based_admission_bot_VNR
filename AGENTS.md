# Agent Context Entry Point

Use this repository context system before broad code exploration.

Read order:
1. [docs/ai-context/README.md](docs/ai-context/README.md)
2. The single topic file that matches the task
3. The owning implementation file if you need verification

Rules:
- Treat source code as the authority; the context files are a compressed map.
- Prefer the smallest relevant context file over scanning the whole repo.
- Do not store secrets or duplicate code snippets here.
- Update the matching context file when behavior, routes, workflows, or constraints change.

High-signal source files:
- [app/main.py](app/main.py)
- [app/api/chat.py](app/api/chat.py)
- [app/api/admin.py](app/api/admin.py)
- [app/logic/cutoff_engine.py](app/logic/cutoff_engine.py)
- [app/logic/cutoff_cache.py](app/logic/cutoff_cache.py)
- [app/rag/retriever.py](app/rag/retriever.py)
- [app/data/init_db.py](app/data/init_db.py)
- [app/config.py](app/config.py)
 - [app/logic/turnstile_service.py](app/logic/turnstile_service.py)  # server-side Turnstile verification
 - [app/logic/abuse_guard.py](app/logic/abuse_guard.py)  # abuse escalation now may require Turnstile
 - [app/classifier/intent_classifier.py](app/classifier/intent_classifier.py)  # deterministic multilingual allowlist
 - [app/frontend/widget.js](app/frontend/widget.js)  # Turnstile widget integration + retry logic
 - [app/frontend/widget.html](app/frontend/widget.html)
 - [app/frontend/widget.css](app/frontend/widget.css)

Notes:
- Turnstile integration is controlled via `ENABLE_TURNSTILE`, `TURNSTILE_SITE_KEY`, and `TURNSTILE_SECRET_KEY` in `app/config.py`.
- When enabled, suspicious chat requests are escalated to a challenge flow that returns `{"requires_turnstile": true}` instead of hard 429 blocks.
- The intent classifier contains a deterministic multilingual allowlist that short-circuits some LLM fallbacks; update tests if you change keyword lists.

Abuse guard:
- [app/logic/abuse_guard.py](app/logic/abuse_guard.py) — centralizes rate-limit and abuse decisions. When `ENABLE_TURNSTILE` is true the guard may set `challenge_required` instead of returning a 429; callers should respond with `{"requires_turnstile": true}` and allow the frontend to surface the Turnstile widget. The guard populates `request.state.abuse_identity` used for concise Turnstile logging.