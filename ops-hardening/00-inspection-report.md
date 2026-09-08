# 00 — Inspection Report

**Date:** 2026-09-06
**Scope:** Existing n8n workflow structure; Nexus Aurea client-intake portal.
**Status of this document:** Findings only. Nothing was published, activated, deleted, overwritten, or altered.

---

## 1. What I could and could not inspect

| Asset | Inspected? | How |
|---|---|---|
| n8n Cloud workflow definitions (all five) | **No** | This session has no n8n Cloud credential, no n8n API access, and no n8n MCP server. Live workflows are unreachable from here. |
| Workflow design documentation in git | Yes | `kaybags214/nexus-aurea` |
| Workflow **output artifacts** committed by the running workflows | Yes | `kaybags214/nexus-core` → `dg-reviews/` (4 files) |
| Client-intake portal source | **No** | Not present in either GitHub repository. Stated as local-only and uncommitted to remote. |

> **Read this before the hardening report.** Because no workflow JSON exists anywhere in git and
> the live instance is unreachable, the node-level findings below are inferred from **committed
> output artifacts** — the actual bytes the workflows produced and pushed. That is strong evidence
> for what the output path does and weak evidence for what the trigger and error paths do. Every
> finding is labelled **OBSERVED** (proven by an artifact) or **INFERRED** (deduced, must be
> confirmed against the exported JSON).

---

## 2. Inventory reconciliation

You listed five n8n Cloud workflows. Here is what exists in evidence:

| # | Workflow as named | Evidence found | Discrepancy |
|---|---|---|---|
| 1 | Market Watch | `market-watch/ROUTINE-PROMPT.md`, `SETUP-WALKTHROUGH.md`, `n8n-analysis-prompt.md` | **The committed Market Watch automation is a claude.ai Routine, not an n8n workflow.** `ROUTINE-PROMPT.md` says "paste this as the prompt when recreating the routine in claude.ai > Routines", schedule 4:32 PM ET, connectors Alpha Vantage + Crypto.com. `n8n-analysis-prompt.md` describes an *optional* Anthropic node for a "weekly Market-Watch workflow". Two different systems share one name. **Confirm which one is live.** |
| 2 | Class 3 Flammable Liquids | 2 output artifacts in `nexus-core/dg-reviews/class-3/` | No workflow definition in git. |
| 3 | Class 8 Corrosive Materials | 1 output artifact in `nexus-core/dg-reviews/class-8/` | No workflow definition in git. |
| 4 | Class 9 Misc. Dangerous Goods | 1 output artifact in `nexus-core/dg-reviews/class-9/` | No workflow definition in git. |
| 5 | Physical AI — Shipment Capture Sandbox | **None** | No definition, no output, no design note in either repository. |
| — | Compliance Auditor (photo-in) | `compliance-auditor/n8n-workflow-setup.md` — a full node map | **Documented but not in your list of five.** Confirm whether it was built, folded into the Class 3/8/9 workflows, or abandoned. It matters: its documented node map has an unauthenticated webhook and a direct GitHub-commit output. |

`nexus-core/automation/` and `nexus-core/ai-configs/` exist but contain only `.gitkeep`. **There is no
workflow backup anywhere.** If the n8n Cloud tenant were lost today, all five workflows would be
unrecoverable.

---

## 3. Observed artifacts (the evidence base)

Four review outputs, all committed to `kaybags214/Nexus-Core` (private) on 2026-09-05:

| File | Time | Source document read | Header document identity |
|---|---|---|---|
| `dg-reviews/class-3/2026-09-05_183908.md` | 18:39:08 | Shipper's Declaration, labelled "TRAINING IMAGE (REDACTED)" | `Source file: shippers-declaration-column-format-fillable.pdf` |
| `dg-reviews/class-3/2026-09-05_203737.md` | 20:37:37 | Shipper's Declaration — UN1845 + UN3393 | `Documents submitted: sdoc` |
| `dg-reviews/class-8/2026-09-05_203934.md` | 20:39:34 | Shipper's Declaration — UN1830, PG II, PI 851 | `Documents submitted: sdoc` |
| `dg-reviews/class-9/2026-09-05_204101.md` | 20:41:01 | Shipper's Declaration | `Documents submitted: sdoc` |

All four share an identical 5-section template: Extracted Fields → (Cross-Document Consistency) →
Possible Document Discrepancies → Unable to Verify → Human-Review Recommendations.

### 3.1 The AI layer is sound — do not rebuild it

This is worth stating plainly before the defect list, because the instruction for today was not to
rebuild working things. The review engine's *substance* is good:

- It refuses to infer. `"Gross weight: no labeled gross-weight field on this form; cannot be
  derived, and volumes in L must not be converted to kg."` — correct, and exactly the failure mode
  that gets a DGD rejected.
- It carries **per-field read confidence** (High / Medium / Low) and separates "the field is blank"
  from "I cannot read the field": `"AWB number | (blank — no entry) | High (that it is blank)"`.
- It caught real shipper errors: a Packing Group entered against UN1845 Class 9 dry ice and against
  a Division 6.2 entry (neither takes a PG); and a `UN3393` / "Biological Substances category B" /
  PI 650 pairing that does not hold together — Category B is **UN3373** with PI 650, and UN3393 is a
  different substance entirely. It flagged both as "verify against current DGR" rather than
  asserting a correction. That is the right posture.
- It refused to certify: every artifact opens with a draft-only banner and closes with
  "Human review by a qualified dangerous-goods person is required."

**The defects below are in the plumbing — routing, output contract, redaction, traceability — not
in the analysis.** Harden the pipe; leave the engine alone.

### 3.2 Defects proven by the artifacts

**OBSERVED — D1. Unredacted live document content is committed to GitHub.**
`class-3/2026-09-05_203737.md` lines 12–17 and 44–47 contain a real shipper name and street
address, a real consignee name and street address, a named signatory, and a working emergency
telephone number, extracted from a live Shipper's Declaration and pushed to a git remote. The
18:39 run on the same day was explicitly labelled `TRAINING IMAGE (REDACTED)`; the 20:37 run is
not. Redaction is therefore an operator habit, not a control — and the habit broke within two hours.
This contradicts `nexus-aurea/README.md` ("Do not store confidential customer documents unless
redacted") and `compliance-auditor/intake/README.md`. The repository is private, which limits
exposure but does not remove it: git history is permanent, and a visibility flip re-exposes
everything retroactively.

**OBSERVED — D2. No class-scope gate. A document was reviewed under the wrong class and produced a
full report anyway.** The Class 3 run at 20:37 read a declaration whose only entries were UN1845
(Class 9) and a Division 6.2 line. There is no Class 3 material on the document. The workflow
produced a complete "Class 3 Dangerous Goods" review regardless. The mis-routing surfaces only as
item **#10 of 11** in a prose discrepancy list — `"this review was framed as a Class 3 review, but
no Class 3 entries appear on this document. Possible mis-routing of the file to the wrong review
queue."` The workflow did not halt, did not downgrade its status, and committed a class-labelled
artifact to a class-labelled folder. The audit trail now asserts a Class 3 review of a document
that carries no Class 3 goods.

**OBSERVED — D3. No machine-readable status field exists.** None of the four artifacts contains a
status, verdict, or decision token. `AUDIT-ENGINE-PROMPT.md` §6 specifies a
`PASS / HOLD FOR CORRECTION / REJECT` verdict, but the deployed Class 3/8/9 template has no such
section — it ends at "Human-Review Recommendations". Consequences: nothing downstream can branch on
outcome; no gate can be enforced in code; and determining whether a submission is blocked requires a
human to read ~120 lines of prose. This is the single blocker to everything else in today's
objectives — the approval gate cannot be wired in until a status field exists.

**OBSERVED — D4. Document identity is not recorded; traceability is broken.** The three newer
artifacts emit `**Documents submitted:** sdoc`. `sdoc` is a form-field key, not a filename. The
older 18:39 artifact correctly emitted the real filename. Somewhere between those two runs the
header started reporting the multipart field name instead of the document identity. **You cannot
currently tie a committed review back to the document it reviewed.** No filename, no hash, no
submission ID, no page count.

**OBSERVED — D5. The GitHub commit body is an unvalidated escaped string.** All four artifacts begin
with a single physical line containing literal backslash-n sequences —
`# Class 3 ... Review\n\n**Generated:** ...\n\n**Model:** claude-opus-5\n\n> Draft assistive
review only...` — instead of real newlines. The commit node is writing a JSON-escaped string
without unescaping it. Cosmetically minor; structurally it proves there is **no validation step
between the model output and the git write**. Whatever the model emits goes to the remote verbatim.

**OBSERVED — D6. Output schema drifts between runs.** `Source file:` (18:39) became
`Documents submitted:` (20:37). The 18:39 artifact has 4 sections; the later ones have 5. Two
different top-level H1 banners are in use. Without a pinned contract, every prompt edit silently
changes the shape of the compliance record.

### 3.3 Defects inferred from documentation

**INFERRED — D7. Unauthenticated webhook.** `compliance-auditor/n8n-workflow-setup.md` §1 specifies
a plain `n8n-nodes-base.webhook`, POST, binary/form-data enabled, at
`https://<your-n8n>/webhook/compliance-audit` — with no authentication, no shared secret, no
allow-list, and no size or MIME limit. Anyone who learns or guesses the URL can inject a document,
consume Anthropic API spend, and cause a commit to a Nexus Aurea repository. Must be confirmed
against the live Class 3/8/9 trigger nodes.

**INFERRED — D8. No error workflow, no failure policy.** No error handling appears in any design
document. n8n's defaults do not stop a workflow on a node failure if `continueOnFail` /
`onError: continueRegularOutput` is set, and `alwaysOutputData` will emit an empty item downstream.
Either setting on an AI, image, file, or API node in a compliance path produces the worst possible
outcome: a review artifact that looks complete but was generated from an empty or partial input.
**This must be verified node-by-node in the export before anything else is changed.**

**INFERRED — D9. Execution logs retain document content.** n8n Cloud saves production execution data
by default. Every binary document, every extracted field, every model prompt is retained in the
execution log at full fidelity, outside the redaction discipline applied to the committed artifact.

**INFERRED — D10. No human approval step exists anywhere.** No design document describes one, and
none of the four artifacts records a reviewer, decision, or timestamp. The path is
trigger → AI → commit, uninterrupted. The artifacts substitute a *textual disclaimer* for a
*structural gate*: "a qualified person must verify this" is written in the output, but nothing in
the system requires that it happened.

---

## 4. Client-intake portal

Not present in `kaybags214/nexus-aurea` or `kaybags214/Nexus-Core`. Per your description it is built
and committed to a local repository, not deployed, with no real credentials configured.

I could not inspect it, so I have not written findings about it. `05-portal-predeploy-checklist.md`
is a **pre-deployment gate** to run against it — not an audit of it. The single most useful thing
you can do before it is deployed is push it to a private remote (or run the checklist locally) so it
can be reviewed while it still has no real credentials in it. That is the cheapest moment in its
lifetime to fix a secrets-handling defect.

---

## 5. What I need from you to complete the inspection

1. **Exports of all five workflows** — see `01-backup-and-export-sop.md`. Sanitised, as described
   there. Without these, D7–D10 stay inferences.
2. **Confirmation on Market Watch** — n8n workflow, claude.ai Routine, or both?
3. **Confirmation on Compliance Auditor** — built, folded into Class 3/8/9, or abandoned?
4. **Confirmation on Physical AI — Shipment Capture Sandbox** — it produced no artifact and has no
   design note. Does it exist yet?
5. **A decision on D1** — the unredacted artifact is committed and in history. Options are in
   `02-hardening-report.md` §6.
