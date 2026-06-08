# Deployment and Operations

| Topic | Notes |
|---|---|
| Local development | `python railway_start.py` for the main chatbot; `python site_app_start.py` for the wrapper site. |
| Build process | Dockerfile installs requirements and starts the chatbot entrypoint. |
| Multi-service run | `docker-compose.yml` runs chatbot and site with health checks and port separation. |
| Testing | `python -m pytest tests -v` is the main regression check. |
| Environment | `.env` is loaded from the project root by `app/config.py`. |

Operational constraints:
- Keep port separation intact: 8000 for the chatbot, 8001 for the site wrapper.
- Keep startup hydration paths stable so the cutoff cache is ready before serving traffic.