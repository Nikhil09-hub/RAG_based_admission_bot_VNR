# Quick Reference

| Item | Summary |
|---|---|
| Most important workflows | Chat routing, guided documents flow, guided cutoff flow, RAG fallback, contact request capture. |
| Most important commands | `python railway_start.py`, `python site_app_start.py`, `python -m pytest tests -v`, `docker-compose up -d`. |
| Critical decisions | Two FastAPI apps; cache-first cutoff lookup; Pinecone RAG with translation; final response normalization. |
| Key constraints | VNRVJIET-only scope, exact cutoff answers, weak admin auth, secret hygiene, clickable markdown links. |