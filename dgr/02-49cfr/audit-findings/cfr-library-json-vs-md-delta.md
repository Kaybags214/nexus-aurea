# Delta Audit — CFR Library JSON vs Markdown, both "Version 1.0"

**Documents under review:**
- `dgr/02-49cfr/nexus_aurea_cfr_library.json` (version 1.0, built 2026-09-09)
- `dgr/02-49cfr/nexus-aurea-cfr-library-v1.0.md` (version 1.0, built 2026-09-09)

**Review date:** 2026-09-09
**Status:** DRAFT — human review required.
**Companion report:** `cfr-library-v1.0-audit-findings.md` (findings F-01 … F-20 against the Markdown)

The JSON is **not** a serialization of the Markdown. The two artifacts carry the same name,
the same version number and the same build date, and their content differs. All divergences
below were confirmed by parsing both files, not by reading.

---

## HEADLINE FINDING

### J-01 — Two documents, one version number, different content
**Status:** ❌ Fail | **Risk:** Critical

| Attribute | JSON | Markdown |
|---|---|---|
| Standing rules | **6** | **7** |
| Standing rule 3 status list | Pass / Fail / Warning / Unable to Verify | Pass / Fail / Warning / Unable to Verify / **Not Applicable** |
| Rule "Findings must identify discrepancies and missing data only" | present | **absent** |
| Active/reference audit classes | metadata fields | standing rules 6 and 7 |
| Class 3 exceptions from classification | **5 listed** | **0 — section absent** |
| Class 3 flash point definition | present | absent |
| Packing group exceptions list | present | absent |
| `effective_date` amendment claims | 3 sections | **none** |
| §172.202(a)(5) cited | yes | **no** |
| §172.203(k) cited | yes | **no** |
| §173.199 cited | yes (1×) | **no** |
| Emergency response phone terminology | correct | **"ERG number"** (see F-14) |

Under document control, two artifacts sharing an identifier and version while differing in
their **non-negotiable standing rules** is a fundamental defect. A finding issued today cannot
be traced to the rule set that produced it. Neither file references the other, and neither
declares which is authoritative.

**Fix:** designate one artifact as the source of record and generate the other from it. If both
must exist, they need distinct version identifiers and a stated generation direction.

---

## NEW FINDINGS — JSON ONLY

### J-02 — Standing rule 3 omits a status the library uses 16 times
**Status:** ❌ Fail (verified by parse) | **Risk:** High

JSON standing rule 3 reads: *"Mark each finding: Pass / Fail / Warning / Unable to Verify."*
"Not Applicable" is absent. Yet:

- `finding_status_definitions` defines `Not_Applicable`.
- **16 audit checks** in the JSON carry a `not_applicable` outcome.

The rule set forbids a status the checks depend on. An auditor following rule 3 literally has
no disposition for a check that does not apply, and will be pushed toward Pass — recording a
compliant result for a check that was never performed. That is the worst available failure
direction: a false Pass in the record.

### J-03 — Asserted amendment dates, one of them implausible
**Status:** ❓ Unable to Verify | **Risk:** High

The JSON adds `effective_date` fields absent from the Markdown:

| Section | Claim |
|---|---|
| §173.120 (Class 3) | "Amended 76 FR 3371, Jan. 19, 2011 (most recent amendment cited)" |
| §173.136 (Class 8) | "Amended 85 FR 27880, May 11, 2020" |
| §173.140 (Class 9) | **"Amended 58 FR 33305, June 16, 1993"** |

The Class 9 claim asserts §173.140 has stood unamended for over thirty years. Part 173 has been
revised repeatedly across the HM-215 international harmonisation series in that period. If the
claim is wrong, the library states — with the false precision of a Federal Register citation —
that its Class 9 text is current when it may not be.

The §173.120 field is worse in construction: "most recent amendment cited" is a hedge about the
library's own research, presented in a field an auditor will read as regulatory fact.

**These fields are more dangerous than the no-date state of the Markdown.** A missing date
prompts an auditor to check. A confidently wrong date stops them checking. Verify all three
against the Federal Register, or delete the fields and record the eCFR "current as of" date
instead.

### J-04 — The JSON contradicts itself on §175.10 within one file
**Status:** ❌ Fail (verified by parse) | **Risk:** Critical

The JSON's `part_175_air_transport` block gets this **right**: it titles §175.10 *"Exceptions
for Passengers, Crewmembers, and Air Operators,"* describes the dry ice rule as passenger-carried,
and scopes its audit check to *"passenger-carried dry ice."*

And then, in the same file:

- `C9-002` (cargo dry ice documentation) — source: `49 CFR §173.140(b), §175.10(a)(10)`
- `PH-001` (pharma cold-chain dry ice) — source: `49 CFR §173.140, §175.10(a)(10)`

The library demonstrably knows §175.10 is a passenger baggage exception and cites it anyway as
the regulatory authority for two commercial cargo checks. `pharma_temperature_sensitive.relevant_sections`
repeats it: *"§175.10 (air transport exceptions — dry ice passenger limits)"* — listed as
relevant to pharma cargo.

This strengthens **F-01** rather than resolving it. Both cargo checks must be re-cited to
§173.217 and the applicable §172.202/§172.203 paragraphs.

### J-05 — Declared scope excludes the firm's actual operations
**Status:** ❌ Fail | **Risk:** Medium

`library_meta.scope`: *"U.S. domestic hazardous materials transport."*

The business is international pharma air freight. The library itself concedes the gap in three
places — the Part 175 note ("For international air, IATA DGR 67th Edition governs"), PH-005's
source line, and PH-002's "flag for IATA DGR review when air transport." A reference library
whose declared scope excludes the firm's primary lane cannot support findings on that lane, and
every air-freight finding issued from it is out of its own stated scope.

---

## CORRECTION TO THE COMPANION REPORT

### F-13 — downgraded from ❌ Fail to ❓ Unable to Verify

The companion report recorded an internal citation conflict in §172.202 and stated that the
three paragraph assignments "cannot all be correct as assigned." **That was overstated.** The
JSON assigns them to three distinct paragraphs:

- `§172.202(a)(5)` — total quantity, ground/rail/sea
- `§172.202(a)(6)` — net mass per package, air
- `§172.202(a)(7)` — number and type of packages

Three distinct paragraphs can each be correct. There is no internal contradiction. The finding
is therefore **not** a Fail — it is a specific three-way claim requiring confirmation against
§172.202(a), which this environment cannot reach. The reviewer's residual concern is that
§172.202(a)(5) may carry total quantity for all modes with no separate air paragraph at (a)(6);
that concern is unverified and is recorded as such.

The Markdown remains weaker on this point: it cites (a)(6) and (a)(7) and gives no paragraph
for total quantity at all.

### F-14 — RESOLVED in the JSON, open in the Markdown

The JSON correctly names the requirement *"Emergency response telephone number"* and cites
`§172.201(d)`. The Markdown's "ERG number" phrasing does not appear.

The finding is **closed against the JSON** and **stays open against the Markdown**. Partial only:
neither artifact cites §172.604, so the monitoring criteria — number monitored at all times the
material is in transportation, attended by a person with knowledge of the material — remain
unchecked in both.

### F-19 — partially resolved in the JSON, with new drift

The JSON adds the five `exceptions_from_class_3` entries whose absence the companion report
flagged (§173.115, ASTM D4206, Appendix H, ISO 2592, the 99% and >90% water thresholds). None
has been verified against §173.120(a).

New drift in the JSON's §173.136 definition: *"liquids or solids that have a severe corrosion
rate."* The HMR limb reviewer recalls is narrower — a liquid, **or a solid which may become
liquid during transportation**. Dropping that qualifier widens the definition. Verify.

### F-16 — partially resolved

§173.199 is now cited once in the JSON, in the §172.200 exception list. There is still no
Division 6.2 audit section, and §173.320 (Class 2.2 cryogenic) remains absent from both files.

---

## FINDINGS THAT CARRY OVER UNCHANGED

Verified by parsing the JSON — every one of these is present in both artifacts:

| ID | Finding | Confirmation |
|---|---|---|
| F-01 | §175.10 mis-cited for cargo dry ice | C9-002 and PH-001 sources, above |
| F-02 | §173.217 absent | 0 occurrences in JSON, 0 in MD |
| F-03 | Lithium listed, never audited | UN3480/3481 appear once; **0** lithium audit checks |
| F-04 | No temperature values | searched 2–8, −20, −70, −80, 15–25, 20–25, 78.5 → **none present** |
| F-05 | Dry ice checks presence-only | no cross-document weight reconciliation in either file |
| F-06 | Subparts D/E/F/G/H absent | §172.301, §172.400, §172.500, §172.602, §172.604, §172.700 → 0 each |
| F-07 | Part 175 core sections absent | §175.30, §175.33 (NOTOC), §175.75 → 0 each; §175.10 is the **only** entry in `key_sections` |
| F-08 | Pharma checks lack citable authority | PH-002 "GDP guidelines (not 49 CFR)"; PH-003 "GDP / pharma SOP requirement"; PH-004 "Nexus Aurea audit scope"; PH-005 "to be added" |
| F-09 | Class 3 PG I flash point criterion; §173.121 uncited | PG I row still `flash_point: "Below -18°C (0°F)"`; source still "§172.101 Table, Column 5"; §173.121 → 0 occurrences |
| F-10 | §172.200 exceptions omit waste / hazardous substance carve-out | 4 exceptions listed, carve-out absent |
| F-11 | §173.27 absent | 0 occurrences |
| F-12 | OECD 439 listed as accepted method | still 5th entry in `test_methods_accepted`, self-labelled "In Vitro Skin **Irritation**" |
| F-15 | EPA waste code cited to the HMR; "Waste" prefix unchecked | C9-005 source unchanged |
| F-17 | No document control block | no author, reviewer, approver, effective date, or change history in either |
| F-18 | PH-005 active on a pending source | unchanged |
| F-20 | Worked example varies two attributes | `example_incorrect` unchanged |

**F-12 note:** the JSON makes this finding self-evident. Its own label for entry 5 reads
*"In Vitro Skin Irritation (RHE)"* — an irritation method, listed under `test_methods_accepted`
for a corrosivity classification. The document contradicts itself in a single string.

---

## RECOMMENDED FIXES — DELTA ONLY

Additional to the fixes in the companion report:

- **Designate a source of record.** One artifact is authoritative; the other is generated from
  it, or is retired. Two files at "Version 1.0" with different standing rules cannot both stand.
- **Reconcile the standing rules** to a single set, and restore "Not Applicable" to rule 3 in
  the JSON so the rules match the 16 checks and the status definitions that already use it.
- **Verify or delete the three `effective_date` fields.** Priority on §173.140's 1993 claim.
  Prefer recording the eCFR "current as of" date per section over Federal Register amendment
  citations, which go stale silently.
- **Re-cite C9-002, PH-001, and `pharma_temperature_sensitive.relevant_sections`** away from
  §175.10. The JSON's own Part 175 block already states the correct scope of that section —
  make the checks agree with it.
- **Correct `library_meta.scope`** to state the modes actually audited, or add international air
  as an explicit out-of-scope exclusion with the IATA module named as its successor.
- **Add a `schema_version` and a checksum** to the JSON so drift between artifacts is detectable
  mechanically rather than by inspection.

---

*This report is DRAFT. No clearance, approval, or "safe to ship" conclusion is issued or implied.
All ❓ Unable to Verify findings remain open until confirmed against primary source. Primary-source
access (ecfr.gov, govinfo.gov, law.cornell.edu) is blocked by network egress policy in this
environment; no citation in either artifact has been confirmed against current CFR text.*
