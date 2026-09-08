# 03 — Prototype Spec: Physical Shipment Evidence Capture

**Scope: 30–60 days, before submission.** Not the Phase I project — the thing that makes the pitch
credible and produces the first real data for `01`.

**Simulated and self-authored inputs only. No client documents, no client shipments.**

---

## 1. What it must prove

Not that a model can read a document — that is assumed. Three things a reviewer will want evidence
for:

1. **The abstention behaviour is real and measurable**, not an anecdote from four artifacts.
2. **Cross-modal binding is achievable** — a finding can cite a region of a package photograph and
   be checked against the paperwork.
3. **The team can run a measurement**, not just build a workflow. This is the one that separates a
   research proposal from a product demo.

A working demo alone does not do this. **The deliverable is a measurement, and the demo is how the
measurement is produced.**

## 2. Scope

**In:**
- A staged corpus: self-authored declarations plus photographed packages, with deliberately injected
  defects and therefore known ground truth.
- Capture of package image + document image as one submission.
- Extraction into the review envelope (`../ops-hardening/schemas/review-envelope.schema.json`).
- Per-field confidence and explicit abstention.
- Evidence locators bound to image regions and document hashes.
- Computed status via the fail-closed policy (`../ops-hardening/02-hardening-report.md` F-6).
- The human approval gate (`../ops-hardening/04-approval-gate/`).
- **A measurement harness** — the actual deliverable.

**Out:** real client documents or shipments; production deployment; mobile app work; any
integration with a live carrier, TMS or WMS; real sensors beyond a phone camera; anything from
Track 2 or Track 3.

## 3. The staged corpus

Roughly 60–100 submissions is enough for a defensible preliminary result at this stage. Each is a
package photograph plus its paperwork, authored so ground truth is known by construction.

Defect taxonomy — derived from real observed errors, not invented. The 2026-09-05 `dg-reviews/`
artifacts already supply most of these:

| Class | Example | Ground truth |
|---|---|---|
| **UN / PSN mismatch** | UN number paired with the wrong proper shipping name | Injected, known |
| **Packing group error** | PG entered on an entry that takes none | Injected, known |
| **Absent required field** | AWB number blank; no gross weight field completed | Injected, known |
| **Package/paper contradiction** | Photo shows 3 cartons, packing list says 4; label class ≠ declared class | Injected, known |
| **Legibility defect** | Overlapping strike-marks on the aircraft-limitation box | Injected, graded |
| **Unit / format trap** | `0,5 L` decimal comma; litres where kg is expected | Injected, known |
| **Clean control** | No defect | Known clean |

Include clean controls at roughly 25–30%. Without them the false-positive rate cannot be measured,
and false-positive rate is what R5 turns on.

Vary image quality deliberately — angle, lighting, focus, resolution — and record the variation as a
covariate. Degradation under image quality *is* R1's second measurement, not a nuisance.

## 4. Measurements

This is the part that distinguishes the prototype from a demo. Instrument from the first run.

| Measurement | Method | Feeds |
|---|---|---|
| **Detection rate per defect class** | Injected defects found / injected | R3 |
| **False-positive rate** | Findings asserted on clean controls | R2, R5 |
| **Calibration** | Reliability curve of stated confidence vs. correctness, per field type | **R1** |
| **Abstention correctness** | When it says "cannot verify" — could a human verify it? Separates honest abstention from failure to try | **R1, R2** |
| **Locator precision** | Does the cited region actually contain the cited evidence? Manual check | **R3** |
| **Run-to-run variance** | Same input ×5; compare finding sets and status | **R4** |
| **Latency and cost** | Per submission | Feasibility |

**Abstention correctness is the most important and least obvious.** A system that abstains on
everything is perfectly calibrated and useless. The measurement that matters is whether abstention
tracks genuine unreadability — and it requires a human to independently attempt each abstained
field.

## 5. Build order

| | Work | Why this order |
|---|---|---|
| **1** | Corpus + defect taxonomy + labelling scheme | Gates everything. Longest lead time (`01` §6) |
| **2** | Capture path: package + document → envelope | Reuses the hardened node map |
| **3** | Measurement harness | **Before** tuning anything — otherwise you tune against intuition |
| **4** | Baseline run, untuned | The honest starting number. Record it |
| **5** | Locator binding for 2–3 defect classes | R3, scoped small |
| **6** | Variance run | R4. Cheap, and nobody has this number |
| **7** | Threshold exploration against a per-field cost model | R2, only once R1 has data |

Steps 3 and 4 before any tuning. A baseline you cannot reproduce is not a baseline, and "it got
better" without a recorded starting point is not a result.

## 6. Reuse — build almost nothing new

Deliberately thin. Nearly all of it exists:

| Component | Source |
|---|---|
| Output contract + schema | `../ops-hardening/schemas/` |
| Approval gate | `../ops-hardening/04-approval-gate/` |
| Node topology, failure policy | `../ops-hardening/02-hardening-report.md` §2 |
| Decision policy, class-scope gate | F-5, F-6 |
| Redaction split | F-7 |
| Domain standards | `../compliance-auditor/standards-of-precedence.md` |

**New:** the staged corpus, the package-capture path, the locator binding, and the measurement
harness. That is the whole build.

## 7. What it produces for the pitch

- A defect taxonomy grounded in real observed errors.
- A labelled corpus with known ground truth.
- Baseline detection, false-positive, and calibration numbers.
- A preliminary reliability curve — the single most persuasive artifact available for R1.
- A run-to-run variance figure for R4.
- Evidence that the team measures rather than asserts.

**Even a bad result is usable.** "Confidence is uncorrelated with correctness at baseline" is a
strong motivating finding for a proposal whose primary objective is fixing exactly that. What is not
usable is having no numbers at all.

## 8. Constraints

- Self-authored and simulated inputs only. No client documents.
- Any real document used in corpus construction requires consent and redaction
  (`../ops-hardening/07-client-document-custody.md` §5) — and redaction must not destroy the defect
  under study.
- The prototype certifies, clears, tenders and sends nothing
  (`../ops-hardening/02-hardening-report.md` §7).
- `environment: "sandbox"` on every record.
- Nothing from Track 2 or Track 3 enters this build.
