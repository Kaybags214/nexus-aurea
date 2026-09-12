---
name: commercial-invoice-review
description: Review a commercial invoice for customs and trade compliance — parties and identifiers, line-item arithmetic and totals, Incoterms 2020 with named place, country of origin, HS heading plausibility, and agreement with the AWB and packing list. Use when reviewing a commercial invoice, proforma invoice, customs invoice, or the value and classification documents supporting an import or export entry.
---

# Commercial invoice review

**One job:** audit the invoice for customs sufficiency and internal consistency.
The AWB goes to `awb-review`. Full classification research is not this skill.

Contract: `compliance-auditor/skill-contract.md`
Precedence: `compliance-auditor/standards-of-precedence.md` section 3 —
**destination customs authority has final say on classification and valuation.**
Output shape: `compliance-auditor/audit-report-template.md`
Reference lanes: `customs/03-hs-codes/`, `templates/03-commercial-invoice/`

## Run in this order — read only the file you are on

| # | Check | File |
|---|-------|------|
| 1 | Parties, identifiers and required declarations | `checks/01-parties.md` |
| 2 | Line items and arithmetic — recompute every total | `checks/02-arithmetic.md` |
| 3 | Incoterms 2020 and currency | `checks/03-terms.md` |
| 4 | Origin and HS heading plausibility | `checks/04-origin-hs.md` |
| 5 | Agreement with AWB and packing list | `checks/05-cross-document.md` |

Run all five.

## The contract

- **Never assign an HS code.** This skill checks plausibility and internal consistency only.
  Classification is a determination for the destination authority or a licensed broker.
- Recompute every total. Do not accept a printed total because it looks right.
- Never adjust a value, quantity or term to make the arithmetic close. The discrepancy is the
  finding.
- Everything in `skill-contract.md` applies.

## After the run

Write the sidecar JSON beside the report per `skill-contract.md`.
Append what surprised you to `learnings.md`.
