---
name: corrected-package-review
description: Re-review a corrected document package against the findings from the first review — confirm each finding was actually closed, catch corrections that introduced a new defect, and carry forward anything the first review could not verify. Use when a client returns a corrected package, when documents are resubmitted after a HOLD or REJECT, for a second-pass review, a re-review, or any request to check that fixes were made properly.
---

# Corrected-package re-review

**One job:** decide whether the findings raised in the first review are actually closed, and
whether correcting them broke anything.

> **This is not a repeat of the first review.** A re-review that simply re-runs the original
> checks will report a clean document and miss the fact that finding C-3 was never addressed —
> or that fixing C-1 introduced a new Critical. The prior report is an input, not history.

This is the **$100 corrected-package re-review** sold on nexusaureainc.com. It is a distinct
product, and a client is entitled to a finding-by-finding answer, not a fresh opinion.

Contract: `compliance-auditor/skill-contract.md`
Precedence: `compliance-auditor/standards-of-precedence.md`
Output shape: `compliance-auditor/audit-report-template.md`

## Run in this order — read only the file you are on

| # | Check | File |
|---|-------|------|
| 1 | Pairing — is this the same shipment, and which report is v1? | `checks/01-pairing.md` |
| 2 | Closure — every prior finding, one at a time | `checks/02-closure.md` |
| 3 | Regression — what did correcting it break? | `checks/03-regression.md` |
| 4 | Carry-forward — what v1 could not verify does not vanish | `checks/04-carry-forward.md` |

Run all four. Check 1 gates the rest: without the prior report there is nothing to re-review.

## The contract

- **Every prior finding gets an explicit status.** Closed, not closed, partially closed, or
  closed incorrectly. Silence on a finding is a failure of this review, not an implied pass.
- **Do not accept a field as fixed because it changed.** A changed field can be wrong in a new
  way. Re-check it against the standard, not against the fact that it moved.
- **Re-run every Critical from first principles.** Cheap, and the alternative is telling a client
  their shipment is clear when it is not.
- **A re-review can raise new findings**, and often should — see check 3.
- Everything in `skill-contract.md` applies.

## Verdict

The verdict is about the package in front of you, not about progress. A package that closed six
of seven Criticals is still REJECT. Say what improved, then say what still blocks.

## After the run

Write the sidecar JSON, adding `prior_report` and `findings_closed` / `findings_open` counts.
Append what surprised you to `learnings.md`.
