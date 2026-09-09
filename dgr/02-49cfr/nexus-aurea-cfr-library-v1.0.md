# Nexus Aurea Inc. — 49 CFR Compliance Reference Library
**Version:** 1.0 | **Built:** 2026-09-09
**Authority:** 49 CFR — Title 49, Code of Federal Regulations, PHMSA, U.S. Department of Transportation
**Source URL:** https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-C

---

## ⚠️ STANDING RULES — NON-NEGOTIABLE

1. All findings are **DRAFT**. Human review required before any action is taken.
2. Never issue "clearance," "approved," or "safe to ship" conclusions.
3. Every finding must be marked: **Pass / Fail / Warning / Unable to Verify / Not Applicable**
4. Cite the specific regulatory section for every finding.
5. Never invent a missing regulation, shipping name, weight, or approval.
6. Active audit classes: **Class 3, Class 8, Class 9, Pharma/Temperature-Sensitive**
7. Reference only (do not actively audit unless requested): Classes 1, 2, 4, 5, 6, 7

---

## ⏳ PENDING SOURCES (to be added when received)
- IATA DGR 67th Edition (2026) — user has licensed copy
- IMDG Code — user providing this week
- IATA DGR 66th Edition — user providing this week
- ICAO Technical Instructions — under consideration
- WHO Guidelines — under consideration (pharma)

---

## PART 1 — KEY DEFINITIONS (49 CFR §171.8)

| Term | Definition | Audit Relevance |
|---|---|---|
| **Elevated temperature material** | Liquid at/above 100°C in bulk; OR liquid with flash point ≥37.8°C transported at/above flash point in bulk; OR solid at/above 240°C | Triggers Class 9; requires "HOT" on shipping paper |
| **Hazardous substance** | Listed in §172.101 appendix; quantity in one package ≥ reportable quantity (RQ) | Requires "RQ" notation on shipping paper |
| **Marine pollutant** | Listed in §172.101 appendix with "P" in Column 1 | Requires "Marine Pollutant" on shipping paper |
| **Packing group** | PG I = great danger; PG II = medium danger; PG III = minor danger | Must be verified against §172.101 Table |
| **Proper shipping name (PSN)** | Primary name from §172.101 Table, Column 2 | Must appear exactly on shipping paper; no unauthorized abbreviations |

---

## PART 2 — SHIPPING PAPERS (49 CFR Part 172, Subpart C)

### §172.200 — Applicability
Every person offering a hazardous material for transport must describe it on a shipping paper.

**Exceptions:** A-coded materials (except air), W-coded materials (except water), limited quantity packages (except air/vessel), Category B infectious substances.

| Check | Pass | Fail | Warning |
|---|---|---|---|
| Is a shipping paper present? | Present and covers all HM entries | No shipping paper for regulated HM | Present but entries may be incomplete |

---

### §172.201 — Preparation and Retention

| Rule | Check | Pass | Fail |
|---|---|---|---|
| HM entries must appear first, OR in contrasting color, OR marked "X"/"RQ" in HM column | Is HM clearly distinguished? | Yes — first, contrasting, or HM column marked | HM entries not distinguishable |
| Must be legible and in English | Legible and in English? | Yes | Not in English or not legible |
| No unauthorized codes or abbreviations | Any unauthorized abbreviations? | None found | Unauthorized abbreviations present |
| Emergency response telephone number required | ERG number present? | Present | Missing |
| Retained 2 years (3 years hazardous waste); acceptance date required | Acceptance date on document? | Present | Missing |

---

### §172.202 — Required Basic Description (SEQUENCE IS MANDATORY)

**Required order — no information may be inserted between these four elements:**

> **[1] UN/NA Number → [2] Proper Shipping Name → [3] Hazard Class → [4] Packing Group**

**Example (correct):** `UN2744, Cyclobutyl chloroformate, 6.1, (8, 3), PG II`
**Example (incorrect):** `Cyclobutyl chloroformate, UN2744, Corrosive, PG II`

#### Element Checks

**1. UN/NA Identification Number** (§172.101 Table, Column 4)

| Check | Pass | Fail | Warning |
|---|---|---|---|
| UN/NA number present and correct? | Matches §172.101 Table for stated material | Absent, incorrect, or mismatched to PSN | Present but not cross-checked against Table |

**2. Proper Shipping Name** (§172.101 Table, Column 2)

| Check | Pass | Fail | Warning |
|---|---|---|---|
| PSN correct and unabbreviated? | Matches §172.101 Table exactly | Missing, abbreviated, or wrong | n.o.s. entry without required technical name |

**3. Hazard Class / Division** (§172.101 Table, Column 3)

| Check | Pass | Fail | Warning |
|---|---|---|---|
| Primary and subsidiary class correct? | Matches Table; subsidiary in parentheses | Missing, incorrect, or subsidiary omitted | Present but subsidiary unclear |

**4. Packing Group** (Roman numerals — §172.101 Table, Column 5)

| Check | Pass | Fail | Warning |
|---|---|---|---|
| PG in Roman numerals and correct? | Correct PG in Roman numerals | Missing or incorrect | Not in Roman numeral format |

**5. Total Quantity with Units**
- Ground/rail/sea: total quantity with unit (e.g., "200 kg", "50 L")
- Air: net mass per package (not total shipment)

| Check | Pass | Fail | Warning |
|---|---|---|---|
| Quantity and correct units present? | Present and appropriate for mode | Missing or no unit of measure | Present but mode-of-transport match unclear |

**6. Number and Type of Packages** (§172.202(a)(7))

| Check | Pass | Fail | Warning |
|---|---|---|---|
| Package count and type stated? | Clearly stated (e.g., "12 drums") | Missing count or type | Abbreviated type — verify it is common/accepted |

---

### §172.203 — Additional Description Requirements

| Field | Rule | Pass | Fail | N/A |
|---|---|---|---|---|
| **Special Permit** | "DOT-SP [number]" when under special permit | Notation present | Missing from special permit shipment | No special permit |
| **Limited Quantity** | "Limited Quantity" or "Ltd Qty" after basic description | Present | Missing from LQ shipment | Not LQ |
| **RQ Notation** | "RQ" before or after basic description for hazardous substances | "RQ" present | Missing when RQ threshold is met | Below RQ |
| **Air Transport Statement** | States "Passenger and Cargo Aircraft" or "Cargo Aircraft Only" | Statement present | Missing from air shipment docs | Not air |
| **HOT Notation** | "HOT" immediately before PSN for elevated temperature liquids in bulk (unless PSN already contains "Molten" or "Elevated temperature") | "HOT" present or in PSN | Missing for elevated temperature bulk liquid | Not elevated temp |
| **Marine Pollutant** | "Marine Pollutant" in association with description; component name in parentheses for n.o.s. entries | Noted correctly | Designation missing | Not marine pollutant |
| **Technical Name (n.o.s. / "G" entries)** | Technical name in parentheses when PSN is "G"-coded in §172.101 Column 1 | Technical name in parentheses | Missing for G-coded n.o.s. entry | Not a G-coded entry |

---

### §172.204 — Shipper's Certification

| Check | Pass | Fail | Warning |
|---|---|---|---|
| Certification present with required language? | Present, signed, correct language for mode | Missing or unsigned | Present but missing signature, date, or company name |

**Required language (ground):**
> "This is to certify that the above-named materials are properly classified, described, packaged, marked, and labeled, and are in proper condition for transportation according to the applicable regulations of the Department of Transportation."

**Required language (air):**
> "I hereby declare that the contents of this consignment are fully and accurately described above by the proper shipping name, and are classified, packaged, marked and labeled/placarded, and are in all respects in proper condition for transport according to applicable international and national governmental regulations."

---

## PART 3 — CLASS 3: FLAMMABLE LIQUIDS (49 CFR §173.120)

**Definition:** A liquid with a flash point of **≤60°C (140°F)**, OR a liquid intentionally heated and transported at or above its flash point in bulk.

**Combustible liquid:** Flash point **>60°C and <93°C** (200°F) — does not meet another hazard class. NOT reclassifiable as combustible liquid for air or vessel.

### Packing Group Criteria (§172.101 Table)

| Packing Group | Flash Point | Initial Boiling Point |
|---|---|---|
| **PG I** | Below -18°C (0°F) | ≤35°C (95°F) |
| **PG II** | Below 23°C (73°F) | >35°C (95°F) |
| **PG III** | 23°C – 60°C (73°F – 140°F) | >35°C (95°F) |

### Class 3 Audit Checklist

| Check ID | Check | Pass | Fail | Warning | Source |
|---|---|---|---|---|---|
| **C3-001** | Flash point on document matches SDS | Flash points match within test variance | Mismatch or flash point missing | SDS not available for comparison | §173.120(a) |
| **C3-002** | Packing group correct for flash point | PG matches flash point criteria | PG incorrect for stated flash point | Flash point data insufficient to verify PG | §172.101 Table |
| **C3-003** | PSN matches UN number | PSN and UN match §172.101 Table | Mismatch | — | §172.101, §172.202 |
| **C3-004** | Flash point noted for water shipments (if ≤60°C) | Flash point noted on shipping paper | Missing for water transport | — | §172.203(i)(2) |
| **C3-005** | "HOT" notation for elevated temperature bulk | "HOT" precedes PSN or "Molten"/"Elevated temperature" in PSN | Missing | — | §172.203(n), §173.120(a) |
| **C3-006** | Combustible liquid reclassification check | Properly noted or not applicable | Classified as Class 3 without justification when combustible liquid criteria met | Reclassification may apply | §173.120(b)(2) |

---

## PART 4 — CLASS 8: CORROSIVE MATERIALS (49 CFR §173.136 / §173.137)

**Definition:** A liquid or solid that causes **irreversible skin damage** within a specified time; OR a liquid/solid with **severe corrosion rate on steel or aluminum** (>6.25 mm/year at 55°C).

### Packing Group Criteria (§173.137)

| Packing Group | Skin Exposure Time | Observation Period | Metal Corrosion |
|---|---|---|---|
| **PG I** | ≤3 minutes | Up to 60 minutes | — |
| **PG II** | >3 min, ≤60 min | Up to 14 days | — |
| **PG III** | >60 min, ≤4 hours | Up to 14 days | OR >6.25 mm/year on steel or aluminum at 55°C |

**Accepted Test Methods:** OECD Test No. 404, 430, 431, 435, 439

### Class 8 Audit Checklist

| Check ID | Check | Pass | Fail | Warning | Source |
|---|---|---|---|---|---|
| **C8-001** | Material correctly identified as Class 8 | SDS or test data supports classification | SDS/data does not support Class 8 | SDS not available | §173.136(a) |
| **C8-002** | Packing group correct for corrosivity data | PG matches §173.137 criteria | PG incorrect for available data | Test data not available to verify | §173.137 |
| **C8-003** | PSN and UN number match §172.101 Table | Match confirmed | Mismatch | — | §172.101, §172.202 |
| **C8-004** | Subsidiary hazard class noted (if applicable) | Subsidiary noted in parentheses | Subsidiary present in Table but missing on document | — | §172.202(a)(3) |
| **C8-005** | Legacy test data (pre-Sept 30, 1995) — authorized? | Authorized per §173.136(c) | Outside authorized parameters | — | §173.136(c) |

---

## PART 5 — CLASS 9: MISCELLANEOUS HAZARDOUS MATERIALS (49 CFR §173.140)

**Definition:** A material presenting a hazard during transport that does not meet the definition of any other hazard class.

### Class 9 Subcategories

| Category | Description | Source |
|---|---|---|
| Aviation hazard | Anesthetic/noxious — could impair flight crew | §173.140(a) |
| Elevated temperature material | Liquid ≥100°C (bulk) or solid ≥240°C | §173.140(b) |
| Hazardous substance | Meets §171.8 definition; ≥RQ in one package | §173.140(b) |
| Hazardous waste | Meets §171.8 definition | §173.140(b) |
| Marine pollutant | Listed in §172.101 appendix with "P" | §173.140(b) |

### Common Class 9 Materials

| Material | UN Number | Packing Group | Note |
|---|---|---|---|
| Dry Ice (Carbon Dioxide, Solid) | UN1845 | Not assigned | Common in pharma cold-chain |
| Lithium ion batteries | UN3480 / UN3481 | Not assigned | With or without equipment |
| Environmentally hazardous substance, liquid | UN3082 | PG III | Marine pollutant common |
| Environmentally hazardous substance, solid | UN3077 | PG III | Marine pollutant common |
| Elevated temperature liquid, n.o.s. | UN3257 | PG III | Liquid ≥100°C |
| Elevated temperature solid, n.o.s. | UN3258 | PG III | Solid ≥240°C |

### Class 9 Audit Checklist

| Check ID | Check | Pass | Fail | Warning | Source |
|---|---|---|---|---|---|
| **C9-001** | Material correctly identified as Class 9 | Meets a Class 9 subcategory; no better primary class | May belong to another class | Verify does not meet Class 3, 6, or 8 | §173.140 |
| **C9-002** | UN1845 dry ice — UN declared, net weight stated, packaging marked | All three elements present | Any element missing | Dry ice in pharma shipment but declaration not found | §173.140(b), §175.10(a)(10) |
| **C9-003** | Marine pollutant notation | "Marine Pollutant" noted; component named for n.o.s. | Designation missing | — | §172.203(l), §173.140(b) |
| **C9-004** | "HOT" notation for elevated temperature | "HOT" precedes PSN or in PSN | Missing | — | §172.203(n), §173.140(b) |
| **C9-005** | Hazardous waste — EPA waste code present | EPA code (e.g., D001) on shipping paper | Missing | — | §172.203(c)(1), §173.140(b) |

---

## PART 6 — PHARMACEUTICAL / TEMPERATURE-SENSITIVE SHIPMENTS

> **Note:** No single 49 CFR section covers all pharmaceutical shipments. This section captures 49 CFR elements relevant to pharma documentation review. IATA DGR 67th Edition governs air pharma — to be added when source is integrated.

### Pharma Audit Checklist

| Check ID | Check | Pass | Fail | Warning | Source |
|---|---|---|---|---|---|
| **PH-001** | UN1845 declared for all dry ice refrigerant use | UN1845 declared; net weight stated; packaging marked | Dry ice confirmed but UN1845 absent from all documents | Mentioned on invoice/packing list but not on shipping paper | §173.140, §175.10(a)(10) |
| **PH-002** | Temperature control requirements documented | Temperature requirements present in shipment documentation | Temp-sensitive pharma with no temperature documentation | Temperature referenced on invoice only | GDP guidelines; flag for IATA DGR review for air |
| **PH-003** | Chain-of-custody document present | Present, signed, covers shipment period | Not present | Referenced but not included | GDP / Nexus Aurea SOP |
| **PH-004** | Certificate of Analysis/Conformance matches shipping paper | Product name, lot number, quantity match | Certificate does not match shipping paper | Present but lot or quantity not legible | Nexus Aurea audit scope |
| **PH-005** | Air waybill has temperature handling instructions | Handling instructions with temperature range present | Temp-sensitive pharma on AWB with no handling instructions | Instructions present but temp range not specified | IATA DGR 67th Ed. — to be integrated |

---

## PART 7 — AIR TRANSPORT (49 CFR Part 175)

> **Note:** Part 175 covers U.S. domestic air transport. International air = IATA DGR 67th Edition (to be added).

### Key Air Transport Checks

| Check ID | Check | Pass | Fail | Warning | Source |
|---|---|---|---|---|---|
| **AIR-001** | Passenger/cargo or cargo-only statement on shipping paper | Statement present; matches material's authorized aircraft type | Statement missing | Present but type not clearly specified | §172.203(f) |
| **AIR-002** | Quantity shown as net mass per package (not total shipment) | Net mass per package stated | Only total shipment quantity shown | Present but unclear if per-package or total | §172.202(a)(6) |
| **AIR-003** | Dry ice (UN1845) passenger limit | ≤2.5 kg per person; packaging marked; package permits CO2 release | Exceeds 2.5 kg or marking missing | — | §175.10(a)(10) |

---

## PART 8 — STANDARD DOCUMENT AUDIT SCOPE

For every shipment review, check the following documents when present:

| Document | Required For | Key Checks |
|---|---|---|
| **Air Waybill (AWB)** | All air shipments | Shipper/consignee; cargo description matches shipping paper; special handling codes; temp instructions for pharma |
| **Shipper's Declaration for Dangerous Goods** | DG air shipments | Basic description sequence; PG; quantity per package; passenger/cargo statement; shipper certification |
| **Commercial Invoice** | All shipments | Product description consistency; quantity/weight consistency |
| **Packing List** | All shipments | Package count matches shipping paper; contents consistent with declared commodity |
| **UN1845 Dry Ice Declaration** | Shipments with dry ice | UN1845 present; net weight declared; packaging marking |
| **GDP Temperature-Handling Instructions** | Temperature-sensitive pharma | Temperature range specified; handling instructions present |
| **Temperature Monitoring Records** | Temp-sensitive pharma (when provided) | Continuous record; excursions documented if present |
| **Chain-of-Custody Document** | Pharmaceutical shipments (Nexus Aurea SOP) | Signature chain complete; dates/times consistent; no unaccounted gaps |
| **Certificate of Analysis / Conformance** | When provided by shipper | Product name, lot, quantity match shipping paper; issued by authorized party |

---

## FINDING STATUS DEFINITIONS

| Status | Meaning |
|---|---|
| ✅ **Pass** | Element is present, correct, and consistent with cited regulation. |
| ❌ **Fail** | Element is missing, incorrect, or inconsistent. Requires immediate flagging for human review. |
| ⚠️ **Warning** | Element is present but contains an anomaly or ambiguity. Human verification required before release. |
| ❓ **Unable to Verify** | Required document or data element was not provided or is not legible. Cannot confirm compliance or non-compliance. |
| ➖ **Not Applicable** | Rule or check does not apply to this shipment type, mode, or material. |

---

*This library is a working reference only. All findings produced using this library are DRAFT. Human review is required before any action is taken. This document will be updated as additional regulatory sources (IATA DGR, IMDG, ICAO, WHO) are integrated.*

*Source: 49 CFR, ecfr.gov — accessed September 9, 2026*
