# Learnings — commercial-invoice-review

Append after every run. Newest at the top. A few lines each.

```
## YYYY-MM-DD — <document ref>
- What the document did that the skill did not expect:
- What the skill got wrong or missed:
- Change to make:
```

---

## 2026-09-07 — Set A commercial invoice, handwritten (first real run)

- **Check 2 could not complete.** The skill requires recomputing every line total and the
  invoice total. Handwritten figures were not legible enough to do that with confidence, so the
  finding became "cannot be reconciled, restate legibly" rather than a specific arithmetic
  error. **That is the right outcome** — inventing a reading to complete the check would have
  been worse than reporting it unreadable. Check 2 should say so explicitly: where figures
  cannot be read, the finding is illegibility, not a computed discrepancy.
- **Check 4's restraint held.** Line 2 carried "A B2" where an HS heading belongs. The skill
  reported it as malformed and referred it to a broker rather than supplying a code. Line 1's
  2811.21 for carbon dioxide was correctly formatted and plausible, and the skill said plausible
  rather than correct. Both are the intended behaviour.
- **The strongest finding came from cross-document, not from the invoice alone.** Net weight
  "30kg" against 3.0 kg elsewhere is only visible with the declaration and AWB alongside. An
  invoice audited on its own would have passed that field. Reinforces check 5 and the note there
  about marking single-document reviews as not reconciled.
- **Absent commercial terms clustered.** Invoice number, Incoterm, currency, payment terms and
  purpose of shipment were all blank together — a form filled for the goods and not for the
  trade. Worth watching whether that clusters again; if so it is one finding about how the form
  is approached, not five.

No prior runs. This file starts here.

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
