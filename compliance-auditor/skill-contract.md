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

## Repeating defects across documents

When more than one document from the same submitter is audited in one session, check for
defects that **repeat**, and report them as one pattern finding rather than separately in each
report.

A defect on three documents out of three is not three findings. It is a habit, and naming it as
one tells the submitter something the individual reports cannot: that the cause is a process or
a template, not a slip.

- [ ] After auditing the set, list every defect appearing on more than one document
- [ ] State the count plainly — "on 3 of 3 declarations"
- [ ] Put it in a **Repeating defects** section, above the individual reports or in a covering
      note, whichever the submission shape allows
- [ ] Say what the pattern implies: a blank field on every document usually means a template or
      a step in the filling routine, not carelessness on one form

Order the pattern list by severity, then by how many documents it appears on.

This works in the other direction too. A defect appearing on **one** document out of several
otherwise-correct ones is evidence it is an outlier — worth saying, because it changes the fix
from "retrain the process" to "correct this form".

## After the run — learning

1. **Append to the skill's `learnings.md`.** Every run, newest at the top: what the document did
   that the skill did not expect, what the skill missed, what to change.
2. **Promote what reaches beyond this skill** to `docs/agentic-os/second-brain.md` — a lesson
   that would change another skill's behaviour, a judgment call that must not be re-argued, a
   mistake this system made, or a limit on what it may claim. That file states the rule.
3. Neither file carries client facts or regulatory limits. Patterns, not parties; pointers, not
   numbers.

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
