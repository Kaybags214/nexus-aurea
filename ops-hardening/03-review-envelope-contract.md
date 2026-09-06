# 03 — Review Envelope Contract

The single structured output every Nexus Aurea review workflow emits, and the only thing the
Human Approval & Exception Gate accepts.

**Schema:** `schemas/review-envelope.schema.json` (JSON Schema draft 2020-12)
**Version:** 1.0.0 — draft, not yet applied to any live workflow.

---

## 1. Why this exists

Today's Class 3/8/9 output is prose. It carries good analysis (see `00-inspection-report.md` §3.1)
but nothing downstream can read it: no status token, no confidence value, no way to branch, no way
to gate. Every other control in `02-hardening-report.md` depends on this contract existing first.

The prose does not go away. It is **rendered from** the envelope rather than being the source of
truth — so the human-readable record and the machine-readable record cannot disagree, which is
exactly the drift observed in finding C-8.

---

## 2. Required fields

Nine fields are mandatory. The gate hard-fails if any is absent — including the array fields, which
must be sent as `[]` rather than omitted. "Absent" and "none" are different claims and the system
must never conflate them.

| Field | Type | Notes |
|---|---|---|
| `workflow_name` | string | Which workflow produced this. |
| `submission_id` | string | UUID assigned at intake, before any processing. |
| `review_type` | enum | `dg_document_review` · `physical_shipment_capture` · `building_maintenance_alert` |
| `system_status` | enum | See §3. Computed, never model-generated. |
| `confidence` | number 0–1 | System confidence in the review as a whole. |
| `discrepancies` | array | What was found. `[]` if none. |
| `missing_information` | array | What could not be established. `[]` if none. |
| `evidence` | array | Where each finding came from. `[]` if none. |
| `recommended_human_action` | object | What a person should do next. |

## 3. Status vocabulary

```
REJECT_INTAKE                          nothing was reviewed — payload invalid, unreadable,
                                       oversized, or the wrong type
HOLD                                   a blocking problem was found — critical discrepancy,
                                       blocking missing information, or class-scope mismatch
HUMAN_REVIEW_REQUIRED                  uncertain — low confidence, low legibility, or findings
                                       without evidence
REVIEW_COMPLETE_NO_DISCREPANCIES_FOUND nothing found by a draft reading aid, on the documents
                                       supplied. Still requires a human. Not a clearance.
```

**There is no `PASS`.** `AUDIT-ENGINE-PROMPT.md` §6 currently offers one; `02-hardening-report.md`
F-6 removes it. On a dangerous-goods document "PASS" reads as a clearance, and this system must
never issue one. The longest status name in the list is the clean one, deliberately — it states its
own limits.

**Status is computed by the decision-policy node (F-6), never emitted by the model.** Asking a model
whether its own output can be trusted is not a control.

## 4. Field detail

**`discrepancies[]`** — `id`, `severity` (`critical`/`major`/`minor`), `field`, `observed`,
`expected`, `standard`, `precedence_level`, `confidence` (`high`/`medium`/`low`).

`standard` is mandatory and carries the repo's existing rule: *a flag without a named standard is
not a finding* (`AUDIT-ENGINE-PROMPT.md`, Standing rules). `precedence_level` records which level of
`standards-of-precedence.md` the flag came from, so the strictest-governs rule stays auditable.

**`missing_information[]`** — `id`, `item`, `why_it_matters`, `blocking` (boolean).
`blocking: true` forces `HOLD`. This is where "AWB number is blank" and "no gross weight field on
this form" belong — the current engine handles these well in prose; this gives them structure.

**`evidence[]`** — `discrepancy_id`, `document_sha256`, `locator`, `quote`, `legibility`
(`high`/`medium`/`low`).

`locator` is a position, not content: `"page 1, quantity column, line 1"`. This is what makes the
redaction split (F-7) workable — a locator plus a legibility rating is fully reviewable without
reproducing the shipper's address. **`quote` is the only field here that may contain document text,
and it is never included in the public record.**

`legibility: low` forces `HUMAN_REVIEW_REQUIRED`. It maps directly to what the engine already
produces well: *"strike-through marks are partially overlapping/illegible"*.

**`recommended_human_action`** — `summary`, `steps[]`, `required_qualification`, `do_not[]`.

`do_not[]` is not decoration. The current Class 3 artifact carries
*"Do not infer or convert any unit — the L values must not be converted to kg"* — a real safety
instruction that today lives in prose where nothing can enforce or display it reliably. Structured,
the gate renders it to the reviewer every time.

**`observed_scope` / `declared_scope`** — optional at the schema level, **required for
`dg_document_review`**. `declared_scope.class` is the queue the submission entered; `observed_scope`
is what the model actually read. The class-scope gate (F-5) compares them. This is the fix for
finding C-2 — the Class 3 run that reviewed a document carrying no Class 3 goods.

**`automation_boundary`** — all-false constants stamped into every envelope:
`certifies`, `clears`, `tenders`, `sends_to_client`, `signs`. Redundant with the gate's own
assertion, and that is the point: the property is stated at both ends of the pipe and asserted in
code at the gate.

## 5. What must never appear

- API keys, tokens, credentials.
- Full document images or binary payloads.
- Extracted personal or commercial field values **in the public record** — names, addresses, phone
  numbers, signatures. These live only in the working copy (F-7), never in git.
- Any word implying clearance: `PASS`, `CLEARED`, `APPROVED`, `CERTIFIED`, `TENDERED`.

## 6. Validation

- The AI node's Structured Output Parser is bound to the schema. **A parse failure is a stop**, never
  a fallback to prose.
- The gate re-validates on receipt and throws on any violation — it does not trust its caller.
- The pre-commit assertion node (F-9) validates once more before anything reaches git.

Three checks on the same contract is deliberate. Each is a different trust boundary: model→workflow,
workflow→gate, workflow→git.

## 7. Worked example

`schemas/example-envelope-class3-holdaction.json` is the real 2026-09-05 Class 3 case expressed as
an envelope: the class-scope mismatch as a critical discrepancy, the blank AWB and absent gross
weight as blocking missing information, the illegible strike-marks as low-legibility evidence, and
the resulting `HOLD`. Field values are placeholdered — it demonstrates the shape, not the shipment.
