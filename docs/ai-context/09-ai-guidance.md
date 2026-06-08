# AI Guidance

## Rarely Modify

- Response finalization in `app/api/chat.py`.
- Guided cutoff flow and session-state helpers.
- Cutoff normalization and rank resolution logic.
- Cache hydration and fallback ordering.
- Widget/page injection in `app/main.py` and `app/site_app.py`.

## Common Mistakes

- Treating README text as authoritative when code says otherwise.
- Broadening cutoff support beyond the B.Tech + Convener rule.
- Breaking markdown link conversion or list formatting.
- Resetting session state too aggressively and losing follow-up context.
- Adding new behavior without updating the matching tests.

## Required Checks

- Run the smallest focused test for the touched behavior.
- Verify route or formatting changes with the existing regression tests.
- If data flow changes, confirm cache hydration and fallback paths still work.

## Preferred Patterns

- Make the smallest local edit that preserves current behavior shape.
- Add a helper if it centralizes normalization used in multiple paths.
- Keep user-facing messages localized and concise.

## Classifier guidance

- The intent classifier now contains a deterministic multilingual allowlist which is checked before invoking any LLM or RAG fallback. Changes to the keyword lists (languages or college signals) can materially change routing — update tests and quick-reference notes when editing the lists.
- Prefer deterministic rules for domain-signals (cutoff, eligibility, department names) and reserve probabilistic models for ambiguous cases.