# Learnings — coa-review

Append after every run. Newest at the top. A few lines each.

```
## YYYY-MM-DD — <document ref>
- What the document did that the skill did not expect:
- What the skill got wrong or missed:
- Change to make:
```

---

## Provenance of the check order — read before reordering

The checks are ordered by **consequence**: what would be worst to miss runs first, and
deterministic checks that cost nothing run before expensive ones.

They are **not** ordered by observed failure rate. As of 2026-09-07 no dock observations exist
to order them by — the operator is building the system ahead of the role, per the standing rule
in `CLAUDE.md`. Consequence-ordering is the right default in that position, but it is a
default, not evidence.

**When real reviews start, that changes.** Record what actually fails, and reorder to match.
Until then nobody should read this order as validated by practice.

No runs yet. The first real review starts this file.
