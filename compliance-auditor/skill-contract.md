# Skill Contract

The rules every Nexus Aurea compliance skill obeys. Skills cite this file rather than
restating it. If a skill contradicts this file, this file wins.

## Ground rules

1. **The strictest applicable requirement governs.** Apply `standards-of-precedence.md`.
   Every finding names the level it came from. A flag without a cited standard is not a finding.
2. **Read what is written.** Never assume a field is present because it usually is. A field you
   cannot read is **"cannot verify from image"** — never a guess, never an invented value.
3. **Never state a regulatory limit from memory.** Packing instruction quantities, proper
   shipping names, specification ranges: verify against the governing document, or record the
   check as unverified. A remembered figure must never become the basis of a finding.
4. **Reality beats paper.** Where the package contradicts the paperwork, the paperwork is what
   gets corrected.
5. **Nothing here clears, certifies, releases or signs.** Skills flag and correct. A qualified
   person signs before tender; a QP or MA holder makes any product-release decision.
6. **Never PASS with an open Critical.** Verdict is HOLD FOR CORRECTION or REJECT.
7. **Stay in your lane.** A skill does its one job. Note what belongs to another skill and move
   on rather than half-doing it.

## Severity

Per `standards-of-precedence.md` section 5 — 🔴 Critical, 🟡 Major, 🟢 Minor.

## Output shape

`audit-report-template.md`. Do not restate that format inside a skill; point at it.

## Sidecar log

Every report saved to `audit-reports/` gets a JSON file beside it, same basename, `.json`.
This is the audit trail — it is how a finding gets defended months later.

```json
{
  "skill": "dry-ice-un1845",
  "run": "2026-09-07T21:14:00Z",
  "documents": ["AWB 020-4471 8822", "DGD p1 of 1"],
  "references_read": [
    "compliance-auditor/standards-of-precedence.md",
    "audit-lab/dry-ice-un1845/dry-ice-review-checklist.md"
  ],
  "precedence_levels_cited": ["IATA DGR 67th ed.", "State variation USG"],
  "findings": { "critical": 1, "major": 2, "minor": 0 },
  "unverified": ["PI 954 limit — no DGR copy to hand"],
  "verdict": "HOLD FOR CORRECTION"
}
```

`unverified` is not optional. It is the honest record of what the run could not confirm.
