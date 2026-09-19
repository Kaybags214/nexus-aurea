---
name: excursion-assessment
description: Assess a cold-chain temperature excursion against the product's labelled storage range — logger data integrity, magnitude and duration out of range, cumulative time-out-of-range across the lane, and the documentation a quality decision needs. Use when reviewing a temperature log, data logger report, excursion report, cold-chain deviation, or any shipment where product went outside +2/+8, -20C or -70C storage conditions.
---

# Cold-chain excursion assessment

**One job:** characterise the excursion precisely and assemble what a quality decision needs.

> **This skill does not decide whether product is fit for use.** Only the Marketing
> Authorisation holder or a Qualified Person releases product after an excursion. Producing a
> "product is fine" conclusion here would be practising quality release without authority.
> You describe; they decide. See `skill-contract.md` rule 5.

Contract: `compliance-auditor/skill-contract.md`
Precedence: `compliance-auditor/standards-of-precedence.md` section 2
Output shape: `compliance-auditor/audit-report-template.md`

## Run in this order — read only the file you are on

| # | Check | File |
|---|-------|------|
| 1 | Establish the governing range — the product label is the floor | `checks/01-governing-range.md` |
| 2 | Logger and data integrity — before trusting any number | `checks/02-logger-integrity.md` |
| 3 | Characterise the excursion — magnitude, duration, cumulative | `checks/03-characterise.md` |
| 4 | Assemble the quality decision package | `checks/04-decision-package.md` |

Run all four in order. Check 2 gates checks 3 and 4 — untrustworthy data cannot be characterised.

## The contract

- **The product's labelled storage condition is the floor and is never widened.** Not by a
  carrier SOP, not by a customer agreement, not by "it was only slightly over".
- Never compute mean kinetic temperature and present it as a pass. MKT is an input to a quality
  decision, not a verdict, and it can mask a short excursion that matters.
- Never state a product's stability budget or allowable time-out-of-refrigeration from memory.
  It comes from the MA holder's stability data or it is unverified.
- Everything in `skill-contract.md` applies.

## After the run

Write the sidecar JSON beside the report per `skill-contract.md`.
Append what surprised you to `learnings.md`.
