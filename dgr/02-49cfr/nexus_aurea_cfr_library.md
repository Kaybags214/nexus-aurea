# Nexus Aurea Inc. — 49 CFR Compliance Reference Library

> **Version:** 1.0.1 | **Schema:** 1.0.1 | **Last Updated:** 2026-09-09
> **Source of Record:** `nexus_aurea_cfr_library.json` — do not edit the Markdown directly; edit JSON and regenerate.
> **Integrity Note:** Run a structural diff between JSON and MD after any edit to confirm alignment. Schema version must be incremented on any structural change.

**Source Authority:** 49 CFR — Title 49, Code of Federal Regulations, Pipeline and Hazardous Materials Safety Administration (PHMSA), U.S. Department of Transportation
**Source URL:** https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-C

**Scope:** U.S. domestic and international air — DG Classes 3, 8, 9 and pharmaceutical/temperature-sensitive shipments. Note: International air transport is governed by IATA DGR 67th Edition (pending integration). All air freight findings from 49 CFR Part 175 are domestic scope only.

---

## Audit Classes

**Active:** Class 3, Class 8, Class 9, Pharma/Temperature-Sensitive
**Reference Only:** Class 1, Class 2, Class 4, Class 5, Class 6, Class 7

---

## Standing Rules

_These rules govern every audit finding produced from this library._

1. All findings are DRAFT. Human review required before any action is taken.
2. Never issue 'clearance', 'approved', or 'safe to ship' conclusions.
3. Mark each finding: Pass / Fail / Warning / Unable to Verify / Not Applicable.
4. Cite the specific regulatory section for every finding.
5. Never invent a missing regulation, shipping name, weight, or approval.
6. Findings must identify discrepancies and missing data only.

---

## Pending Sources

- IATA DGR 67th Edition (2026) — user has licensed copy; to be added
- IMDG Code — user will provide this week
- IATA DGR 66th Edition — user will provide this week
- ICAO Technical Instructions — under consideration
- WHO Guidelines — under consideration (pharma)

---

## 49 CFR Part 171 — General Information, Regulations, and Definitions

### Key Definitions — 49 CFR §171.8

#### Elevated temperature material

**Definition:** A material that, when offered for transportation or transported in a bulk packaging, is in a liquid phase and at a temperature at or above 100°C (212°F); or a material that is in a liquid phase with a flash point at or above 37.8°C (100°F) that is intentionally heated and offered for transportation or transported at or above its flash point; or in a solid phase and at a temperature at or above 240°C (464°F).

**Relevance:** Triggers Class 9 classification and special shipping paper notations (HOT).

#### Hazardous substance

**Definition:** A material, including its mixtures and solutions, that is listed in the appendix to §172.101, is in a quantity in one package that equals or exceeds the reportable quantity (RQ) listed in that appendix, and when in a mixture or solution, is in a concentration by weight which equals or exceeds the concentration listed in §171.8.

**Relevance:** Requires RQ notation on shipping papers.

#### Marine pollutant

**Definition:** A material listed in the appendix to §172.101 with a 'P' in column 1.

**Relevance:** Requires 'Marine Pollutant' notation on shipping papers; special segregation requirements.

#### Packing group

**Definition:** A grouping (PG I, II, or III) according to the degree of danger presented by hazardous materials. PG I = great danger; PG II = medium danger; PG III = minor danger.

**Relevance:** Must be verified on shipping paper and matches §172.101 table.

#### Proper shipping name

**Definition:** The primary name of the hazardous material as listed in §172.101 Table, Column 2.

**Relevance:** Must appear on shipping paper exactly as listed; no abbreviations unless authorized.

---

## 49 CFR Part 172, Subpart C — Shipping Papers

**URL:** https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-C/part-172/subpart-C

### §172.200 — Applicability

**Rule:** Every person offering a hazardous material for transportation must describe it on shipping papers as required by this subpart.

**Exceptions:**

- Materials marked 'A' in §172.101 Table Column 1 (except air transport)
- Materials marked 'W' in §172.101 Table Column 1 (except water transport)
- Limited quantity packages (except air or vessel transport)
- Category B infectious substances per §173.199

**Audit Check:**

| Field | Detail |
|-------|--------|
| Question | Is a shipping paper present for this DG shipment? |
| Pass | Shipping paper is present and covers all HM entries. |
| Fail | No shipping paper present for a regulated hazardous material. |
| Warning | Shipping paper present but may be missing required entries — check §172.202. |
| Unable to Verify | Document not legible or not provided. |

### §172.201 — Preparation and Retention of Shipping Papers

#### Rule 172.201.a.1

**Rule:** Hazardous material descriptions must appear first on the shipping paper OR be in a contrasting color OR be marked with 'X' or 'RQ' in a column captioned 'HM'.

| Field | Detail |
|-------|--------|
| Question | Is the HM description clearly distinguished from non-HM entries on the shipping paper? |
| Pass | HM entry is first, contrasting color, or 'X'/'RQ' marked in HM column. |
| Fail | HM entries are not distinguishable from non-HM entries. |
| Warning | Unclear presentation — verify HM column or ordering. |

#### Rule 172.201.a.2

**Rule:** The shipping paper and all copies must be legible and printed in English.

| Field | Detail |
|-------|--------|
| Question | Is the shipping paper legible and in English? |
| Pass | Legible, printed in English. |
| Fail | Not in English or not legible. |
| Warning | Partially legible or bilingual — English portion must contain all required fields. |

#### Rule 172.201.a.3

**Rule:** No codes or abbreviations unless specifically authorized.

| Field | Detail |
|-------|--------|
| Question | Does the shipping paper use any unauthorized codes or abbreviations? |
| Pass | No unauthorized codes or abbreviations found. |
| Fail | Unauthorized abbreviations or codes are present. |
| Warning | Abbreviations present — verify each is specifically authorized. |

#### Rule 172.201.d

**Rule:** Emergency response telephone number required on shipping paper.

| Field | Detail |
|-------|--------|
| Question | Is an emergency response telephone number present on the shipping paper? |
| Pass | Emergency response number is present. |
| Fail | No emergency response telephone number on shipping paper. |
| Warning | Number present but may not be 24-hr accessible — flag for review. |

#### Rule 172.201.e

**Rule:** Shipping papers must be retained for 2 years (3 years for hazardous waste) after acceptance by initial carrier. Must include acceptance date.

| Field | Detail |
|-------|--------|
| Question | Is the date of carrier acceptance noted on the shipping paper? |
| Pass | Acceptance date is present. |
| Fail | No acceptance date noted. |
| Warning | Date present but format is unclear. |

### §172.202 — Description of Hazardous Material on Shipping Papers — Required Basic Description

**Rule:** The basic description must appear in this exact sequence: (1) UN/NA ID Number, (2) Proper Shipping Name, (3) Hazard Class or Division, (4) Packing Group (in Roman numerals). No additional information may be interspersed.

**Required Elements:**

##### UN/NA Identification Number

**Source:** §172.101 Table, Column 4 | **Format:** UN#### or NA####

| Field | Detail |
|-------|--------|
| Question | Is a valid UN/NA ID number present and correctly formatted? |
| Pass | UN/NA number present and matches §172.101 Table for the stated material. |
| Fail | UN/NA number absent, incorrect, or does not match the proper shipping name. |
| Warning | Number present but not verified against §172.101 — flag for cross-check. |

##### Proper Shipping Name (PSN)

**Source:** §172.101 Table, Column 2 | **Format:** Must be the primary listed name; technical name in parentheses if 'G' in Column 1

| Field | Detail |
|-------|--------|
| Question | Is the proper shipping name correct, unabbreviated, and matching the §172.101 Table? |
| Pass | PSN matches §172.101 Table exactly for the stated UN number. |
| Fail | PSN is missing, abbreviated, or does not match the UN number. |
| Warning | PSN present but uses 'n.o.s.' without a required technical name in parentheses. |

##### Hazard Class or Division Number

**Source:** §172.101 Table, Column 3 | **Format:** Primary class followed by subsidiary class(es) in parentheses if required

| Field | Detail |
|-------|--------|
| Question | Is the primary hazard class and any required subsidiary hazard class present and correct? |
| Pass | Hazard class matches §172.101 Table; subsidiary classes correctly noted in parentheses. |
| Fail | Hazard class missing, incorrect, or subsidiary class omitted when required. |
| Warning | Hazard class present but subsidiary class notation unclear. |

##### Packing Group

**Source:** §172.101 Table, Column 5 | **Format:** Roman numerals: PG I, PG II, or PG III (may be preceded by 'PG')

**Exceptions:** Class 1 explosives, Self-reactive substances, Division 5.2, Entries with no assigned packing group

| Field | Detail |
|-------|--------|
| Question | Is the packing group present in Roman numerals and correct for this material? |
| Pass | Packing group is present in Roman numerals and matches §172.101 Table. |
| Fail | Packing group missing or incorrect. |
| Warning | Packing group present but not in Roman numeral format — flag. |

##### Total Quantity

**Source:** §172.202(a)(5) — ground/rail/sea; §172.202(a)(6) — air | **Format:** Ground: total quantity with unit of measure (e.g., '200 kg', '50 L'). Air: net mass per package or gross mass if indicated.

| Field | Detail |
|-------|--------|
| Question | Is the total quantity of hazardous material stated with correct units? |
| Pass | Quantity and unit of measure are present and appropriate for the mode of transport. |
| Fail | Quantity missing or unit of measure absent. |
| Warning | Quantity present but unit of measure may not match the mode of transport requirements. |

##### Number and Type of Packages

**Source:** §172.202(a)(7) | **Format:** e.g., '12 drums', '3 cylinders', '1 IBC'

| Field | Detail |
|-------|--------|
| Question | Is the number and type of packages stated? |
| Pass | Number and type of packages clearly stated. |
| Fail | Package count or type is missing. |
| Warning | Package type abbreviated — verify abbreviation is commonly accepted. |

**Sequence Check:**

Rule: Basic description must appear in order: UN/NA Number → PSN → Hazard Class → Packing Group. No information may be inserted between these four elements.

✅ Correct: `UN2744, Cyclobutyl chloroformate, 6.1, (8, 3), PG II`
❌ Incorrect: `Cyclobutyl chloroformate, UN2744, Corrosive, PG II`

| Field | Detail |
|-------|--------|
| Question | Is the basic description in the correct required sequence? |
| Pass | UN number, PSN, hazard class, PG appear in correct order with no interspersed data. |
| Fail | Elements are out of sequence or information is inserted between required elements. |
| Warning | Sequence appears correct but technical name placement needs verification. |

### §172.203 — Additional Description Requirements

#### Special Permit Notation

**Rule:** Must show 'DOT-SP' followed by special permit number when shipment is under a special permit.

| Field | Detail |
|-------|--------|
| Question | If a special permit applies, is 'DOT-SP [number]' noted on the shipping paper? |
| Pass | DOT-SP notation present and associated with the correct description. |
| Fail | Special permit shipment has no DOT-SP notation. |
| Warning | DOT-SP notation present but number is not readable. |
| Not Applicable | No special permit involved. |

#### Limited Quantity

**Rule:** Must include 'Limited Quantity' or 'Ltd Qty' following the basic description.

| Field | Detail |
|-------|--------|
| Question | If offered as limited quantity, is 'Limited Quantity' or 'Ltd Qty' noted? |
| Pass | LQ designation present following basic description. |
| Fail | LQ shipment has no LQ notation on shipping paper. |
| Not Applicable | Not a limited quantity shipment. |

#### Reportable Quantity (RQ)

**Rule:** The letters 'RQ' must appear before or after the basic description for each hazardous substance meeting RQ threshold.

| Field | Detail |
|-------|--------|
| Question | If this is a hazardous substance meeting RQ, is 'RQ' noted on the shipping paper? |
| Pass | 'RQ' present before or after basic description. |
| Fail | RQ threshold met but 'RQ' notation missing. |
| Not Applicable | Material does not meet RQ threshold. |

#### Air Transport Statement

**Rule:** For air shipments, must state whether the shipment is within limitations for passenger and cargo aircraft OR cargo aircraft only.

**Source:** §172.203(f)

| Field | Detail |
|-------|--------|
| Question | For air shipments, is the passenger/cargo or cargo-only aircraft statement present? |
| Pass | Statement present and correct for the material's air eligibility. |
| Fail | Air transport statement missing from air shipment documentation. |
| Warning | Statement present but does not clearly specify passenger+cargo vs. cargo-only. |

#### Elevated Temperature Material (HOT)

**Rule:** If a liquid meets elevated temperature definition and 'Molten' or 'Elevated temperature' is not in the PSN, the word 'HOT' must immediately precede the PSN.

**Source:** §172.203(n)

| Field | Detail |
|-------|--------|
| Question | For elevated temperature liquids, does 'HOT' precede the PSN if not already in the name? |
| Pass | 'HOT' is present preceding the PSN, or 'Molten'/'Elevated temperature' is in the PSN. |
| Fail | Elevated temperature liquid with no 'HOT' notation and no indication in PSN. |
| Not Applicable | Material is not an elevated temperature material. |

#### Marine Pollutant

**Rule:** Words 'Marine Pollutant' shall appear in association with the basic description. For n.o.s. entries, the name of the pollutant component must appear in parentheses.

**Source:** §172.203(l)

| Field | Detail |
|-------|--------|
| Question | If material is a marine pollutant, are 'Marine Pollutant' words and component name present? |
| Pass | 'Marine Pollutant' noted; component name in parentheses if n.o.s. entry. |
| Fail | Marine pollutant designation missing from shipping paper. |
| Not Applicable | Material is not a marine pollutant. |

#### Technical Name for n.o.s. Entries

**Rule:** If PSN is marked 'G' in §172.101 Column 1, the technical name of the hazardous constituent must appear in parentheses in association with the basic description.

**Source:** §172.203(k)

| Field | Detail |
|-------|--------|
| Question | For 'G'-marked n.o.s. entries, is the technical name in parentheses with the description? |
| Pass | Technical name in parentheses correctly identifies the hazardous constituent. |
| Fail | n.o.s. entry with 'G' designation has no technical name in parentheses. |
| Warning | Technical name present but may not identify the primary hazardous constituent. |

### §172.204 — Shipper's Certification

**Rule:** For most shipments, the shipper must certify on the shipping paper that the material is properly classified, described, packaged, marked, and labeled and is in proper condition for transport.

**Audit Check:**

| Field | Detail |
|-------|--------|
| Question | Is the shipper's certification present and complete on the shipping paper? |
| Pass | Certification present, signed, and contains required language for the mode of transport. |
| Fail | Certification missing, unsigned, or uses incorrect language. |
| Warning | Certification present but signature, date, or company name is missing. |

**Ground Certification Text:** _This is to certify that the above-named materials are properly classified, described, packaged, marked, and labeled, and are in proper condition for transportation according to the applicable regulations of the Department of Transportation._

**Air Certification Text:** _I hereby declare that the contents of this consignment are fully and accurately described above by the proper shipping name, and are classified, packaged, marked and labeled/placarded, and are in all respects in proper condition for transport according to applicable international and national governmental regulations._

| Field | Detail |
|-------|--------|
| Question | Is the shipper's certification present and complete on the shipping paper? |
| Pass | Certification present, signed, and contains required language for the mode of transport. |
| Fail | Certification missing, unsigned, or uses incorrect language. |
| Warning | Certification present but signature, date, or company name is missing. |

---

## 49 CFR Part 173 — Class 3: Flammable Liquids

**Section:** §173.120 | **URL:** https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-C/part-173/section-173.120
**eCFR Current As Of:** 2026-09-09
> ⚠️ FR amendment history not verified — Part 173 has been revised repeatedly via the HM-215 series and subsequent rulemakings. Check ecfr.gov for the current version before relying on any specific amendment cite.

### Definition

**Class 3 Flammable Liquid:** A liquid having a flash point of not more than 60°C (140°F), OR any material in liquid phase with a flash point at or above 37.8°C (100°F) that is intentionally heated and offered for transport at or above its flash point in a bulk packaging.

**Flash Point:** The minimum temperature at which a liquid gives off vapor in sufficient concentration to form an ignitable mixture with air near the surface of the liquid.

**Combustible Liquid:** A liquid with a flash point above 60°C (140°F) and below 93°C (200°F) that does not meet any other hazard class definition.

### Exceptions from Class 3

- Liquid meeting another hazard class definition per §173.115
- Mixture with ≥99% components having flash point ≥60°C not transported at or above flash point
- Liquid with flash point >35°C that does not sustain combustion per ASTM D4206 or Appendix H
- Liquid with flash point >35°C and fire point >100°C per ISO 2592
- Liquid with flash point >35°C in water-miscible solution with >90% water by mass

### Packing Groups — Source: §172.101 Table, Column 5

| Group | Flash Point | Initial Boiling Point |
|-------|-------------|----------------------|
| PG I | Below -18°C (0°F) | ≤35°C (95°F) |
| PG II | Below 23°C (73°F) | >35°C (95°F) |
| PG III | 23°C-60°C (73°F-140°F) | >35°C (95°F) |

### Audit Checklist

#### C3-001 — Flash point verification

**Question:** Does the declared flash point on the shipping document match the SDS flash point for this material?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | Flash point on document matches SDS within acceptable test method variance. |
| ❌ Fail | Flash point on document does not match SDS; or flash point is missing from documents. |
| ⚠️ Warning | Flash point present on document but SDS not available for cross-reference. |
| ❓ Unable to Verify | Neither document nor SDS provides flash point data. |
| 📎 Source | 49 CFR §173.120(a) |

#### C3-002 — Correct packing group assigned

**Question:** Is the stated packing group (PG I, II, or III) correct for the flash point and boiling point of this material?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | Packing group matches the flash point criteria for the assigned group. |
| ❌ Fail | Packing group does not correspond to the stated flash point. |
| ⚠️ Warning | Packing group present but flash point data is not sufficient to verify. |
| 📎 Source | 49 CFR §172.101 Table |

#### C3-003 — Proper shipping name matches UN number

**Question:** Does the proper shipping name correspond to the UN number in the §172.101 Table?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | PSN and UN number match §172.101 Table. |
| ❌ Fail | PSN and UN number do not correspond in §172.101 Table. |
| 📎 Source | 49 CFR §172.101, §172.202 |

#### C3-004 — Flash point notation for water shipments

**Question:** For shipments by water, is the minimum flash point (if ≤60°C) noted on the shipping paper?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | Flash point noted in association with basic description for water shipment. |
| ❌ Fail | Flash point not noted on shipping paper for water transport. |
| — Not Applicable | Shipment is not by water. |
| 📎 Source | 49 CFR §172.203(i)(2) |

#### C3-005 — Elevated temperature liquid — HOT notation

**Question:** If this Class 3 material is transported at or above its flash point in bulk, is the word 'HOT' preceding the PSN?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | 'HOT' precedes the PSN, or 'Molten'/'Elevated temperature' is included in the PSN. |
| ❌ Fail | Elevated temperature Class 3 bulk shipment missing 'HOT' notation. |
| — Not Applicable | Material not transported at or above flash point. |
| 📎 Source | 49 CFR §172.203(n), §173.120(a) |

#### C3-006 — Combustible liquid reclassification

**Question:** If material has flash point 38°C-60°C and no other hazard class applies, has it been reclassed as combustible liquid?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | Reclassification properly noted or not applicable. |
| ❌ Fail | Material meets combustible liquid criteria but is classified as Class 3 without justification. |
| ⚠️ Warning | Reclassification may apply — flag for shipper review. |
| 📎 Source | 49 CFR §173.120(b)(2) |
| 📝 Note | Reclassification as combustible liquid does not apply to vessel or aircraft transport. |

---

## 49 CFR Part 173 — Class 8: Corrosive Materials

**Section:** §173.136 | **URL:** https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-C/part-173/section-173.136
**eCFR Current As Of:** 2026-09-09
> ⚠️ FR amendment history not verified — Part 173 has been revised repeatedly via the HM-215 series and subsequent rulemakings. Check ecfr.gov for the current version before relying on any specific amendment cite.

### Definition

A liquid or solid that causes irreversible damage to human skin at the site of contact within a specified period of time. Also includes liquids or solids that have a severe corrosion rate on steel or aluminum exceeding 6.25 mm/year at 55°C.

### Packing Group Criteria — Source: 49 CFR §173.137

| Group | Criteria |
|-------|----------|
| PG I | Causes irreversible damage to intact skin within observation period of up to 60 minutes, starting after exposure of 3 minutes or less. |
| PG II | Causes irreversible damage to intact skin within observation period of up to 14 days, starting after exposure of more than 3 minutes but not more than 60 minutes. |
| PG III | Causes irreversible damage to intact skin within observation period of up to 14 days after exposure of more than 60 minutes but not more than 4 hours; OR exhibits corrosion rate on steel or aluminum exceeding 6.25 mm/year at 55°C. |

### Accepted Test Methods

- OECD Guideline Test No. 404 — Acute Dermal Irritation/Corrosion (in vivo)
- OECD Guideline Test No. 430 — In Vitro Skin Corrosion: Transcutaneous Electrical Resistance (TER)
- OECD Guideline Test No. 431 — In Vitro Skin Corrosion: Reconstructed Human Epidermis (RHE) Test Method
- OECD Guideline Test No. 435 — In Vitro Membrane Barrier Test Method for Skin Corrosion
- OECD Guideline Test No. 439 — In Vitro Skin Irritation: Reconstructed Human Epidermis (RHE) Test Method — NOTE: TG 439 is an irritation (not corrosion) test. It is used to support a finding of non-corrosivity; if the result indicates corrosive potential, assign PG II minimum or retest with TG 430/431/435.

### Audit Checklist

#### C8-001 — Corrosive material identification

**Question:** Is the material correctly identified as Class 8 based on skin corrosion or metal corrosion rate criteria?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | Material meets Class 8 definition per §173.136; classification is supported by SDS or test data. |
| ❌ Fail | Material classified as Class 8 but SDS or test data does not support this classification. |
| ⚠️ Warning | Classification not verifiable from documents provided — SDS not available. |
| 📎 Source | 49 CFR §173.136(a) |

#### C8-002 — Packing group assignment — Class 8

**Question:** Is the assigned packing group (PG I, II, or III) correct for the corrosivity data of this material?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | Packing group matches §173.137 criteria for the documented exposure time/corrosion rate. |
| ❌ Fail | Packing group does not correspond to the corrosivity data available. |
| ⚠️ Warning | Packing group present on document but corrosivity test data not available to verify. |
| 📎 Source | 49 CFR §173.137 |

#### C8-003 — Proper shipping name and UN number match

**Question:** Does the proper shipping name and UN number correspond correctly in the §172.101 Table?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | PSN and UN number are consistent with §172.101 Table. |
| ❌ Fail | PSN or UN number does not match §172.101 Table for this Class 8 material. |
| 📎 Source | 49 CFR §172.101, §172.202 |

#### C8-004 — Subsidiary hazard class notation

**Question:** If a subsidiary hazard applies (e.g., flammable, toxic), is it noted in parentheses after the primary class on the shipping paper?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | Subsidiary hazard class noted correctly in parentheses following primary class. |
| ❌ Fail | Subsidiary hazard is present per §172.101 Table but not noted on shipping paper. |
| — Not Applicable | No subsidiary hazard for this material. |
| 📎 Source | 49 CFR §172.202(a)(3) |

#### C8-005 — Skin corrosion data currency

**Question:** If legacy test data (pre-September 30, 1995) is referenced, is it properly authorized under §173.136(c)?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | Legacy data cited and falls within authorized use per §173.136(c). |
| ❌ Fail | Legacy data cited outside of authorized parameters. |
| — Not Applicable | No legacy data referenced. |
| 📎 Source | 49 CFR §173.136(c) |

---

## 49 CFR Part 173 — Class 9: Miscellaneous Hazardous Materials

**Section:** §173.140 | **URL:** https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-C/part-173/section-173.140
**eCFR Current As Of:** 2026-09-09
> ⚠️ FR amendment history not verified — Part 173 has been revised repeatedly via the HM-215 series and subsequent rulemakings. The 1993 FR cite (58 FR 33305) is stale and must NOT be cited in audit findings. Check ecfr.gov for the current version.

### Definition

A material which presents a hazard during transport but does not meet the definition of any other hazard class.

### Class 9 Includes

| Category | Description | Source |
|----------|-------------|--------|
| Aviation hazard | Any material with anesthetic, noxious, or similar properties that could cause extreme annoyance or discomfort to a flight crew member so as to prevent correct performance of assigned duties. | §173.140(a) |
| Elevated temperature material | Material meeting the definition in §171.8 for an elevated temperature material. | §173.140(b) |
| Hazardous substance | Material meeting the definition in §171.8 for a hazardous substance (RQ threshold). | §173.140(b) |
| Hazardous waste | Material meeting the definition in §171.8 for a hazardous waste. | §173.140(b) |
| Marine pollutant | Material meeting the definition in §171.8 for a marine pollutant. | §173.140(b) |

### Common Class 9 Materials

| Name | UN Number | Packing Group | Note |
|------|-----------|---------------|------|
| Dry Ice (Carbon Dioxide, Solid) | UN1845 | Not assigned | Common in pharma cold-chain shipments. |
| Lithium ion batteries | UN3480 / UN3481 | Not assigned | Transported with or without equipment. |
| Environmentally hazardous substances, liquid | UN3082 | PG III | Marine pollutant designation common. |
| Environmentally hazardous substances, solid | UN3077 | PG III | Marine pollutant designation common. |
| Elevated temperature liquid, n.o.s. | UN3257 | PG III | Liquid at or above 100°C. |
| Elevated temperature solid, n.o.s. | UN3258 | PG III | Solid at or above 240°C. |

### Audit Checklist

#### C9-001 — Class 9 material identification

**Question:** Is the material correctly identified as Class 9 — does it meet a Class 9 subcategory and not another primary hazard class?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | Material meets one of the Class 9 categories in §173.140 and is not better classified under another class. |
| ❌ Fail | Material classified as Class 9 but may belong to another hazard class. |
| ⚠️ Warning | Class 9 assigned — verify material does not meet criteria for Class 3, 6, or 8. |
| 📎 Source | 49 CFR §173.140 |

#### C9-002 — UN1845 Dry Ice — documentation requirements

**Question:** For dry ice shipments: Is UN1845 correctly stated? Is net weight of dry ice declared? Is packaging marked 'DRY ICE' or 'CARBON DIOXIDE, SOLID'?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | UN1845 stated; net weight declared; packaging marked correctly. |
| ❌ Fail | UN1845 missing, net weight not declared, or packaging not marked. |
| ⚠️ Warning | Dry ice present in pharma shipment but UN1845 declaration not found — check if RQ threshold applies. |
| — Not Applicable | No dry ice in this shipment. |
| 📎 Source | 49 CFR §173.140(b) |
| 🔖 Source Note | §175.10 removed — that section governs passenger/crew/operator exceptions only and does not apply to commercial cargo documentation checks. |

#### C9-003 — Marine pollutant notation

**Question:** If material is a Class 9 marine pollutant, are 'Marine Pollutant' words and component name present on the shipping paper?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | 'Marine Pollutant' noted; component name in parentheses for n.o.s. entries. |
| ❌ Fail | Marine pollutant designation missing from shipping paper. |
| — Not Applicable | Material is not a marine pollutant. |
| 📎 Source | 49 CFR §172.203(l), §173.140(b) |

#### C9-004 — Elevated temperature notation

**Question:** For elevated temperature Class 9 materials, is 'HOT' preceding the PSN (if not already in the name)?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | 'HOT' precedes the PSN, or 'Elevated temperature' is in the PSN. |
| ❌ Fail | Elevated temperature Class 9 material missing 'HOT' notation. |
| — Not Applicable | Material is not an elevated temperature material. |
| 📎 Source | 49 CFR §172.203(n), §173.140(b) |

#### C9-005 — Hazardous waste — EPA waste code

**Question:** For hazardous waste classified as Class 9, is the EPA hazardous waste number included on the shipping paper?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | EPA waste code (e.g., D001) present on shipping paper in association with basic description. |
| ❌ Fail | EPA waste code missing from hazardous waste shipment. |
| — Not Applicable | Material is not a hazardous waste. |
| 📎 Source | 49 CFR §172.203(c)(1), §173.140(b) |

---

## 49 CFR — Pharmaceutical / Temperature-Sensitive Shipments

> No single 49 CFR section governs all pharma shipments. Compliance draws from multiple sections. IATA DGR 67th Edition (and GDP guidelines) govern air transport of temperature-sensitive pharmaceuticals. This section captures the 49 CFR elements relevant to pharma documentation review.

### Relevant 49 CFR Sections

- §173.140 (Class 9 — dry ice, elevated temperature)
- §172.202 (shipping paper basic description)
- §172.203 (additional description — RQ, elevated temp, marine pollutant)

> ⚠️ §175.10 removed from pharma checklist relevant_sections — that section governs passenger, crewmember, and operator exceptions only. It is correctly scoped under part_175_air_transport for passenger-carried dry ice checks. Commercial cargo pharma checks cite §173.140(b) only.

### Audit Checklist

#### PH-001 — Dry ice (UN1845) declaration — pharma cold-chain

**Question:** Is UN1845 declared on all shipping documents where dry ice is used as a refrigerant?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | UN1845 declared; net weight of dry ice stated; packaging marked 'DRY ICE' or 'CARBON DIOXIDE, SOLID'. |
| ❌ Fail | Dry ice confirmed in shipment but UN1845 declaration is absent from all documents. |
| ⚠️ Warning | Dry ice mentioned on commercial invoice or packing list but not declared on the shipping paper. |
| 📎 Source | 49 CFR §173.140(b) |
| 🔖 Source Note | §175.10 removed — that section governs passenger/crew/operator exceptions only and does not apply to commercial cargo documentation checks. For passenger-carried dry ice limits, see Part 175 section in this library. |

#### PH-002 — Temperature control requirements documented

**Question:** Are temperature handling/storage requirements documented in the shipment record (e.g., GDP temperature instructions, temperature monitoring records)?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | Temperature requirements present in shipment documentation. |
| ❌ Fail | Temperature-sensitive pharmaceutical shipment with no temperature control documentation. |
| ⚠️ Warning | Temperature requirements referenced on commercial invoice only — not on all required documents. |
| ❓ Unable to Verify | Temperature control documents not included in the package submitted for review. |
| 📎 Source | GDP guidelines (not 49 CFR); flag for IATA DGR review when air transport. |

#### PH-003 — Chain-of-custody documentation present

**Question:** Is a chain-of-custody document present for this pharmaceutical shipment?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | Chain-of-custody document present, signed, and covers the shipment period. |
| ❌ Fail | No chain-of-custody document present. |
| ⚠️ Warning | Chain-of-custody document referenced but not included in the document package. |
| ❓ Unable to Verify | Document not provided for review. |
| 📎 Source | GDP / pharma SOP requirement — flag for human review. |

#### PH-004 — Certificate of Analysis / Conformance

**Question:** If provided, does the Certificate of Analysis or Conformance match the product described on the shipping paper?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | Certificate product name, lot number, and quantity match shipping paper. |
| ❌ Fail | Certificate does not match shipping paper — discrepancy in name, lot, or quantity. |
| ⚠️ Warning | Certificate present but lot number or quantity not clearly legible. |
| — Not Applicable | No certificate provided or required for this shipment. |
| 📎 Source | Nexus Aurea audit scope — document cross-check |

#### PH-005 — Air waybill temperature notation

**Question:** For air transport of temperature-sensitive pharma, does the air waybill include special handling instructions (e.g., 'KEEP FROZEN', 'KEEP REFRIGERATED', temperature range)?

| Disposition | Criteria |
|-------------|----------|
| ✅ Pass | Air waybill contains appropriate temperature handling instructions. |
| ❌ Fail | Temperature-sensitive pharma on air waybill with no handling instructions. |
| ⚠️ Warning | Handling instructions present but temperature range not specified. |
| — Not Applicable | Not an air shipment. |
| 📎 Source | IATA DGR 67th Edition — to be added when source is integrated. |

---

## 49 CFR Part 175 — Carriage by Aircraft

**URL:** https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-C/part-175

> Part 175 governs U.S. domestic air transport of hazardous materials. For international air, IATA DGR 67th Edition governs and will be integrated as a separate library module.

### Key Sections

#### §175.10 — Exceptions for Passengers, Crewmembers, and Air Operators

**Relevance:** Defines what hazardous materials are permissible in carry-on or checked baggage. Critical for pharma shipments involving dry ice or personal use medical devices.

**Dry Ice Rule:** Dry ice (UN1845) for perishables may be carried by passengers: maximum 2.5 kg (5.5 lbs) per person. Package must permit release of CO2 gas. Checked baggage must be marked 'DRY ICE' or 'CARBON DIOXIDE, SOLID' with net weight.

**Source:** §175.10(a)(10)

| Field | Detail |
|-------|--------|
| Question | For passenger-carried dry ice: is quantity within 2.5 kg limit and is packaging marked correctly? |
| Pass | Quantity ≤2.5 kg; packaging marked 'DRY ICE' or 'CARBON DIOXIDE, SOLID' with net weight. |
| Fail | Quantity exceeds 2.5 kg limit or packaging not correctly marked. |
| Not Applicable | Dry ice is not passenger-carried in this shipment. |

### Air Transport Shipping Paper Requirements

**Rule:** For all air shipments, shipping paper must state whether shipment is within limitations for: (a) Passenger and cargo aircraft, OR (b) Cargo aircraft only.

**Source:** 49 CFR §172.203(f)

#### AIR-001

| Field | Detail |
|-------|--------|
| Question | Is the passenger/cargo or cargo-only aircraft authorization statement present on the air shipping paper? |
| Pass | Statement present and consistent with the material's authorized air eligibility. |
| Fail | Statement missing from air shipment shipping paper. |
| Warning | Statement present but does not clearly specify which aircraft type is authorized. |

### Quantity Per Package — Air

**Rule:** For air transport, the total net mass per package (not total shipment) must be shown on the shipping paper, unless gross mass is specified in §172.101 Table Columns 9A or 9B.

**Source:** 49 CFR §172.202(a)(6)

#### AIR-002

| Field | Detail |
|-------|--------|
| Question | Does the air shipping paper show net mass per package (or authorized gross mass per package)? |
| Pass | Net mass or authorized gross mass per package is stated on the shipping paper. |
| Fail | Air shipping paper shows only total shipment quantity, not per-package quantity. |
| Warning | Quantity present but unclear whether it is per-package or total. |

---

## Standard Documents to Check per Shipment

| Document | Required For | Key Checks |
|----------|-------------|------------|
| Air Waybill (AWB) | All air shipments | Shipper/consignee details; Cargo description matches shipping paper; Special handling codes; Temperature instructions for pharma |
| Shipper's Declaration for Dangerous Goods | DG air shipments | Basic description sequence; Packing group; Quantity per package; Passenger/cargo aircraft statement; Shipper certification |
| Commercial Invoice | All shipments | Product description consistency with shipping paper; Quantity/weight consistency |
| Packing List | All shipments | Package count matches shipping paper; Contents consistent with declared commodity |
| UN1845 Dry Ice Declaration | Shipments with dry ice | UN1845 present; Net weight of dry ice declared; Packaging marking |
| GDP Temperature-Handling Instructions | Temperature-sensitive pharma | Temperature range specified; Handling instructions present |
| Temperature Monitoring Records | Temperature-sensitive pharma (when provided) | Continuous record; No excursions or excursions documented |
| Chain-of-Custody Document | Pharmaceutical shipments (Nexus Aurea SOP) | Signature chain complete; Dates/times consistent; No unaccounted gaps |
| Certificate of Analysis / Conformance | When provided by shipper | Product name, lot number, quantity match shipping paper; Issued by authorized party |

---

## Finding Status Definitions

| Status | Meaning |
|--------|---------|
| **Pass** | Document element is present, correct, and consistent with the cited regulation. |
| **Fail** | Document element is missing, incorrect, or inconsistent with the cited regulation. Requires immediate flagging for human review. |
| **Warning** | Document element is present but contains an anomaly or ambiguity that requires human verification before release. |
| **Unable to Verify** | The required document or data element was not provided or is not legible. Cannot confirm compliance or non-compliance. |
| **Not Applicable** | The rule or check does not apply to this shipment type, mode, or material. |

---

_End of Nexus Aurea Inc. 49 CFR Compliance Reference Library_

_Generated from `nexus_aurea_cfr_library.json` v1.0.1 on 2026-09-09_