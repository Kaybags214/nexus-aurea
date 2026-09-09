# Audit Findings — 49 CFR Compliance Reference Library v1.0

**Document under review:** `dgr/02-49cfr/nexus-aurea-cfr-library-v1.0.md` (v1.0, built 2026-09-09)
**Companion report:** `cfr-library-json-vs-md-delta.md` — the JSON artifact is not a
serialization of this Markdown; the two diverge, including in their standing rules.
**Review date:** 2026-09-09
**Status of this report:** DRAFT — human review required before any action is taken.
**Disposition of v1.0:** NOT RELEASED FOR AUDIT USE pending remediation of F-01 through F-08.

---

## ⚠️ VERIFICATION LIMITATION — READ FIRST

Primary-source verification could **not** be performed in this session. Outbound access to
`ecfr.gov`, `govinfo.gov`, and `law.cornell.edu` is blocked by network egress policy. No
citation in v1.0 has been confirmed against the current CFR text.

Per the library's own **Standing Rule 5** ("Never invent a missing regulation"), every finding
below that depends on the exact wording or paragraph designation of a section is marked
**❓ Unable to Verify** regardless of reviewer confidence. Findings marked **❌ Fail** are those
provable from the document's own contents (internal inconsistency, absent coverage,
self-contradiction) and require no external source.

**Every ❓ item must be checked against eCFR before v1.0 is released.**

---

## FINDINGS SUMMARY

| ID | Finding | Status | Risk |
|---|---|---|---|
| F-01 | §175.10 mis-cited as authority for cargo dry ice declarations | ❓ Unable to Verify | Critical |
| F-02 | §173.217 (dry ice) absent from library entirely | ❌ Fail | Critical |
| F-03 | Lithium batteries listed as in-scope but zero audit checks exist | ❌ Fail | Critical |
| F-04 | No temperature values anywhere in the library | ❌ Fail | Critical |
| F-05 | All dry ice checks are presence-only; no cross-document reconciliation | ❌ Fail | Critical |
| F-06 | Part 172 Subparts D/E/F/G/H absent — no marking, labeling, ER info, training | ❌ Fail | Critical |
| F-07 | Part 175 air coverage omits NOTOC (§175.33), acceptance (§175.30), loading (§175.75) | ❌ Fail | Critical |
| F-08 | Four of five pharma checks carry no regulatory citation — violates Standing Rule 4 | ❌ Fail | Critical |
| F-09 | Class 3 PG I criteria state a flash point threshold; §173.121 never cited | ❓ Unable to Verify | High |
| F-10 | §172.200 exception list omits the hazardous waste / hazardous substance carve-out | ❓ Unable to Verify | High |
| F-11 | §173.27 (general air packaging requirements) absent | ❌ Fail | High |
| F-12 | OECD 439 listed as an accepted corrosivity test method | ❓ Unable to Verify | High |
| F-13 | §172.202 quantity/package paragraph assignments unconfirmed | ❓ Unable to Verify | High |
| F-14 | "ERG number" used for the emergency response telephone number | ❌ Fail (Markdown only) | Medium |
| F-15 | Hazardous waste: EPA code cited to HMR; mandatory "Waste" prefix never checked | ❓ Unable to Verify | Medium |
| F-16 | Class 6.2 (UN3373) and Class 2.2 cryogenic absent from a pharma library | ❌ Fail | Medium |
| F-17 | No document control block — uncontrolled document generating audit findings | ❌ Fail | Medium |
| F-18 | PH-005 is an active check sourced to a document listed as PENDING | ❌ Fail | Medium |
| F-19 | Definitional imprecision — §173.120(a), §173.120(b)(2), §173.136(a), marine pollutant | ❓ Unable to Verify | Low |
| F-20 | Worked example at line 73 varies two attributes at once | ❌ Fail | Low |

---

## CRITICAL DISCREPANCIES

### F-01 — §175.10 mis-cited as the authority for cargo dry ice declarations
**Status:** ❓ Unable to Verify — direction of concern stated below
**Location:** Lines 228 (C9-002), 243 (PH-001), 261 (AIR-003)

49 CFR §175.10 is titled *"Exceptions for passengers, crewmembers, and air operators."* It
governs what an individual may carry aboard an aircraft in baggage. The library uses
`§175.10(a)(10)` as the cited source for **cargo** shipment declaration requirements in both
the Class 9 checklist (C9-002) and the Pharma checklist (PH-001).

A finding written against a commercial pharma air cargo shipment and cited to a
passenger-baggage exception is not defensible. If challenged by a carrier or an inspector, the
citation collapses and the finding is withdrawn.

Two separate defects are present:
- **Wrong section.** Cargo dry ice declaration and packaging authority is §173.217, plus
  §172.202/§172.203 for the shipping paper description, and IATA DGR PI 954 for air.
- **Paragraph designation unconfirmed.** `(a)(10)` is asserted three times. The paragraph
  numbering of §175.10(a) has moved across rulemakings and must be confirmed against the
  current text before use.

AIR-003 (the ≤2.5 kg per person limit) is a correct passenger rule but does not belong in a
cargo audit checklist — it occupies one of only three checks in the entire air transport
section (see F-07).

---

### F-02 — §173.217 is absent from the library entirely
**Status:** ❌ Fail (verified by search of the document)
**Location:** Document-wide

Dry ice is the single most frequently handled dangerous good in this operation. §173.217 is
the controlling packaging section for Carbon dioxide, solid. It appears **zero times** in the
library. Every dry ice check in v1.0 is sourced to §173.140 (the Class 9 definition) and
§175.10 (passenger exceptions).

The library can therefore assert that dry ice *is* Class 9, and nothing about how it must be
packaged, vented, marked, or quantity-limited.

---

### F-03 — Lithium batteries are listed as in-scope and never audited
**Status:** ❌ Fail
**Location:** Line 217 (listed); Class 9 checklist lines 226–231 (no checks)

UN3480 / UN3481 appear in the "Common Class 9 Materials" table. The Class 9 audit checklist
(C9-001 through C9-005) contains **no lithium battery check of any kind**. Absent from the
document: §173.185, state-of-charge limits for air, Section IA/IB/II distinctions, PI 965–970,
lithium battery mark, and the Class 9A label.

**This is the library's largest cold-chain exposure.** Every IoT-monitored pharma shipment
carries a data logger or real-time tracker containing lithium cells — typically UN3481
PI 967 Section II. A temperature-monitored shipment is, by construction, a lithium battery
shipment. v1.0 audits the temperature documentation and is blind to the battery in the same
carton. The repository already carries `dgr/04-lithium-batteries/` as a scope area.

---

### F-04 — The library contains no temperature values
**Status:** ❌ Fail (verified by search — one incidental line, no values)
**Location:** Part 6, lines 235–247; Part 8, lines 276–277

PH-002 asks whether "temperature control requirements" are "documented." PH-005 asks whether
the AWB carries a "temperature range." Neither check states any range against which the
document under review is to be judged.

Absent from the library: 2–8 °C, −20 °C, −70/−80 °C, controlled room temperature 15–25 °C,
dry ice sublimation temperature (−78.5 °C), and any definition of a temperature excursion or
mean kinetic temperature.

**Consequence:** the library can confirm that *a* temperature is written on a document. It
cannot detect that the temperature is the *wrong* one. A shipment labelled 2–8 °C packed on
dry ice — a product-destroying mismatch — passes PH-002 and PH-005 as written.

---

### F-05 — Dry ice checks test presence on a single document, never consistency across documents
**Status:** ❌ Fail
**Location:** C9-002 (line 228), PH-001 (line 243), Part 8 line 275

All three dry ice checks are constructed as presence tests: "net weight stated," "UN1845
declared," "packaging marking." Part 8 lists the AWB, the Shipper's Declaration, the packing
list, the commercial invoice and the dry ice declaration as separate documents to review, but
**no check requires the declared dry ice net weight to be identical across them.**

The real-world failure mode is not an absent weight — it is 15 kg on the AWB, 12 kg on the
Shipper's Declaration, and an unmarked outer package. Under v1.0 that shipment passes every
dry ice check. No unit of measure is mandated either, so "12" and "12 lb" both satisfy
"net weight stated."

---

### F-06 — Part 172 Subparts D, E, F, G and H are absent
**Status:** ❌ Fail (verified by search — zero occurrences of §172.301, §172.400, §172.500, §172.600, §172.602, §172.604, §172.700)
**Location:** Document-wide; Part 2 covers Subpart C only

The library covers shipping papers and nothing else in Part 172. Missing:

- **Subpart D (marking)** — UN number and PSN on the package, orientation arrows.
- **Subpart E (labeling)** — Class 9 label, subsidiary labels, CARGO AIRCRAFT ONLY label.
- **Subpart F (placarding)** — road leg to the gateway.
- **Subpart G (emergency response information)** — §172.602 ER information accompanying the
  shipping paper; §172.604 telephone number monitoring requirements.
- **Subpart H (training)** — §172.700–704, HazMat employee training, recurrent every three
  years, records retained. A standard finding category in any DG audit.

**Self-contradiction:** the library validates the §172.204 air shipper's certification at
line 141, in which the shipper declares the consignment is *"packaged, marked and
labeled/placarded"* in proper condition. v1.0 verifies the signature on that declaration while
possessing no capability to audit any of the three things being declared.

---

### F-07 — Part 175 coverage omits the core air carrier requirements
**Status:** ❌ Fail (verified by search — zero occurrences of §175.30, §175.33, §175.75)
**Location:** Part 7, lines 251–261

The air transport section contains three checks. Two are shipping paper items already covered
in Part 2 (AIR-001, AIR-002); the third is a passenger baggage rule (AIR-003, see F-01). The
net new air-specific audit capability is effectively zero.

Missing:
- **§175.33 — Notification to the pilot-in-command (NOTOC).** Dry ice must appear on the
  NOTOC. This is a flight safety document and its absence is a reportable finding. Not
  mentioned anywhere in v1.0.
- **§175.30 — Acceptance requirements / carrier acceptance check.**
- **§175.75 — Quantity limitations and cargo location.** Dry ice loading limits are an
  asphyxiation hazard in the hold.

---

### F-08 — Four of five pharma checks carry no regulatory citation
**Status:** ❌ Fail — violates the library's own Standing Rule 4
**Location:** Part 6, lines 244–247

Standing Rule 4 (line 13) states: *"Cite the specific regulatory section for every finding."*
The Source column of the Pharma checklist reads:

| Check | Stated source |
|---|---|
| PH-002 | "GDP guidelines; flag for IATA DGR review for air" |
| PH-003 | "GDP / Nexus Aurea SOP" |
| PH-004 | "Nexus Aurea audit scope" |
| PH-005 | "IATA DGR 67th Ed. — to be integrated" |

None is a citable authority. "GDP guidelines" is not a document — the applicable instruments
are EU GDP 2013/C 343/01, WHO TRS 961 Annex 9, USP <1079>, and 21 CFR 205.50 for US storage
and handling. "Nexus Aurea audit scope" is a self-reference. A finding issued under PH-004
cites the auditor's own scope statement as its authority.

The library breaches its own non-negotiable rule in 80% of the section that covers this
firm's primary commodity.

---

## HIGH AND MEDIUM FINDINGS

### F-09 — Class 3 packing group criteria: flash point stated as a PG I criterion; §173.121 never cited
**Status:** ❓ Unable to Verify | **Location:** Lines 151–157

The PG table gives PG I as flash point "Below −18 °C (0 °F)" with initial boiling point ≤35 °C,
and sources the table to "§172.101 Table."

Two concerns:
- **§173.121 is the packing group assignment section for Class 3 and is cited nowhere in the
  document** (verified by search). §172.101 is the Hazardous Materials Table; it lists
  assigned packing groups, it does not state the assignment criteria.
- Reviewer's understanding is that §173.121 assigns PG I on **initial boiling point ≤35 °C
  alone**, with flash point not a PG I criterion. If correct, the −18 °C threshold in v1.0 is
  an invented criterion and C3-002 ("Packing group correct for flash point") will mis-assign.

Both points require confirmation against §173.121. PG II and PG III rows appear consistent
with the reviewer's understanding.

### F-10 — §172.200 exception list omits the waste / hazardous substance carve-out
**Status:** ❓ Unable to Verify | **Location:** Line 46

v1.0 states the exceptions as: A-coded (except air), W-coded (except water), limited quantity
(except air/vessel), Category B infectious substances.

Reviewer's understanding is that §172.200(b) opens with a carve-out — the exceptions do **not**
apply to a hazardous waste or a hazardous substance. That qualifier is absent from v1.0. As
written, an auditor could clear a limited quantity hazardous substance as requiring no
shipping paper. Confirm against §172.200(b).

### F-11 — §173.27 (general requirements for transportation by aircraft) absent
**Status:** ❌ Fail | **Location:** Document-wide

Zero occurrences. §173.27 carries the air-specific packaging requirements — package pressure
differential, closure requirements, inner packaging quantity limits by aircraft type. For an
air freight auditor this is a core section.

### F-12 — OECD 439 listed as an accepted corrosivity test method
**Status:** ❓ Unable to Verify | **Location:** Line 184

v1.0 lists OECD 404, 430, 431, 435, **439**. OECD Test Guideline 439 is an in vitro skin
*irritation* method (reconstructed human epidermis); it does not determine corrosivity and
cannot support a Class 8 packing group assignment. If 439 is not in §173.137, an auditor
following v1.0 could accept an irritation study as classification evidence under C8-002.
Confirm the exact list in §173.137.

The PG I/II/III exposure-time and observation-period criteria at lines 178–182 appear
consistent with the reviewer's understanding of §173.137 and are not challenged.

### F-13 — §172.202 quantity and package paragraph assignments unconfirmed
**Status:** ❓ Unable to Verify — **downgraded from ❌ Fail, see correction below** | **Location:** Lines 109 and 260

Line 109 cites **§172.202(a)(7)** for number and type of packages.
Line 260 cites **§172.202(a)(6)** for net mass per package on air shipments.
Line 101 describes total quantity as a separate element with no paragraph cited.

**Correction (2026-09-09):** this finding originally stated that the three assignments "cannot
all be correct." That was overstated — three distinct paragraphs can each be correct, and the
JSON artifact assigns them cleanly as (a)(5) ground, (a)(6) air, (a)(7) packages. There is no
internal contradiction. What remains is an unverified three-way claim: the reviewer's residual
concern is that §172.202(a)(5) may carry total quantity for all modes with no separate air
paragraph at (a)(6). Confirm against §172.202(a). See `cfr-library-json-vs-md-delta.md`.

### F-14 — "ERG number" used for the emergency response telephone number
**Status:** ❌ Fail — **Markdown only; resolved in the JSON artifact** | **Location:** Line 61

ERG is the Emergency Response Guidebook. The requirement is an **emergency response telephone
number**, subject to monitoring requirements in Subpart G (§172.604) — the number must be
monitored at all times the material is in transportation, by a person knowledgeable of the
material or with immediate access to someone who is. v1.0 checks only that a number is
"present."

Conflating a guidebook with a monitored 24-hour contact number in a safety-critical checklist
is a terminology defect that will propagate into findings. The JSON artifact names this
correctly and cites §172.201(d); the finding is closed against the JSON and open against the
Markdown. Neither artifact cites §172.604, so the monitoring criteria stay unchecked in both. Related: §172.602 emergency
response **information** accompanying the shipping paper is not checked at all (see F-06).

### F-15 — Hazardous waste: EPA code cited to the HMR; the "Waste" prefix is never checked
**Status:** ❓ Unable to Verify | **Location:** Line 231 (C9-005)

C9-005 checks for the EPA waste code (e.g. D001) and cites §172.203(c)(1). EPA waste codes are
a 40 CFR 262 manifest requirement, not an HMR shipping paper requirement — this appears to be
a cross-title mis-citation.

Separately, the HMR requirement that the word **"Waste"** precede the proper shipping name is
not checked anywhere in the library. Confirm both against §172.203(c) and §172.101(c).

### F-16 — Class 6.2 (UN3373) and Class 2.2 cryogenic absent
**Status:** ❌ Fail | **Location:** Standing Rule 6 (line 15); line 46

Standing Rule 6 places Classes 2 and 6 in "reference only." Two problems:

- Line 46 already **relies** on the Category B infectious substances exception to scope a
  shipping paper check — the library depends on a Division 6.2 rule it declares out of scope,
  with §173.199 cited nowhere.
- **Class 2.2 cryogenic** (§173.320, liquid nitrogen dry shippers) is absent. This is the
  standing shipping mode for cell and gene therapy lanes and a common source of undeclared
  dangerous goods.

The repository carries `pharma/03-biological-substances/` as an active scope area. Library
scope and business scope do not agree.

### F-17 — No document control block
**Status:** ❌ Fail | **Location:** Header, lines 1–4

v1.0 has a version number and a build date. It has no document number, no author, no reviewer,
no approver, no signature, no effective date, no periodic review cycle, and no change history.

The document self-describes as "a working reference only" (line 295), but it is the sole
source of authority for findings issued to clients. That makes it a controlled document. Under
GDP Chapter 4 (Documentation), an unapproved and unsigned document used to generate regulated
findings is itself an audit finding — and the first one a client's quality unit will raise.

### F-18 — PH-005 is an active check sourced to a pending document
**Status:** ❌ Fail | **Location:** Lines 21, 247

IATA DGR 67th Edition is listed under PENDING SOURCES (line 21) as not yet integrated. PH-005
is written as an active check with "IATA DGR 67th Ed. — to be integrated" as its sole source.

A check whose authority is not in the library can only ever return ❓ Unable to Verify. It
should be held out of the active checklist and staged in a pending block until the source is
integrated, rather than shipped as if operational.

### F-19 — Definitional imprecision against source wording
**Status:** ❓ Unable to Verify | **Location:** Lines 35, 147, 149, 174

- **Line 147, §173.120(a):** the intentionally-heated limb omits the qualifier that the flash
  point be at or above 37.8 °C. The §173.120(a) exceptions are also omitted.
- **Line 149, §173.120(b)(2):** "NOT reclassifiable as combustible liquid for air or vessel"
  omits the qualifying clause permitting it where other means of transportation is
  impracticable. Directly relevant to an air operation.
- **Line 174, §173.136(a):** uses the GHS phrase "irreversible skin damage." The HMR wording
  is "full thickness destruction of human skin." Quoting non-regulatory wording in a
  citation-bearing document weakens the finding.
- **Line 35, marine pollutant:** "listed in §172.101 appendix with 'P' in Column 1" appears to
  conflate Appendix B (List of Marine Pollutants) with the Column 1 symbol set of the §172.101
  Table. The "PP" severe marine pollutant designation is also absent. Confirm the Column 1
  symbol set and Appendix B structure.

### F-20 — Worked example varies two attributes at once
**Status:** ❌ Fail | **Location:** Lines 72–73

The correct example is `UN2744, Cyclobutyl chloroformate, 6.1, (8, 3), PG II`. The "incorrect"
example is `Cyclobutyl chloroformate, UN2744, Corrosive, PG II` — which changes the element
order **and** restates a Division 6.1 material as "Corrosive."

The teaching point is sequence. Changing the hazard class in the same example risks seeding a
misclassification of UN2744 in a trainee's memory. Vary one attribute.

---

## RECOMMENDED FIXES

**Blocking — v1.0 must not be used for client work until these are closed**

- Re-cite every dry ice check to §173.217 and the applicable §172.202/§172.203 shipping paper
  paragraphs. Remove §175.10 as an authority for cargo findings. Retain AIR-003 only if the
  library is explicitly extended to passenger baggage, in a separate section.
- Add a Class 9 lithium battery checklist: §173.185, PI 965–970, Section IA/IB/II, state of
  charge for air, lithium battery mark, Class 9A label. Add a standing check that any shipment
  containing a temperature logger or tracker is screened as a lithium battery shipment.
- Populate Part 6 with actual temperature criteria: 2–8 °C, −20 °C, −70/−80 °C, CRT 15–25 °C,
  dry ice −78.5 °C, and a defined excursion threshold. Rewrite PH-002 and PH-005 to compare
  the declared range against the product requirement rather than test for presence.
- Add cross-document reconciliation checks: dry ice net weight per package identical across
  AWB, Shipper's Declaration, package marking and packing list; unit of measure mandatory (kg);
  declared temperature range identical across AWB, GDP handling instructions and CoA.
- Add Part 172 Subparts D, E, F, G and H. Marking and labeling defects are the leading cause of
  DG rejection at the counter, and the library currently certifies compliance it cannot audit.
- Add §175.33 (NOTOC), §175.30 (acceptance) and §175.75 (loading limits) to Part 7.
- Give every pharma check a citable authority (EU GDP 2013/C 343/01, WHO TRS 961 Annex 9,
  USP <1079>, 21 CFR 205.50). Where the authority is a Nexus Aurea SOP, cite the SOP by number
  and revision — not "Nexus Aurea audit scope."

**Required before release**

- Verify every ❓ item above against the current eCFR text. This session could not reach
  ecfr.gov, govinfo.gov or law.cornell.edu; verification must be performed from an environment
  with access, and the verification date recorded per section.
- Add §173.121 as the cited source for Class 3 packing group criteria and correct the PG I row.
- Add §173.27 for air packaging requirements.
- Add §173.199 (UN3373 Category B) and §173.320 (Class 2.2 cryogenic), and revise Standing
  Rule 6 so declared scope matches the lanes this firm actually handles.
- Reconcile the §172.202(a) paragraph designations at lines 109 and 260.
- Replace "ERG number" with "emergency response telephone number" and add the §172.604
  monitoring criteria.
- Move PH-005 into a pending block until the IATA DGR 67th Edition is integrated.

**Document control**

- Add a control block: document number, author, reviewer, approver, effective date, review
  cycle, change history. Under GDP an unapproved document cannot support a regulated finding.
- Record the CFR amendment date per section, not only the access date, so a finding can be
  defended against the edition in force on the shipment date.
- Add a separate title register. 49 CFR, 21 CFR and IATA DGR content must not sit in one
  undifferentiated structure — a finding must name its title and edition.

**Sustained**

- Correct the definitional wording at lines 35, 147, 149 and 174 to match source text exactly.
- Revise the worked example at line 73 to vary sequence only.

---

## ITEMS REVIEWED AND NOT CHALLENGED

For completeness — these were checked and no discrepancy was identified, subject to the same
primary-source verification limitation:

- §172.202 basic description sequence: UN number → PSN → hazard class → packing group, no
  information interspersed (line 70).
- Class 8 packing group criteria — exposure times and observation periods (lines 178–182).
- Class 9 subcategories against §173.140(a) and (b) (lines 204–210).
- UN1845 assigned no packing group (line 216).
- Shipper's certification language, ground and air (lines 138, 141).
- Offeror shipping paper retention: 2 years, 3 years for hazardous waste (line 62). Note that
  carrier-side retention obligations are not captured, and §172.204(c) air certification copy
  requirements are not captured.
- Finding status vocabulary (lines 285–291) — sound, and applied throughout this report.

---

*This report is DRAFT. No clearance, approval, or "safe to ship" conclusion is issued or
implied. Human review is required before any action is taken. All ❓ Unable to Verify findings
remain open until confirmed against primary source.*
