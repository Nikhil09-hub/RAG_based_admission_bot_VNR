# Business Logic

| Topic | Rules |
|---|---|
| Core rules | Cutoff answers are exact, scope-limited, and should say when data is missing. |
| Priority rules | Required-documents flow and guided cutoff flow run before general classification. |
| Validation rules | Ranks ignore year-like numbers; branch/category/gender/quota extraction is regex-based and conservative. |
| Edge cases | Short follow-ups need context; "both" genders are treated as combined cutoff lookup; noisy repeated words are collapsed. |
| Non-obvious decisions | Non-English queries are translated for retrieval, but responses remain in the user’s language. |
| Scope restrictions | Cutoff support is limited to B.Tech under Convener quota; non-convener requests are rejected. |

Regression-sensitive behavior:
- Session-memory handling for follow-ups.
- URL rewriting into clickable markdown links.
- Guided cutoff step ordering and back-navigation.
- Category normalization, especially SC variants and legacy aliases.