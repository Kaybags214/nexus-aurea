# 02 — NSF Project Pitch: Draft

**Status: DRAFT. Not submitted.** Placeholders in `<angle brackets>` need real values before this
goes anywhere.

Structure and character limits are from secondary sources — NSF's own site is unreachable from this
environment. **Confirm the prompts and limits in the live Project Pitch form before submitting**;
they are reported as four sections at 3500 / 3500 / 1750 / 1750 characters.

**Before submitting, read `01-technical-risk-register.md`.** Pitches are reported to be capped at two
per company per 12 months and three per technology. A pitch submitted before the risk framing is
sharp is not cheap feedback — it spends half the annual allowance.

| Section | Limit | Draft | Headroom |
|---|---|---|---|
| Technology Innovation | 3500 | 2591 | 909 |
| Technical Objectives and Challenges | 3500 | 3042 | 458 |
| Market Opportunity | 1750 | 1663 | 87 |
| Company and Team | 1750 | 1494 | 256 |

Counts are whitespace-normalised. Headroom in *Company and Team* is deliberate — the placeholders
there expand when filled.

---

## 1. Technology Innovation

Dangerous-goods and pharmaceutical air freight is governed by documents that must agree with each
other and with the physical package. A Shipper's Declaration, air waybill, packing list and the
marks on the carton must be mutually consistent; where they conflict, the package governs. Today
that reconciliation is done by eye, by a certified person, under time pressure at acceptance. Errors
are common and consequential: a wrong UN number, a packing group on an entry that takes none, an
absent gross weight, an illegible aircraft-limitation deletion. Each can produce a rejected
shipment, a delayed pharmaceutical consignment, or an unsafe tender.

Commercial vision models can now read these documents. That is not the innovation, and it is not
sufficient. A model that reads a declaration confidently and wrongly is more dangerous than no model
at all, because it produces an authoritative-looking record of a check that did not really happen.

Our innovation is a system built around the opposite property: one that establishes, measurably,
when it cannot determine an answer, and abstains in a way a certified reviewer can act on. In our
existing prototype the system already declines rather than guesses -- reporting that a field is
illegible, that a value is absent rather than unreadable, and that a gross weight cannot be derived
and that litre quantities must not be converted to kilograms. It localises its own uncertainty to a
region of the page.

We propose to turn that behaviour from an emergent property into a measured, calibrated capability,
and to bind it to physical evidence. The system captures the package by camera alongside the
paperwork, reconciles the two, and emits a structured record in which every assertion carries an
evidence locator -- a specific region of a specific hashed image -- plus a per-field confidence and
an explicit statement of what could not be established. A computed status, derived from countable
facts rather than model self-assessment, routes the submission to a human approval gate that records
reviewer identity, decision and rationale, and which is architecturally incapable of certifying,
clearing, signing or tendering anything.

The result is not an automated compliance decision. It is an auditable evidence package that makes a
human decision faster and better-supported, and that leaves a defensible record of what was checked,
what was uncertain, and who decided. The technical contribution is calibrated selective prediction
plus verifiable cross-modal evidence binding in a domain where being confidently wrong is a safety
event.

---

## 2. Technical Objectives and Challenges

The core research question: can a vision-language system's uncertainty on regulated shipping
documents be calibrated well enough that a threshold-based abstention policy is safe, and can its
assertions be bound to physical evidence tightly enough to stand as a compliance record?

Objective 1 -- Calibration on regulated documents. It is unknown whether stated confidence predicts
correctness on this document class. These documents are the distribution shift that published
calibration results do not cover: carrier-specific layouts, handwriting, decimal commas, overlapping
strike-marks, phone photographs at angle, fax artifacts. We will assemble a ground-truth-labelled
corpus of redacted and purpose-authored declarations with known injected defects, and measure
reliability and expected calibration error per field type, including degradation under controlled
image-quality variation. Challenge: corpus construction requires certified labelling and lawful
sourcing. Managed by authoring documents with injected defects drawn from a taxonomy derived from
real observed errors, supplemented by consenting-partner documents under redaction.

Objective 2 -- Cross-modal evidence binding. Reconciling package against paperwork is the
differentiator and is not solved by general-purpose vision APIs. The deliverable is the linkage: each
finding cites a region of a hashed image so a reviewer can verify the reasoning rather than trust it.
We will measure detection rate per discrepancy class and, critically, evidence-locator precision --
whether the cited region actually contains the cited evidence. Challenge: locator precision may be
insufficient for a reviewer to skip re-examination, collapsing the value. Managed by scoping to a
small number of high-consequence discrepancy classes and measuring precision before expanding.

Objective 3 -- Cost-asymmetric abstention policy. A missed defect is a safety and regulatory event; a
false alarm is reviewer time. These differ by orders of magnitude, and the ratio varies by field: a
wrong UN number is not a misspelling in the handling block. Symmetric metrics such as accuracy and F1
are the wrong instruments. We will build a per-field cost model with certified DG staff and optimise
thresholds against it. Challenge: no threshold may achieve an acceptable miss rate at a workable
review volume -- a negative result that would itself be a significant finding for the field.

Objective 4 -- Reproducibility. A compliance record implies that the same input yields the same
record. Sampling models do not guarantee this, and our own prototype has produced differing output
shapes across runs. We will measure run-to-run variance on identical inputs and define an achievable
reproducibility standard -- finding-set stability versus byte-identity -- with evidence bound to
document hashes and image regions rather than to phrasing.

Risk we are explicitly not claiming: OCR, workflow orchestration, interface construction and file
storage are solved engineering and are not research objectives here.

---

## 3. Market Opportunity

Customers are the parties accountable when a dangerous-goods or pharmaceutical shipment is tendered
incorrectly: freight forwarders and consolidators, cargo-handling agents at acceptance, and shippers
of temperature-controlled pharmaceuticals. The buyer is typically the compliance or quality function,
which carries the regulatory exposure and today staffs it with scarce certified people performing
manual cross-checks under time pressure.

The value is not headcount replacement. Certified human sign-off is required and will remain
required; a vendor claiming to remove it misunderstands the regulation. The value is that the human
decision arrives faster and better-evidenced, and that the resulting record is defensible when an
auditor, a carrier or an insurer asks what was checked and by whom.

Competitive landscape: document-extraction and IDP vendors read forms accurately but produce no
calibrated uncertainty, no physical-package reconciliation, and no auditable abstention -- they tell
you what a field says, not whether they should be believed. Forwarder TMS platforms manage the
transaction, not document correctness. Compliance-content providers publish the rules but do not
inspect shipments. None currently sells a system whose central claim is knowing when it cannot
determine an answer.

Adoption constraint, stated plainly: this domain will not accept an opaque automated decision, which
is why the human-approval architecture and the evidence record are the product rather than an
add-on. The customer-discovery programme running alongside Phase I is designed to test the pricing
and workflow-fit assumptions above rather than to confirm them.

---

## 4. Company and Team

Nexus Aurea Inc. is a <state> corporation founded in <year>, based in <city, state>, focused on
compliance infrastructure for regulated logistics.

Principal Investigator: Kenya Bagwell, <title>. IATA DGR certified, with <N> years of hands-on
dangerous-goods and pharmaceutical air-freight experience spanning shipper's declarations, air
waybills, cold-chain documentation and GDP/GMP handling. This competence is central, not incidental:
the research questions turn on defining what "correct" means on a declaration and on building a
per-field cost model for regulatory error -- neither specifiable by a team without certified DG
expertise. <Add education, prior roles, and any publications, patents or prior federal awards.>

Technical foundation built by the company before this proposal: a document-review engine
demonstrating per-field read confidence and explicit abstention on live shipping documents; a
schema-enforced output contract; a human approval gate architecturally incapable of certifying,
clearing or tendering; and a written order of precedence across IATA DGR, ICAO TI, 49 CFR and
destination customs law.

<Gaps to close before submission, named where possible:> a collaborator with demonstrated background
in model calibration or uncertainty quantification, as senior personnel or consultant; and certified
DG reviewers beyond the PI for labelling and human-factors measurement.

<Name any letter of support secured from a forwarder, handling agent or pharmaceutical shipper.>

---

## Notes on the draft

**What it leads with.** Section 1 concedes immediately that commercial vision models can read these
documents, then argues that reading them is not the problem. Getting ahead of the reviewer's first
objection is stronger than letting them raise it — and it is true, which matters more.

**What it stakes the claim on.** Calibrated selective prediction plus cross-modal evidence binding:
R1 and R3 from the risk register. R2 and R4 appear as secondary objectives. R5 is held back — five
objectives in one Phase I reads as unfocused.

**Where it names negative results.** Objective 3 says plainly that no workable threshold may exist.
Reviewers respond well to a plan that can fail informatively; a project that cannot produce a
negative result is not research.

**What it declines to claim.** Section 2 closes by naming OCR, orchestration, UI and storage as
solved engineering rather than research. Volunteering that is a credibility move — a reviewer who
notices it unacknowledged concludes the applicant cannot tell the difference.

**Why the market section refuses the obvious pitch.** It states that certified human sign-off is
required and will remain required. "Replaces your compliance staff" is both wrong on the regulation
and the fastest way to lose a reviewer who knows the domain.

## Before submitting — fill these in

1. Every `<placeholder>` in Section 4.
2. **The calibration collaborator.** The weakest point in this pitch is that its primary technical
   objective is calibration and uncertainty quantification, while the named team's demonstrated
   depth is regulatory. Naming a real collaborator materially strengthens it. Address the gap rather
   than hoping it goes unnoticed.
3. **Corpus status.** "We have assembled N documents across M defect classes, taxonomy attached"
   beats "we will assemble a corpus." See `01` §6 — start now.
4. **A letter of support**, if one can be secured from a forwarder, handling agent, or pharmaceutical
   shipper. Falls out of customer discovery (`04`).
5. **Verify eligibility and registrations** — `05`. Confirm before spending effort on the writing.
