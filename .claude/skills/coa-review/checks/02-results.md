# Check 2 — Test results against specification

Build this table. One row per test on the certificate — no summarising.

| Test | Method / ref | Specification | Result | Within spec? |
|---|---|---|---|---|
| | | | | |

- [ ] Every test on the certificate has a stated specification
- [ ] Every test has a result — no blanks, no "conforms" without a value where a value is expected
- [ ] Every result carries its unit
- [ ] Analytical method or pharmacopoeial reference named per test
- [ ] Results compared to limits only as printed

## Findings

- A result **outside** its stated specification → **Critical**
- A result with **no stated specification** → **Major**, and marked unverifiable, not passing
- A result missing its unit → **Major**; a number without a unit is not a result
- Method not stated → **Minor** to **Major** depending on the test

## What you may not do

- Do not round, convert or recalculate a result to bring it inside a limit
- Do not supply a specification limit from memory or from a different product's monograph —
  see `skill-contract.md` rule 3
- Do not treat "conforms" as a result where the specification calls for a numeric value

## Out-of-specification results

An OOS result on a shipped lot is Critical and the report says so plainly. Whether the lot was
subject to an approved OOS investigation and released anyway is the MA holder's record to
produce — ask for it; do not assume it exists, and do not assume it does not.
