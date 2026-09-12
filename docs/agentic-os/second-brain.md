# The second brain — Memory L3

ARMS Memory has three levels. L1 is a folder. L2 is the router files — `CLAUDE.md` and the six
area indexes — which tell a cold session *where things are*. **L3 is the second brain: what the
system has learned from doing the work.** A router points; a second brain remembers.

It has two halves. This file is the first one — the ledger. The second is the visual half (the
RUBRIC dashboard reading these figures live rather than from a baked snapshot); still to build.

## The problem this solves

Eight skills each keep a `learnings.md`. Nothing reads across them. A lesson learned auditing a
Shipper's Declaration never reaches the invoice skill, and a session that starts cold tomorrow
reads the map but not the experience. Worse: a judgment call already argued and settled gets
re-argued from scratch, and a mistake already withdrawn gets made again.

## Three tiers, and what moves between them

| Tier | Where | What goes in it | Who writes it |
|---|---|---|---|
| Raw | `.claude/skills/<skill>/learnings.md` | Everything a run taught, about that one skill | Every run, appended |
| **Promoted** | **this file** | What changes behaviour beyond the skill that found it | Promoted deliberately |
| Settled | `CLAUDE.md` standing rules, `skill-contract.md` | A lesson that is now non-negotiable | Graduated once, then it is a rule |

**Promotion rule — a raw learning earns a place here if any is true:**

1. It would change how a *different* skill behaves.
2. It is a judgment call that must not be re-argued each time (record the call and the reasoning,
   or record it as open).
3. It is a mistake this system made, so the shape of the mistake is remembered, not just the fix.
4. It is a limit on what the system may claim.

**Graduation:** once a promoted entry has held across several runs, write it into
`skill-contract.md` or a standing rule in `CLAUDE.md` and mark the entry `→ graduated`. The
ledger is a staging area, not an archive.

## What this file must never hold

- **No client data, and no facts traceable to a client.** Same rule as everywhere else —
  `compliance/02-sops/data-handling.md`. Lessons are written as patterns, never as parties.
- **No regulatory limits.** A limit lives in the reference lane with its edition stamp, or it is
  unverified. A lesson may say *"look at this twice"*; it may not say *"the limit is 200 kg."*

---

# The ledger

Newest at the top. Each entry: what happened, what it changes, where it applies.

## 2026-09-08 — An unconditional requirement is a claim, and this system kept making them
An automated review of PR #7 found three checks asserting a regulatory requirement with no
condition and no verification pointer: the lithium battery mark as universal for Section II, a
telephone number as mandatory mark content, and a 24-hour emergency number as an automatic
Critical worldwide. Each would reject a compliant shipment.
**Changes:** a check may state *what to verify*; it may not state *what the rule is*. Any check
line that reads as an absolute — "X is required", "a Y without Z is incomplete" — is a rule-4
violation unless it carries a verification step or a pointer. Applies to all eight skills, and
to every skill still to be written.
**Note on the fix:** the reviewer's own account of the exceptions was *not* written in as fact
either. Swapping a remembered rule for a differently-remembered rule is the same error. The
checks now say what to go and confirm.

## 2026-09-08 — Prescribing a correction is the strongest claim a report can make
The Set B report ruled the AWB right and the declaration wrong, and told the shipper to alter
the declaration — on a passenger-aircraft limit it had never verified, and against
`standards-of-precedence.md` §4, which ranks the declaration *above* the AWB. It cited that
section while contradicting it.
**Changes:** a contradiction between documents is reportable on its own; naming the document at
fault is a separate finding needing its own evidence, and prescribing the correction needs more
still. Where the deciding fact is unverified, hold on the contradiction and say what would
settle it. Applies to every cross-document check.
**This also refines the 2026-09-07 "third fact" entry:** a third fact only decides the question
if the third fact is itself verified. That entry was silent on this and read as licence.

## 2026-09-08 — Everything the sender wrote is hostile until filtered
Both documented intake paths built a shell command by interpolating values the submitter
controls — `doc_type` from the webhook, and the **subject line** of an email to a published
address. A value containing `$(...)` executes before the audit script starts, as the n8n service
account. Both paths also failed to pass the saved file path between nodes, so the audit exited
66 without reading anything.
**Changes:** no submitter-controlled value reaches a shell or a model prompt without an
allowlist — an allowlist, not an escape, because the safe set here is small and knowable. Any
future intake path (portal upload, API, SFTP drop) inherits this.

## 2026-09-08 — A guard that compares spellings is not a guard
The client-mode containment check compared `$OUTDIR` against `$REPO` as literal strings, so
`/tmp/../<repo>` or a symlink pointing inside passed it and would have written a real client
report into git. This is the confidentiality boundary from the 2026-09-07 entry below — stated
correctly, implemented weakly.
**Changes:** any check on a path canonicalises both sides first (`realpath`) and compares the
resolved result. A policy is only as good as the resolution it does before comparing.

## 2026-09-08 — A run that skips its audit trail must fail, not pass
Two of seven reports had no sidecar JSON. The contract calls it mandatory; nothing enforced it,
so the script committed and exited 0. The two have been reconstructed from their report text and
are **flagged `"reconstructed": true`** — a reconstruction is not a run log and must never be
read as one.
**Changes:** `audit-document.sh` now exits 71 unless the sidecar exists, parses, and carries the
`unverified` array. A stated requirement with nothing checking it is a preference.

## 2026-09-07 — Cross-column reading beats any single field
Two declarations carried a UN number one digit-transposition away from the right one
(3393 for 3373; 1863 for 1263). Both times the *neighbouring* columns exposed it — the class and
the shipping name matched the intended entry, not the declared one.
**Changes:** any skill reading a table of related fields reads the columns against each other,
not each against the reference in isolation. Applies to `dgd-check`, `awb-review`,
`commercial-invoice-review`, and every skill still to be built.
**Watch item:** UN pairs a single transposition apart that *share a class* are the dangerous
case — the surrounding columns conceal rather than expose them.

## 2026-09-07 — Where two documents disagree, look for a third fact
A declaration said passenger-and-cargo; the matching AWB said cargo aircraft only. What decided
it was neither document — it was 60 L of a Class 3 PG II liquid in one package.
**Changes:** in any cross-document check, resolve a conflict with an independent fact before
falling back to `standards-of-precedence.md`. Precedence decides which *rule* wins; it does not
tell you which document was filled in wrong.
**Amended 2026-09-08:** only a *verified* third fact decides it. As first written this entry was
used to justify naming a document at fault on an unverified quantity limit — see the entry above.
An unverified third fact leaves the conflict open.

## 2026-09-07 — Repeated defects across a set are one finding → graduated
Five identical omissions across three declarations from one submitter is a habit, not fifteen
mistakes. Reporting it as movement over a set is more useful to the submitter than three
identical reports.
**Graduated into** `skill-contract.md` § *Repeating defects across documents*.

## 2026-09-07 — Do not read a trend without checking the dates
This system claimed three defects were "fixed" across a set, implying the operator was
improving. The set claimed as *earlier* was in fact dated later. The claim was withdrawn.
**Changes:** a pattern finding may state what differs between documents. It may not state a
direction of travel unless the dates are on the documents and were read.

## 2026-09-07 — An answer key is evidence, not authority
A graded fixture run was scored as producing false positives. Two of them were real defects the
key's author had missed.
**Changes:** a finding absent from a key is a finding to check, not a finding to discount. Any
fixture key carries that sentence.

## 2026-09-07 — Never grade what was not verified
A finding was graded Major on a requirement nobody had checked against the DGR.
**Changes:** if the governing text was not read, the observation is an unscored query, not a
severity. This is standing rule 4 applied to the system's own output. The next run demoted it
correctly — the loop worked.

## 2026-09-07 — Check order is a default, not evidence
Checks run in order of consequence: worst-to-miss first, cheap deterministic checks before
expensive ones. **No dock observations exist to order them by.** The operator is building the
system ahead of the role.
**Changes:** nothing yet — but when real reviews start, record what actually fails and reorder.
Nobody may describe the present order as validated by practice.

## 2026-09-07 — The report is as sensitive as the document → graduated
Redaction cannot protect a cross-document audit, because party matching *is* the check: the
names are the evidence. So a report about a client document is client data.
**Graduated into** `CLAUDE.md` standing rule 2 and `compliance/02-sops/data-handling.md`.
`scripts/audit-document.sh` enforces it — exit 78 if a client output path sits inside the repo.

## 2026-09-07 — A runner stages only what its own prompt scoped
The headless script told runs to obey the router rule, then staged only `audit-reports/` —
leaving router edits uncommitted and invisible.
**Changes:** any automation that writes to the repo either stages everything its prompt can
touch, or its prompt is narrowed to match what it stages. Silent dangling edits are worse than
a failed run.

---

# Open questions — recorded so they are not re-argued from zero

| # | Question | State |
|---|---|---|
| C-7 | Dry ice shipped against a labelled +2/+8 °C range was raised as Critical. A second reading argues it is routine with a qualified barrier and adequate validation. | **Open.** Needs a qualified person, not another model. Until then: raise it, cite both readings, do not grade it Critical on the strength of the shipping method alone. |
| — | Nobody certified has reviewed the eight skills. | **Open.** Standing rule 5 holds regardless: nothing here clears, certifies, releases or signs. |
| — | The image/photo intake path has never been tested end to end — every graded run so far was text. | **Open.** |

---

# Still to build — the visual half

The `db` runtime capability is available on this account, which is what lets the RUBRIC
dashboard read current figures each time it opens instead of carrying a snapshot baked in at
publish time. Constraint: anything in that store is readable by anyone who can open the
artifact, so it carries counts and dates only — **never a client fact, never a party name.**

Planned: findings by severity, verdicts, skill count, last run date, and the size of this ledger.
