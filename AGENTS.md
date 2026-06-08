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