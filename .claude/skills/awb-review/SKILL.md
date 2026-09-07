---
name: awb-review
description: Review an Air Waybill for completeness and internal consistency — 11-digit AWB number check digit, shipper and consignee, piece count, gross and chargeable weight, handling information, DG and dry ice references, and agreement with the invoice and packing list. Use when reviewing an AWB, air waybill, MAWB or HAWB, or when a shipment's transport document needs checking before tender.
---

# Air Waybill review

**One job:** audit the AWB and its agreement with the other documents in the shipment.
Dry ice specifics go to `dry-ice-un1845`; the declaration goes to `dgd-check`. Note and move on.

Contract: `compliance-auditor/skill-contract.md`
Precedence: `compliance-auditor/standards-of-precedence.md`
Output shape: `compliance-auditor/audit-report-template.md`

## Run in this order — read only the file you are on

| # | Check | File |
|---|-------|------|
| 1 | AWB number and check digit — deterministic, run it first | `checks/01-number.md` |
| 2 | Parties and routing | `checks/02-parties.md` |
| 3 | Pieces, weight and charges | `checks/03-weight.md` |
| 4 | Nature and Quantity, handling information | `checks/04-goods.md` |
| 5 | Declarations, signatures, execution | `checks/05-execution.md` |
| 6 | Cross-document agreement | `checks/06-cross-document.md` |

Run all six. Do not stop at the first failure.

## The contract

- A failed check digit is **Critical**, not a typo to correct quietly — the number does not
  exist, and the fix needs the real one from the carrier.
- Within one shipment the AWB outranks invoice and packing list, and is outranked by the DGD
  and by the physical package.
- Do not normalise a name or address to make two documents agree. The mismatch is the finding.
- Everything in `skill-contract.md` applies.

## After the run

Write the sidecar JSON beside the report per `skill-contract.md`.
Append what surprised you to `learnings.md`.
