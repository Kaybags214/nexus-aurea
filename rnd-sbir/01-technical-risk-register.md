# 01 — Technical Risk Register

**The document everything else depends on. Read it before drafting anything.**

---

## 1. The problem to solve before submitting

NSF SBIR funds **technical risk reduction**. The first question a reviewer asks is not "is this
useful?" — it is "what is technically unproven here, and would this project settle it?"

Held to that standard, here is the honest position:

> **What exists today is an integration, not a research result.** A vision model is called from an
> n8n workflow, its prose output is committed to git. Every component is off the shelf. A reviewer
> who reads only that will ask why a commercial vision API plus a form does not already solve it —
> and on that description, it does.

This is not a reason to abandon the pitch. It is the specific weakness the pitch must answer, and it
is answerable — because the interesting thing in the existing system is not the extraction. **It is
the abstention.**

## 2. Where the actual research is

The 2026-09-05 artifacts contain behaviour that is genuinely research-shaped, and it was probably
not recognised as such when it was built:

- `"cannot verify from image"` — the system **declines to answer** rather than guessing.
- `"Gross weight: no labeled gross-weight field on this form; cannot be derived, and volumes in L
  must not be converted to kg"` — it distinguishes *absent* from *unreadable* from *not derivable*.
- Per-field read confidence — `High (that it is blank)` separates confidence in the reading from
  confidence in the value.
- `"strike-through marks are partially overlapping/illegible"` — it localises its own uncertainty to
  a region of the page.

That is **selective prediction on a safety-critical task**: a system that knows when it does not
know, and says so in a form a human can act on.

**The reframe:**

> Detecting documentation exceptions is the easy part. Knowing, reliably and measurably, when the
> system *cannot* detect them — and proving that the resulting record is trustworthy enough to
> stand as a compliance artifact — is the research.

That framing is defensible, it is not solved by calling an API, and it is grounded in something
already demonstrated rather than aspirational.

---

## 3. The risk register

Five risks. Each states what is unproven, why it is hard, what would settle it, and what a negative
result looks like — because a risk that cannot fail is not a risk, and reviewers know it.

### R1 — Confidence calibration on regulated documents
**Unproven:** whether stated confidence predicts correctness. The system says `High` and `Low`. **No
one has ever checked whether `High` is actually right more often than `Low` on this document class.**

**Why it is hard:** vision-language models are known to be poorly calibrated and to shift under
distribution change. Shipping documents *are* the distribution shift — carrier-specific forms,
handwriting, decimal commas (`0,5 L` appears in the Class 8 artifact), overlapping strike-marks,
phone photographs at angle, fax-generation artifacts. Published calibration results on clean
benchmarks do not transfer, and nobody has published on this document class.

**Settled by:** a ground-truth-labelled corpus of redacted DG documents; reliability diagrams and
expected calibration error per field type; measured degradation under controlled image quality.

**Negative result:** confidence is uncorrelated with correctness and cannot be calibrated per field
type. That would be a genuine finding — it would mean any threshold-based gating in this domain is
unsound, which the industry does not currently know.

### R2 — Cost-asymmetric abstention policy
**Unproven:** where the abstention threshold belongs when the two error types are not comparable.

**Why it is hard:** a false negative is a mis-tendered hazmat shipment — a safety and regulatory
event. A false positive is reviewer time. These differ by orders of magnitude and cannot be traded
off with a symmetric metric. Accuracy and F1 are the wrong instruments. **The cost ratio is also not
constant** — it varies by field. Getting a UN number wrong is not the same class of error as missing
a misspelling in the handling block, and a single global threshold cannot express that.

**Settled by:** a per-field cost model built with certified DG staff; threshold optimisation against
it; measured operating points on held-out documents.

**Negative result:** no threshold achieves an acceptable false-negative rate at a workable review
volume — meaning full human review remains necessary and the system's value is triage speed, not
review reduction. Worth knowing before anyone sells it as the latter.

### R3 — Cross-modal evidence binding (package versus paper)
**Unproven:** whether physical evidence can be reconciled against document assertions with an
evidence chain strong enough to stand in a compliance record.

**Why it is hard, and why it is the differentiator:** the operating rule is already written down —
*"reality beats paper"* (`../compliance-auditor/standards-of-precedence.md` §4). Automating it means
comparing what a camera sees on the package (marks, labels, hazard diamonds, piece count, orientation
arrows) against what the declaration asserts, and **binding each comparison to a specific region of
a specific image** so a human can verify the machine's reasoning rather than trust it.

This is not OCR. It is grounded multi-document, multi-modal reconciliation where the *linkage* is
the deliverable. It is also the part no general-purpose vision API does, which is what makes it the
technical core rather than the application layer.

**Settled by:** staged package/document pairs with known injected discrepancies; measured detection
rate per discrepancy class; measured evidence-locator precision — does the cited region actually
contain the cited evidence?

**Negative result:** locators are unreliable enough that a human must re-examine the whole document
anyway, collapsing the value proposition.

### R4 — Auditability of a non-deterministic system
**Unproven:** whether a stochastic model can produce a record a regulator or auditor would accept.

**Why it is hard:** a compliance record implies reproducibility. Run the same document twice and a
sampling model may return different prose, different confidence, possibly different findings. The
2026-09-05 artifacts show exactly this — two runs, two schema shapes, two header formats
(`../ops-hardening/00-inspection-report.md` D6). An audit trail whose contents depend on when it was
generated is a weak audit trail, and "the AI said so" is not a defensible provenance claim.

**Settled by:** measured run-to-run variance on identical inputs; a defined reproducibility standard
(is finding-set stability enough, or is byte-identity required?); an evidence-binding scheme where
each finding is traceable to a document hash and image region regardless of phrasing.

**Negative result:** variance is high enough that only human-confirmed findings can enter the
record — which sharply narrows the automation claim, and is exactly the kind of thing that should be
discovered in Phase I rather than after deployment.

### R5 — Does the human gate survive contact with volume?
**Unproven:** whether human-in-the-loop review remains a real control at operational alert rates.

**Why it is hard:** the gate is only a control while the reviewer actually reads the packet. Under
enough low-value alerts it degrades into clicking through — and **a rubber-stamped gate is worse
than no gate, because it manufactures an audit trail asserting review that did not meaningfully
happen.** The system's own artifacts already show the failure mode in miniature: the Class 3
mis-routing appeared as *item 10 of 11* in a prose list and was not acted on. Correct information,
badly presented, ignored.

**Settled by:** measured false-positive rates per severity; timed review sessions with certified
staff; measured detection of injected discrepancies as alert volume rises; packet presentation
compared across formats.

**Negative result:** review quality degrades measurably above some alert rate — which sets a hard
design constraint on any deployment and is a publishable human-factors finding in its own right.

---

## 4. What is explicitly not a research risk

State this in the proposal. Volunteering it builds credibility, and a reviewer who spots it
unacknowledged concludes the applicant does not know the difference.

| Not research | Why |
|---|---|
| OCR / text extraction from documents | Solved. Commercial APIs do this |
| Workflow orchestration, webhooks, queues | Engineering |
| Building a review UI | Engineering |
| Storing files, hashing, audit logging | Engineering |
| Prompting a vision model to describe an image | Solved |
| The regulatory knowledge itself | Domain expertise the team has — an input, not a finding |

The research is R1–R5: **calibration, cost-asymmetric abstention, evidence binding, reproducibility,
and whether the human control holds.**

---

## 5. Ranking

| | Risk | Centrality | Tractable in Phase I | Phase I priority |
|---|---|---|---|---|
| **R1** | Calibration | High — everything downstream branches on confidence | Yes, with a labelled corpus | **Primary** |
| **R3** | Cross-modal evidence binding | High — the differentiator | Partially; scope to a few discrepancy classes | **Primary** |
| **R2** | Abstention policy | High | Yes, once R1 has data | Secondary, follows R1 |
| **R4** | Reproducibility | Medium-high | Yes — cheap to measure, and nobody has | Secondary |
| **R5** | Human gate under load | Medium | Partially — needs real reviewers | Stretch; design the instrument now |

**A Phase I built on R1 + R3, with R2 and R4 as secondary objectives, is a coherent proposal.** All
five is too many for six to eighteen months and will read as unfocused — the same failure the track
separation exists to avoid.

---

## 6. The corpus problem — the real schedule risk

R1, R2 and R3 all require **labelled documents with known ground truth**. Not simulated. Not
generated. Real forms with real defects, correctly labelled by someone qualified.

This is the hardest logistical constraint in the plan, and it is not a technical one:

- Real client documents cannot be used without consent and a lawful basis
  (`../ops-hardening/07-client-document-custody.md` §5).
- Redaction must not destroy the defects under study — redacting an address is fine, redacting the
  quantity column is not.
- Labelling requires certified DG competence. That is the PI, or paid consultants.

**Three viable sources:**

1. **Self-authored documents with deliberately injected defects.** Fully controlled, no consent
   problem, ground truth known by construction. Weakness: injected defects may not resemble real
   ones. Mitigate by deriving the defect taxonomy from real observed errors — the existing
   `dg-reviews/` artifacts are already a start.
2. **Historical documents from consenting industry partners, redacted.** Realistic. Slow. Requires
   agreements. **Start these conversations during customer discovery** (`04`) — the interviews and
   the corpus recruitment are the same conversations.
3. **Training and sample documents** from carriers and training providers, where licensing permits.

**Begin corpus construction in the next 30 days, in parallel with everything else.** It gates three
of five risks, and no amount of good writing shortens it. A proposal that says "we will assemble a
corpus" is weaker than one that says "we have assembled 200 documents across 6 defect classes and
here is the taxonomy."
