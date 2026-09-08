# 02 — Workflow Hardening Report & Proposed Node Maps

**Date:** 2026-09-06
**Status: PROPOSALS ONLY. Nothing has been published, activated, deleted, overwritten, or altered.**

Read `00-inspection-report.md` first — it carries the evidence these proposals rest on, and the
labelling convention (**OBSERVED** = proven by a committed artifact; **INFERRED** = deduced from
documentation, must be confirmed against the export).

Findings are grouped **Critical Discrepancies** and **Recommended Fixes** per workflow.

---

## 0. Rollout order

Do not apply these in document order. Apply in dependency order:

| Step | What | Why first |
|---|---|---|
| 1 | `01-backup-and-export-sop.md` | Nothing changes without a backup. |
| 2 | Confirm D8 node-by-node in the export | If `continueOnFail` is set anywhere in a compliance path, that is the emergency, and it changes the priority of everything else. |
| 3 | Structured output contract (`03-review-envelope-contract.md`) | Every other control branches on `status`. Nothing can be gated until it exists. |
| 4 | Webhook authentication | Cheapest fix, largest exposure reduction, no compliance-logic risk. |
| 5 | Class-scope gate + fail-closed policy | Depends on step 3. |
| 6 | Redaction split + log retention | Depends on step 3. |
| 7 | Approval gate wiring (`04-approval-gate/`) | Depends on steps 3 and 5. |

One workflow at a time. Class 9 first — it is the lowest-consequence of the three DG lanes to get
wrong while you are learning the pattern. Prove it, then clone to Class 8 and Class 3.

---

## 1. Universal baseline — applies to all five workflows

### Critical Discrepancies

- **No workflow has an error workflow configured.** A failure mid-run currently ends the execution
  silently. In a compliance path, a silent failure and a clean pass are indistinguishable from the
  outside.
- **Failure behaviour on AI / image / file / API nodes is unverified (INFERRED — D8).** n8n's
  `onError: continueRegularOutput` and `alwaysOutputData: true` will emit an **empty item**
  downstream on failure. In these workflows that produces a review artifact generated from nothing,
  formatted identically to a real one, committed to the compliance record. This is the highest-
  severity plausible defect in the system and it is currently unmeasured.
- **Execution logs retain full document content (INFERRED — D9)**, outside whatever redaction is
  applied to the committed artifact.

### Recommended Fixes

**F-U1 — Set failure policy on every node that touches AI, images, files, or external APIs.**

| Setting | Value | Note |
|---|---|---|
| On Error | `Stop Workflow` | Never `Continue`. Never `Continue (using error output)` in a compliance path. |
| Always Output Data | **off** | On + a failure = an empty item that looks like a result. |
| Retry On Fail | on, `Max Tries 2`, `Wait 2000ms` | **Transport failures only.** A 429 or 502 is safe to retry — it produces no output to be inconsistent about. |
| Execute Once | on, where the node should see one submission | Prevents fan-out on a multi-item input. |

The retry distinction matters and is easy to get backwards: retrying a *network* failure is
retrying nothing. Retrying an AI node that *returned* a low-confidence answer is asking the same
question until you get a different answer — that is answer-shopping on a compliance decision. Retry
transport, never content.

**F-U2 — Create one shared error workflow, `Nexus Ops — Error Handler`, and set it as
`errorWorkflow` on all five.** It must: write a failure record to the audit trail (submission ID,
workflow, node, error class, timestamp — **not** the payload); notify you; and never retry, never
resume, never emit a partial result. A failed run must leave a visible gap in the audit trail, not
an invisible one.

**F-U3 — Execution log retention.**

| Setting | Value | Reason |
|---|---|---|
| Save successful production executions | **Do not save** | The compliance record must be the deliberate audit artifact, not an incidental log. Incidental logs are the ones nobody redacts. |
| Save failed production executions | Save | Needed for debugging. Assume these contain document content. |
| Save manual executions | Do not save | Manual runs are where real documents get used for testing. |
| Data retention (n8n Cloud → Settings) | Shortest your plan allows | Caps the exposure window on saved failures. |

Turning off success logging is only safe **after** the explicit audit trail exists (F-U4). Do these
in that order or you will have a window with no record at all.

**F-U4 — Explicit audit trail.** Append-only, one record per submission, holding: `submission_id`,
`workflow_name`, document hashes (**not** contents), `status`, `confidence`, discrepancy and
missing-information *counts*, gate decision, reviewer identity, timestamps. This is the compliance
record. It must survive log rotation and must contain no document content.

**F-U5 — No secrets in parameters.** Every key, token, and secret lives in the n8n credential store
and is referenced by credential, never typed into a node parameter, header value, or code node.
Verified by the `grep` in `01-backup-and-export-sop.md` §4 on every export.

---

## 2. Class 3 Flammable Liquids / Class 8 Corrosive Materials / Class 9 Misc. Dangerous Goods

One design, three instances. These three share a template today (identical 5-section output) and
should share a hardened template.

### Critical Discrepancies

**C-1 — Unredacted live document content committed to GitHub. (OBSERVED — D1)**
`nexus-core/dg-reviews/class-3/2026-09-05_203737.md` carries a real shipper name and address, a real
consignee name and address, a named signatory and a working emergency phone number, pushed to a git
remote. The same workflow, two hours earlier, produced a run labelled `TRAINING IMAGE (REDACTED)`.
Redaction is an operator habit here, not a control, and the habit broke the same day. Private-repo
status limits exposure; it does not remove it. Git history is permanent and a visibility change
re-exposes it retroactively.

**C-2 — No class-scope gate; a document was reviewed under the wrong class and reported anyway.
(OBSERVED — D2)** The Class 3 run at 20:37 reviewed a declaration containing only UN1845 (Class 9)
and a Division 6.2 line — no Class 3 material at all — and produced a full "Class 3 Dangerous Goods"
review, committed to the `class-3/` folder. The model *noticed* and said so, as item **#10 of 11** in
a prose list. The workflow did not act on it. Your audit trail now asserts a Class 3 review of a
document that carries no Class 3 goods.

For a DGR file this is the finding I would escalate first. It is not a formatting problem: a review
labelled with the wrong class, filed in the wrong class folder, is a record that misrepresents what
was checked. If that record is ever produced as evidence of diligence, it is worse than no record.

**C-3 — No status field. (OBSERVED — D3)** None of the artifacts contains a verdict, status, or
decision token. `AUDIT-ENGINE-PROMPT.md` §6 specifies `PASS / HOLD FOR CORRECTION / REJECT`; the
deployed template has no such section. Nothing downstream can branch. No gate can be enforced. The
outcome of a review is only discoverable by reading ~120 lines of prose.

**C-4 — No traceability from artifact to document. (OBSERVED — D4)** Header emits
`Documents submitted: sdoc` — a form-field key, not a document identity. No filename, no hash, no
submission ID. The 18:39 run had it right (`Source file: shippers-declaration-column-format-fillable.pdf`)
and it regressed. A compliance record you cannot tie to its source document does not evidence
anything.

**C-5 — No validation between model output and git write. (OBSERVED — D5)** All four artifacts open
with literal `\n\n` escape sequences instead of newlines — the commit body is a JSON-escaped string
written verbatim. The escaping itself is cosmetic. What it proves is not: whatever the model emits
reaches the remote unchecked.

**C-6 — Unauthenticated webhook. (INFERRED — D7)** Per `compliance-auditor/n8n-workflow-setup.md`,
the documented trigger is a plain POST webhook, binary enabled, no auth, no allow-list, no size or
MIME cap. Anyone with the URL can inject a document, spend your Anthropic budget, and cause a commit
to a Nexus Aurea repository. **Confirm against the live trigger nodes.**

**C-7 — No human approval step. (INFERRED — D10)** The path is trigger → AI → commit. The artifacts
substitute a written disclaimer for a structural gate: "a qualified dangerous-goods person must
verify this" is *printed in the output*, but nothing in the system requires that it happened before
the record was filed.

**C-8 — Output schema drifts between runs. (OBSERVED — D6)** `Source file:` → `Documents submitted:`;
4 sections → 5; two different H1 banners. Every prompt edit silently changes the shape of the
compliance record.

### Recommended Fixes

**F-1 — Authenticate the webhook.** n8n Webhook node → Authentication: **Header Auth**, bound to a
Header Auth credential (a long random value, generated in a password manager, stored only in the
n8n credential store). Add to the node's options: `Raw Body` off, `Binary Property` limited to the
expected field, and a maximum payload size. Then rotate the path: the current URL should be treated
as disclosed.

Header Auth is the right level here — this endpoint is called by your own phone shortcut, not by a
third party negotiating a handshake. It is one header, it is enforced by n8n before any node runs,
and it costs nothing per request.

**F-2 — Intake validation before spend.** An IF node immediately after the webhook, failing closed:
MIME type in `{application/pdf, image/jpeg, image/png}`; file count within a stated maximum; size
within a stated maximum; at least one file present. On failure → respond `415`/`413` and stop. No AI
node runs on an unvalidated payload. This is also your cost control: a rejected payload costs zero
Anthropic tokens.

**F-3 — Assign identity at intake.** A Code node generating `submission_id` (UUID) and, per file,
`sha256`, `bytes`, `mime`, `filename`. This is the fix for C-4 and it is a precondition for the
audit trail, the approval gate, and the redaction split. Hash first, before anything else touches
the payload.

**F-4 — Structured output, contract-pinned.** Replace free prose with the envelope in
`03-review-envelope-contract.md`, enforced by a Structured Output Parser bound to the JSON Schema.
A parse failure is a **stop**, never a fallback to prose. The human-readable markdown is then
*rendered from* the envelope, so prose and data can never disagree — which is what C-8 is.

**F-5 — Class-scope gate (fixes C-2).** A Code node after the parser, comparing
`declared_scope.class` (from the queue the submission entered) against `observed_scope.classes`
(what the model actually read off the document):

- Declared class **not** in observed classes → force `status = HOLD`, prepend a **critical**
  discrepancy `CLASS_SCOPE_MISMATCH`, and route to the approval gate as an exception. Never commit
  a class-labelled artifact for a document that does not carry that class.
- Observed classes include a class **beyond** the declared one → `status = HOLD` with
  `ADDITIONAL_CLASS_PRESENT`. A Class 8 queue reading a Class 8 + Division 6.2 document is a real
  finding, not noise.
- Observed scope empty or unreadable → `status = HUMAN_REVIEW_REQUIRED`. Never "no classes found,
  therefore fine".

**F-6 — Fail-closed decision policy (fixes C-3).** A Code node that computes `status` from the
envelope by rule, not by asking the model to self-assess:

```
if intake validation failed            -> REJECT_INTAKE
if class-scope mismatch                -> HOLD
if any discrepancy.severity == critical-> HOLD
if any missing_information.blocking    -> HOLD
if confidence < 0.85                   -> HUMAN_REVIEW_REQUIRED
if any evidence.legibility == low      -> HUMAN_REVIEW_REQUIRED
if discrepancies > 0 and evidence == 0 -> HUMAN_REVIEW_REQUIRED   (unsupported findings)
otherwise                              -> REVIEW_COMPLETE_NO_DISCREPANCIES_FOUND
```

Two deliberate choices in that ladder:

- **`PASS` is removed from the vocabulary.** `AUDIT-ENGINE-PROMPT.md` currently offers it. "PASS" on
  a DG document reads as a clearance, and this system must never issue one. The clean outcome is
  `REVIEW_COMPLETE_NO_DISCREPANCIES_FOUND` — which still requires a human, and still says only what
  it actually knows: nothing was found, by a draft reading aid, on the documents supplied.
- **The status is computed, not generated.** Asking a model to decide whether its own output is
  trustworthy is not a control. Deriving the status from countable facts is.

The 0.85 threshold is a starting point, not a regulatory number. Tune it against real submissions
and record the tuning; that record is itself audit evidence.

**F-7 — Redaction split (fixes C-1).** Two artifacts, two destinations:

| Artifact | Contents | Destination |
|---|---|---|
| **Public record** | `submission_id`, document `sha256`, status, confidence, discrepancy *types* and cited standards, missing-information *types*, evidence *locators* (`page 1, quantity column, line 1`) and legibility, recommended action, gate decision, reviewer, timestamps | git — `nexus-core/dg-reviews/<class>/` |
| **Working copy** | Everything above **plus** extracted field values — names, addresses, phone numbers, quoted text | Access-controlled store outside git, short retention |

Enforced by a Code node with a **field allow-list**, not a deny-list. A deny-list fails the moment a
document contains a field nobody thought of; an allow-list fails closed. Anything not explicitly
allowed does not reach the git write.

The evidence locator survives redaction, which is what makes this workable: `"page 1, quantity
column, line 1 — legibility: medium"` is fully reviewable without reproducing the shipper's address.

**F-8 — Human Approval & Exception Gate.** Insert `04-approval-gate/` between the decision policy
and every output action. Commit, notify, and file only on the branch the reviewer chose — and even
then, only the commit, never an operational action. See §7 for what stays prohibited regardless of
decision.

**F-9 — Render markdown from the envelope, and validate before writing (fixes C-5, C-8).** A Code
node renders the committed markdown from the validated envelope. Never string-concatenate model
output into a commit body. Assert before the git write: envelope schema-valid; `status` in
vocabulary; gate decision present; no field outside the allow-list. Any assertion fails → stop, and
the error workflow records the gap.

### Proposed node map — Class 3 / 8 / 9 (hardened)

```
[1] Webhook  (POST, Header Auth credential, size + binary limits)
     │
[2] IF: Intake valid?  (mime allow-list, file count, size, ≥1 file)
     ├── false ─→ [2a] Respond 415/413 ─→ [2b] Audit: REJECT_INTAKE ─→ ■ stop
     │            (no AI node runs; zero token spend)
     ▼ true
[3] Code: Assign Identity
     submission_id (uuid) · per-file sha256 / bytes / mime / filename · received_at
     │
[4] Audit Append: submission opened          ── (hashes only, never contents)
     │
[5] Anthropic Vision + Basic LLM Chain
     onError: stopWorkflow · alwaysOutputData: OFF
     retryOnFail: 2 × 2000ms  (transport failures only)
     │
[6] Structured Output Parser  → review-envelope.schema.json
     parse failure = STOP, never a prose fallback
     │
[7] Code: Class-Scope Gate       (F-5)   declared_scope vs observed_scope
     │
[8] Code: Decision Policy        (F-6)   computes status, fail-closed
     │
[9] Code: Redaction Split        (F-7)   allow-list → public record + working copy
     │
[10] Execute Workflow: Human Approval & Exception Gate  ◀── waits for a person
     │
[11] Switch on gate_result.decision
     ├── Acknowledged           → [12] Assert → [13] GitHub commit PUBLIC record → [16]
     ├── Returned for correction→ [14] Notify submitter (no commit)              → [16]
     └── Escalated              → [15] Notify escalation contact (no commit)     → [16]
     │
[16] Audit Append: closed  (status · gate decision · reviewer · timestamps)

  workflow settings:
    errorWorkflow ................. Nexus Ops — Error Handler
    save success executions ....... none      (audit trail is [4]/[16], not the log)
    save error executions ......... all
    save manual executions ........ none
```

Node [12] is the assertion gate from F-9 — the last thing before anything leaves the workflow.

---

## 3. Physical AI — Shipment Capture Sandbox

No workflow definition, no output artifact, and no design note exists in either repository. I cannot
report on what I cannot see, so this section is a **specification to check the live workflow
against**, not a finding list.

### Critical Discrepancies

- **Cannot assess.** Export required.

### Recommended Fixes — apply the same baseline, plus:

**F-P1 — "Sandbox" must be enforced, not named.** A workflow called a sandbox that writes to the
production audit trail, commits to a live repository, or notifies a real contact is not a sandbox.
Enforce it structurally: a separate webhook path, a separate output destination, and an
`environment: "sandbox"` field stamped into every record it produces and asserted before any write.

**F-P2 — Capture is not verification.** A photo of a package establishes what the camera saw at one
moment. It does not establish piece count, gross weight, package integrity, or label correctness.
The envelope's `status` for a capture must never be phrased as a confirmation. Use
`REVIEW_COMPLETE_NO_DISCREPANCIES_FOUND` at most, and put what the image cannot establish into
`missing_information` explicitly — the way the Class 3/8/9 engine already handles "cannot verify
from image".

**F-P3 — Route through the same approval gate.** `review_type: "physical_shipment_capture"`. The
gate is built to take it (`04-approval-gate/README.md` §5).

**F-P4 — Image retention.** Shipment photos capture labels, addresses, and marks. Same allow-list
split as F-7: the public record gets hashes and locators; images go to the access-controlled store
with a stated retention period. Never commit a shipment photo to git.

---

## 4. Market Watch

**Resolve the inventory question first (`00-inspection-report.md` §2): the committed Market Watch
automation is a claude.ai Routine, not an n8n workflow.** `ROUTINE-PROMPT.md` is written for
claude.ai → Routines; `n8n-analysis-prompt.md` describes an optional Anthropic node for a weekly n8n
version. If the n8n one is live, export it. If only the Routine is live, most of this section is
n/a and the relevant controls are the Routine's connector scope and output destination.

### Critical Discrepancies

- **None at compliance severity.** Market Watch produces research, not compliance decisions. It
  makes no client-facing, financial, or operational commitment, and the playbook already forbids
  advice and recommendations. It does not need the approval gate, and adding one would be exactly
  the complexity today's brief says not to add.

### Recommended Fixes

**F-M1 — Do not add the approval gate here.** Deliberate. This lane is research; gating it would add
friction with no compliance benefit.

**F-M2 — Keep the fail-closed data rules that already exist.** `ROUTINE-PROMPT.md` already carries
genuinely good controls that the DG lanes lack: freshness validation on every quote with a
documented failure case (CJMB, 2026-08-27), `DATA UNAVAILABLE` rather than omission, a ban on
`REALTIME_BULK_QUOTES` because it returns fabricated sample data on this plan, and taking the
session date from returned data rather than the system clock.

That last one deserves a note: the playbook says the environment clock "has been observed running
days behind". If that is true, it affects the DG lanes too — every artifact filename and
`Generated:` header in `dg-reviews/` comes from a clock. Check whether the DG timestamps are
trustworthy. A compliance record with a wrong date is a defective compliance record.

**F-M3 — Baseline hygiene only.** Apply F-U1 (stop on API failure — a partial market report is
misleading), F-U2 (error workflow), and F-U5 (no keys in parameters). Skip F-U3's success-log
suppression: there is nothing confidential in a market report, and the log is useful.

**F-M4 — Least-privilege the GitHub write.** Whatever token commits reports should be scoped to the
report paths, not to the whole repository. Same token review applies to the DG lanes.

---

## 5. Compliance Auditor (photo-in)

`compliance-auditor/n8n-workflow-setup.md` documents a complete node map, but this workflow is not
in your list of five. **Confirm whether it was built, folded into Class 3/8/9, or abandoned.**

If it is live, it inherits every finding in §2, and two more:

- **C-9 — The documented node map is trigger → AI → Gmail → GitHub commit, with no gate.** Both
  outputs are terminal actions taken automatically on model output. The Gmail send is the more
  serious of the two: a commit is internal, an email leaves the building.
- **C-10 — `AUDIT-ENGINE-PROMPT.md` §6 offers a `PASS` verdict.** Per F-6, remove it. A system that
  must never clear a shipment should not have a word for clearing one in its vocabulary.

If it is abandoned, mark `n8n-workflow-setup.md` as superseded so nobody builds from it later — the
unauthenticated webhook in §1 of that file is the origin of finding C-6.

---

## 6. Remediating the committed unredacted artifact (C-1)

`nexus-core/dg-reviews/class-3/2026-09-05_203737.md` is committed and in history. Deleting the file
in a new commit removes it from the working tree but **not** from history. Options, with honest
trade-offs — this is your call, not mine:

| Option | Effect | Cost |
|---|---|---|
| **A. Leave it, fix forward** | History retains the data. Repo stays private. | Zero effort. Accepts the exposure. Defensible only if the shipper is you or a consenting party — worth confirming, since the signatory name on the document is yours. |
| **B. Redact in a new commit** | Working tree clean; history retains it. | Low effort. Honest half-measure: stops casual discovery, not retrieval. |
| **C. Rewrite history** (`git filter-repo`) + rotate | Removes it from history. | Invalidates every existing clone. Requires force-push. GitHub may retain unreferenced objects until GC — open a support request to purge. |
| **D. Delete and rebuild the repo** | Cleanest removal. | Loses all history. |

**My recommendation: confirm consent first, then choose.** If the document is your own practice
paperwork with your own details, A or B is proportionate and you can move on to the structural fix
(F-7), which is what actually prevents recurrence. If it is a third party's document, C — and
promptly.

Either way, **F-7 is the fix.** Remediating the file without the redaction split just means the next
run re-commits the same class of data.

---

## 7. Prohibited automatic actions — unconditional

No workflow may perform any of these without a human performing it, regardless of status,
confidence, or gate decision. The gate records that a human reviewed; it never authorises action.

- Certify, sign, or clear any dangerous-goods document.
- Tender, book, release, or dispatch a shipment.
- Send anything to a client, shipper, consignee, carrier, or regulator.
- Alter, correct, or re-issue a source document.
- Make or commit a payment, quote, or financial obligation.
- Create or close a maintenance work order (see `06-rnd-multifamily-sandbox-concept.md`).
- Unlock, grant, or revoke physical access.

`04-approval-gate/`'s **Enforce No-Op Boundary** node asserts this in code and throws if any
boundary flag is not `false`. That is the mechanism; this list is the policy it enforces.

---

## 8. Scope boundaries reaffirmed

- These workflows are **draft assistive document review only**. Not a shipment-clearance system, not
  a certification system, not a regulatory filing system.
- **Class 3, 8, and 9 only.** Not Class 1 explosives, not ITAR/EAR-controlled items, not radioactive
  material. If a submission shows any of those, the correct outcome is `HOLD` with an escalation —
  never a review.
- No Alacran data, systems, workflows, credentials, or integrations are referenced anywhere in this
  hardening pass, and none should be introduced.
- No real API keys, client documents, PHI, or confidential data are in scope for testing. Use
  redacted practice documents, per `compliance-auditor/intake/README.md`.
