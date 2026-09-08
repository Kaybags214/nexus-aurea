# 04 — Human Approval & Exception Gate

**File:** `human-approval-exception-gate.draft.json`
**Version:** 1.0.0-draft · **`"active": false`** · credential-free · 10 nodes

A reusable n8n sub-workflow that puts a named human between a system review and any action taken on
it. **It records a decision. It never takes one.**

**Draft only. Do not activate.** Import it, read it, decide whether the shape is right, then wire it.

---

## 1. What problem it solves

Finding C-7 in `02-hardening-report.md`: the Class 3/8/9 path runs trigger → AI → commit with no
human in it. The artifacts *say* a qualified person must verify — every one of them opens with a
draft-only banner and closes with a human-review instruction — but nothing in the system requires
that it happened before the record was filed.

That gap is the difference between a **written disclaimer** and a **structural gate**. A disclaimer
is a sentence in the output. A gate is a node the execution cannot get past. This is the gate.

---

## 2. Required inputs

All nine are mandatory. The gate hard-fails if any is missing — including the arrays, which must be
sent as `[]` rather than omitted. *Absent* and *none* are different claims and the gate refuses to
conflate them.

| Input | Type | |
|---|---|---|
| `workflow_name` | string | |
| `submission_id` | string | |
| `review_type` | string | `dg_document_review` · `physical_shipment_capture` · `building_maintenance_alert` |
| `system_status` | string | Must be in the allowed vocabulary — see §3 |
| `confidence` | number | 0–1 |
| `discrepancies` | array | `[]` if none |
| `missing_information` | array | `[]` if none |
| `evidence` | array | `[]` if none |
| `recommended_human_action` | object | |

These are exactly the fields of the review envelope (`../03-review-envelope-contract.md`), so a
calling workflow passes its envelope straight through.

---

## 3. What the gate refuses

`Validate Gate Input` throws — stopping the execution — on any of:

- **A missing required field.** Named in the error.
- **A `system_status` outside the vocabulary.** Allowed: `HOLD`, `HUMAN_REVIEW_REQUIRED`,
  `REVIEW_COMPLETE_NO_DISCREPANCIES_FOUND`, `REJECT_INTAKE`. Clearance-shaped words — `PASS`,
  `CLEARED`, `APPROVED`, `CERTIFIED` — are rejected by design. If a caller sends one, the caller is
  wrong and the gate says so rather than quietly accepting it.
- **A `confidence` that is not a number in 0–1.**
- **An array field sent as something other than an array.**
- **Discrepancies asserted with zero evidence.** A finding with no evidence locator cannot be
  reviewed, so asking a human to review it is asking them to rubber-stamp. The gate treats this as
  a defect in the caller, not an edge case to tolerate.

Every one of these is a **stop**, never a continue. There is no `continueOnFail` anywhere in this
workflow and `alwaysOutputData` is off on every node.

---

## 4. Reviewer options

Exactly three, rendered as a required dropdown:

| Option | Meaning | Comments |
|---|---|---|
| **Acknowledge and continue review** | The reviewer has read the packet and the review continues under their ownership. **Not an approval to act.** | optional |
| **Return for correction** | Goes back to the submitter. | **mandatory** |
| **Escalate** | Raised to someone else. | **mandatory** |

`Record Reviewer Decision` throws if comments are empty on the latter two. A return or an escalation
with no stated reason is not an audit trail.

## 5. What it records

```
approval_id · gate_version
workflow_name · submission_id · review_type
system_status · system_confidence · counts · packet_fingerprint_fnv1a
reviewer_name · reviewer_role · reviewer_identity_assurance
decision · comments · gate_opened_at · decided_at
```

`reviewer_role` is mandatory — it is the competence evidence for the review type, and on a DG
document "who signed off" is inseparable from "were they qualified to."

`packet_fingerprint_fnv1a` binds the decision to the packet actually shown, so a later edit to the
review is detectable against the record. It is a **change-detection aid, not a cryptographic seal** —
FNV-1a is not collision-resistant and is not being claimed as such. The authoritative integrity
control is the append-only audit store (`02-hardening-report.md` F-U4).

## 6. The no-op boundary

`Enforce No-Op Boundary` stamps these into every record, on every branch, for every decision:

```
authorizes_operational_action: false     next_step_owner: "human"
certifies: false      clears: false      signs: false
tenders: false        sends_to_client: false
releases_shipment: false                 dispatches_work: false
makes_financial_commitment: false
```

Then it **iterates the flags and throws if any is not `false`.** The property is asserted in code
rather than left as a comment, so a future edit that tries to make the gate permissive fails loudly
instead of silently shipping.

**Acknowledging is not authorising.** A reviewer choosing *Acknowledge and continue review* has
confirmed they read the packet. The calling workflow may then commit a redacted record — and still
may not certify, tender, send, or dispatch. The full prohibited-actions policy is
`02-hardening-report.md` §7; this node is the mechanism that enforces it.

---

## 7. Node map

```
[Gate Input (Execute Workflow Trigger)]   9 required inputs
        ↓
[Validate Gate Input]                     throws on incomplete or clearance-shaped input
        ↓
[Build Review Packet]                     human-readable packet + fingerprint + approval_id
        ↓
[Wait for Reviewer Decision]  ◀── form ── a person, no time limit
        ↓
[Record Reviewer Decision]                identity, role, decision, comments, timestamps
        ↓
[Enforce No-Op Boundary]                  stamps and asserts every boundary flag false
        ↓
[Branch on Decision] ─┬─ Acknowledged
                      ├─ Returned for correction
                      ├─ Escalated
                      └─ Unrecognised → treated as Escalate
```

The fallback branch routes to **Escalate**, not to Acknowledge. Anything the gate cannot classify is
an exception, never a pass.

---

## 8. Reuse

The gate is review-type agnostic — it validates shape, not domain. Callers pass their envelope and
branch on `gate_result.decision`.

| Caller | `review_type` | Notes |
|---|---|---|
| Class 3 / 8 / 9 document review | `dg_document_review` | Node [10] in the hardened node map (`02` §2) |
| Physical AI — Shipment Capture | `physical_shipment_capture` | `02` §3 F-P3 |
| Multifamily maintenance alerts (future) | `building_maintenance_alert` | `06-rnd-multifamily-sandbox-concept.md` |

To call it: **Execute Sub-workflow** node → select this workflow → map the nine inputs → branch on
the returned `gate_result`.

---

## 9. Known residual risks

Stated plainly because they are real, and because a gate whose weaknesses are undocumented is worse
than no gate — it manufactures confidence.

**R-1 — Reviewer identity is self-declared, not proven.** The n8n form is unauthenticated by
default. Anyone with the resume URL can type any name. The record marks this honestly as
`reviewer_identity_assurance: "self_declared"`.

*Before this gate carries real reviews:* front the form with SSO or proxy authentication, or replace
the Wait node with an authenticated `sendAndWait` channel where the responder is identified by the
platform. Then set the field to `"authenticated"`. **Until that is done, this gate evidences that
*a* decision was recorded, not *who* made it.**

**R-2 — The resume URL is a bearer token.** Whoever holds it can submit the decision. Treat it as a
secret; do not forward it.

**R-3 — No wait limit is set, deliberately.** A timeout that resumes the workflow would silently
convert reviewer *silence* into reviewer *approval* — the exact failure this gate exists to prevent.
The trade-off is that unanswered executions accumulate. If you add a wait limit, the expiry branch
must route to **Escalate**. Never to Acknowledge.

**R-4 — FNV-1a is not cryptographic.** See §5.

**R-5 — The gate cannot police what the caller does with the result.** It returns a record with
`authorizes_operational_action: false`. A calling workflow that ignores that and acts anyway is
outside this gate's control. That is why `02-hardening-report.md` F-9 puts a separate assertion node
in the caller, immediately before any output action.

---

## 10. Verification performed

- All four Code node bodies pass `node --check`.
- All connection endpoints resolve to declared nodes.
- No credential object, API key, or token anywhere in the file.
- `"active": false`.

**Not** verified: behaviour inside a live n8n instance. This session had no n8n access. Import it
into a scratch workflow, run it once with dummy inputs, and confirm the form renders before wiring
it to anything real. n8n parameter names shift between versions — if a node shows red on import,
open it and re-pick the affected field, per the note already in `market-watch/n8n-analysis-prompt.md`.
