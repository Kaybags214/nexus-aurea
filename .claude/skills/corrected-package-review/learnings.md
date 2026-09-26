# Learnings — corrected-package-review

Append after every run. Newest at the top.

```
## YYYY-MM-DD — <shipment ref / prior report>
- What the correction did that the skill did not expect:
- What the skill got wrong or missed:
- Change to make:
```

---

## Provenance

Built 2026-09-08 because the $100 corrected-package re-review is sold on the website and nothing
implemented it. A client could have bought it and received a re-run of the original checks —
which would report a clean document while a finding sat unaddressed.

Check 3 (regression) is the reason this is a separate skill rather than a flag on the others.
The failure mode it exists for — a correction that fixes one field and breaks another — is
invisible to any review that only looks at what changed.

**Never run against a real corrected package.** The closure statuses, and particularly "closed
incorrectly", are untested against a real client correction.

No runs yet.
