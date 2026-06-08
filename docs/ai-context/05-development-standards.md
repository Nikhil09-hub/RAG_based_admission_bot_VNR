# Development Standards

| Area | Standard |
|---|---|
| Coding conventions | Keep helpers small, name behavior clearly, and avoid broad rewrites. |
| Folder conventions | New business rules belong in `app/logic`; request handling belongs in `app/api`; parsing belongs in `app/utils`. |
| API design | Prefer explicit Pydantic request/response models and metadata fields for downstream UI use. |
| Error handling | Fail closed for missing cutoff data; return localized fallback messages for retrieval and streaming failures. |
| Logging | Use module loggers; log hydration/source failures and route-level exceptions without leaking secrets. |
| Testing | Add focused tests for behavior changes in routing, normalization, formatting, and site rendering. |

Implementation pattern to prefer:
- Put normalization in one place, then reuse it at the routing boundary instead of duplicating parsing logic downstream.