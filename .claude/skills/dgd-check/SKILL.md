---
name: dgd-check
description: Check a Shipper's Declaration for Dangerous Goods for completeness, correct classification, packing instruction, aircraft limitation, emergency contact and signature, and agreement with the Air Waybill. Use when reviewing a DGD, Shipper's Declaration, dangerous goods declaration, or any air shipment carrying a UN number that requires declared dangerous goods.
---

# Shipper's Declaration for Dangerous Goods

**One job:** audit the DGD. The AWB goes to `awb-review`; dry ice detail to `dry-ice-un1845`.

Where this document and the AWB disagree the DGD wins — but the physical package outranks both.
**State variations for origin, transit AND destination all apply, and stack with operator
variations.** A shipment satisfying IATA DGR but violating a destination variation still fails.

Contract: `compliance-auditor/skill-contract.md`
Precedence: `compliance-auditor/standards-of-precedence.md`
Output shape: `compliance-auditor/audit-report-template.md`
Checklist that outranks this file: `dgr/05-checklists/dg-checklist-non-radioactive-reference.md`

## Run in this order — read only the file you are on

| # | Check | File |
|---|-------|------|
| 1 | Header, routing, pagination | `checks/01-header.md` |
| 2 | Classification, line by line | `checks/02-classification.md` |
| 3 | Aircraft limitation | `checks/03-aircraft.md` |
| 4 | Emergency contact and certification | `checks/04-certification.md` |
| 5 | Form condition — alterations, border, copies | `checks/05-form-condition.md` |
| 6 | Agreement with the AWB | `checks/06-vs-awb.md` |

Run all six. Do not stop at the first failure.

## The contract

- Never supply a packing instruction, PSN or UN number you are not certain of. Say
  **"cannot verify — confirm against DGR 67th ed."** and log it as unverified.
- An unsigned, altered or overwritten form is not correctable in the report. The fix is a
  fresh form.
- Everything in `skill-contract.md` applies.

## After the run

Write the sidecar JSON beside the report per `skill-contract.md`.
Append what surprised you to `learnings.md`.
