---
name: lithium-battery-section-2
description: Review a lithium battery air shipment under IATA DGR Packing Instructions 965-970 — UN3480, UN3481, UN3090, UN3091, which section applies, state of charge, the lithium battery mark, aircraft limitation, and whether a Shipper's Declaration is required. Use when a document mentions lithium batteries, lithium ion, lithium metal, UN3480, UN3481, UN3090, UN3091, PI 965, PI 966, PI 967, PI 968, PI 969, PI 970, watt-hours, cells and batteries, power banks, or equipment shipped with batteries installed.
---

# Lithium batteries — Section II

**One job:** determine which UN number, packing instruction and section apply, then audit the
shipment against them. Dry ice goes to `dry-ice-un1845`; the AWB to `awb-review`.

> **Section is the whole decision.** Section IA, IB and II carry different documentation,
> marking and aircraft rules for the same UN number. Getting the section wrong makes every
> later check wrong, so check 1 decides it before anything else runs.

Contract: `compliance-auditor/skill-contract.md`
Precedence: `compliance-auditor/standards-of-precedence.md`
Output shape: `compliance-auditor/audit-report-template.md`
Checklist that outranks this file: `dgr/05-checklists/dg-checklist-non-radioactive-reference.md`

## Run in this order — read only the file you are on

| # | Check | File |
|---|-------|------|
| 1 | UN number, packing instruction, and which section applies | `checks/01-classification.md` |
| 2 | Section II eligibility — the size thresholds | `checks/02-section-II-limits.md` |
| 3 | State of charge and aircraft limitation | `checks/03-charge-and-aircraft.md` |
| 4 | Marking, labelling and the lithium battery mark | `checks/04-marking.md` |
| 5 | Documentation — and whether a DGD is required at all | `checks/05-documentation.md` |
| 6 | Cross-document agreement | `checks/06-cross-document.md` |

Run all six. Do not stop at the first failure.

## The contract

- **Never state a watt-hour, lithium-content or package limit from memory.** These are the most
  frequently revised figures in the DGR. Verify against the operator's own 67th ed. copy or
  record the check as unverified. See `skill-contract.md` rule 3.
- Section II is a **relief**, not a default. A shipment only qualifies if it meets every
  threshold. Where eligibility cannot be established, treat it as not qualifying and say so.
- Operator variations bite hardest on this commodity — many carriers restrict or forbid
  lithium batteries beyond the base DGR. An operator variation that is stricter governs.
- Everything in `skill-contract.md` applies.

## After the run

Write the sidecar JSON beside the report per `skill-contract.md`.
Append what surprised you to `learnings.md`.
