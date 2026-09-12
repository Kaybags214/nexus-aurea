---
name: dry-ice-un1845
description: Verify dry ice (UN1845, Carbon dioxide solid) documentation on an air shipment — net weight per package in kg, Class 9 marking, PI 954 limits, AWB handling information, and weight agreement across AWB, DGD, invoice and packing list. Use when a document mentions dry ice, UN1845, carbon dioxide solid, a refrigerant, frozen or -20C/-70C shipping, or when reviewing any cold-chain air shipment that could be refrigerated with dry ice.
---

# Dry ice / UN1845

**One job:** decide whether the dry ice on this shipment is documented correctly.
Lithium batteries, excursions, invoices belong to other skills — note and move on.

Contract: `compliance-auditor/skill-contract.md`
Precedence: `compliance-auditor/standards-of-precedence.md`
Output shape: `compliance-auditor/audit-report-template.md`
Operator checklist, which outranks this file: `audit-lab/dry-ice-un1845/dry-ice-review-checklist.md`

## Run in this order — read only the file you are on

| # | Check | File |
|---|-------|------|
| 1 | Is a DGD required at all? Decide first — it sets which checks apply | `checks/01-shipment-type.md` |
| 2 | Identity and net weight — the highest-risk fields | `checks/02-identity-and-weight.md` |
| 3 | Marking, labelling, venting | `checks/03-marking.md` |
| 4 | AWB handling information | `checks/04-awb-entry.md` |
| 5 | Cross-document weight agreement | `checks/05-cross-document.md` |

Run all five. Do not stop at the first failure.

## The contract

- A missing or pounds-only dry ice net weight is **Critical**, every time. It is the most
  common reject at acceptance.
- Never compute a sublimation allowance and present it as the declared weight. If asked whether
  the ice lasts the transit, verify against the packaging's tested sublimation rate and the real
  door-to-door time, label it an estimate, and keep it out of the findings.
- Do not raise a missing-DGD finding until check 1 says one is required.
- Everything in `skill-contract.md` applies.

## After the run

Write the sidecar JSON beside the report per `skill-contract.md`.
Append what surprised you to `learnings.md`.
