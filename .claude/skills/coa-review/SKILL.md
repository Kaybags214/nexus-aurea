---
name: coa-review
description: Review a pharmaceutical Certificate of Analysis against the product specification — identity and lot traceability, every test result against its limit, dates and retest period, and authorised signature. Use when reviewing a CoA, Certificate of Analysis, certificate of conformance, batch analysis certificate, or a QC release document accompanying a pharmaceutical or biological shipment.
---

# Certificate of Analysis review

**One job:** verify the CoA is complete, internally consistent, and traceable to the shipment.

> This skill does not release product or judge fitness for use. It verifies the certificate.
> A result inside spec on paper is not a release decision. See `skill-contract.md` rule 5.

Contract: `compliance-auditor/skill-contract.md`
Precedence: `compliance-auditor/standards-of-precedence.md` section 2
Output shape: `compliance-auditor/audit-report-template.md`
Reference lane: `pharma/02-certificate-of-analysis/`

## Run in this order — read only the file you are on

| # | Check | File |
|---|-------|------|
| 1 | Identity and lot traceability to the shipment | `checks/01-identity.md` |
| 2 | Test results against specification, line by line | `checks/02-results.md` |
| 3 | Dates, retest period and shelf life | `checks/03-dates.md` |
| 4 | Authorisation and document integrity | `checks/04-authorisation.md` |

Run all four.

## The contract

- **Never state a specification limit from memory.** The limit comes from the specification
  document or the CoA itself. An unsourced limit is not a comparison.
- A CoA without a stated specification for a result is not "passing" — it is unverifiable.
  Report it as such.
- Never recalculate or round a reported result to make it fit a limit.
- Everything in `skill-contract.md` applies.

## After the run

Write the sidecar JSON beside the report per `skill-contract.md`.
Append what surprised you to `learnings.md`.
