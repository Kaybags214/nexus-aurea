# Learnings — dry-ice-un1845

Append after every run. Newest at the top. A few lines each.

```
## YYYY-MM-DD — <document ref>
- What the document did that the skill did not expect:
- What the skill got wrong or missed:
- Change to make:
```

---

## 2026-09-07 — FIXTURE-001 (synthetic AWB + packing list + invoice)

First run of the skill. Machinery works: router loaded, all five check files were read in
order, output matched the report template, sidecar log written.

- **Check 1 did its job.** Concluded no DGD required and said so explicitly, so the missing
  declaration was not raised as a false Critical. That trap is the reason the check was moved
  to first position, and it held.
- **Check 5 caught more than expected.** The piece-count and truncated-shipper defects were
  written expecting `awb-review` to catch them, but check 5's "package count agrees with the
  AWB piece count" and "shipper and consignee agree" lines caught both. Overlap between the
  two skills here is useful, not duplicated effort.
- **Two real defects were absent from the fixture's own answer key** — the AWB dry ice entry
  showing no package count, and the aircraft type not being determinable. Both were caught by
  the checklist. Lesson: the checklist beat a deliberately constructed key. Argument for
  running every check rather than reviewing by eye.
- **One call was over-confident.** Class 9 missing from the AWB *text entry* was raised as
  Major. It is a real absence, but whether the class is required in that entry was not
  verified against a DGR copy. It should have been raised as a query, not a Major finding.
  **Change to make:** check 2 should say that where a requirement itself is unverified, the
  finding is logged as a query in `unverified`, not assigned a severity.
- **Limitation of this run:** the fixture was written by the same run that audited it. This
  tested plumbing, not diagnostic judgment on unseen material. Not evidence the skill reads a
  real document well.

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
