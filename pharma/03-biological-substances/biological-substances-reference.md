# Biological Substances & Infectious Materials — Shipping Reference

Purpose: Field-by-field reference for reviewing shipments of blood, blood products, diagnostic
specimens, and infectious substances (the "bloodborne pathogens" lane). Original summary built from
IATA DGR Section 6.3 / PI 620 & PI 650, ICAO TI, 49 CFR 173.134/173.199, and OSHA Bloodborne
Pathogens Standard 29 CFR 1910.1030. Not a copy of any proprietary form.

## Step 1 — Classify the material correctly (this drives everything)

- **Category A — UN2814** (infectious to humans) / **UN2900** (infectious to animals): capable of
  causing permanent disability or life-threatening/fatal disease. Proper shipping name: "Infectious
  substance, affecting humans" / "...affecting animals". Packing Instruction **PI 620**.
- **Category B — UN3373**: an infectious substance not meeting Category A criteria. Proper shipping
  name: "Biological substance, Category B". Packing Instruction **PI 650**. This is the common
  diagnostic-specimen category.
- **Exempt human/animal specimen**: minimal likelihood of pathogens present — marked "Exempt human
  specimen" / "Exempt animal specimen", not regulated as DG (but still packed as triple packaging).
- **Genetically modified micro-organisms/organisms** — UN3245 where applicable.
- **Dry ice used as coolant** — still UN1845, declared separately (see `cold-chain/03-dry-ice/`).

## Step 2 — Triple packaging (required for A, B, and exempt)

- Primary receptacle (leak-proof, watertight) — for liquids, absorbent material between primary and
  secondary sufficient to absorb the entire contents.
- Secondary packaging (leak-proof, watertight).
- Rigid outer packaging with one surface ≥ 100 mm × 100 mm.
- Category A must use packaging certified to **UN Class 6.2 / PI 620 (P620)** and pass the drop test.
- Category B (PI 650): at least one surface of the outer package must display the UN3373 mark
  (diamond, side ≥ 50 mm); proper shipping name "Biological substance, Category B" next to it.

## Step 3 — Marks, labels, documentation

| Item | Category A (UN2814/2900) | Category B (UN3373) |
|------|--------------------------|---------------------|
| Hazard label | Class 6.2 Infectious Substance diamond | No 6.2 diamond; UN3373 mark only |
| UN mark | UN2814 / UN2900 next to PSN | UN3373 diamond mark |
| Shipper's Declaration (DGD) | **Required** | **Not required** |
| Air Waybill nature of goods | PSN + UN number | "Biological substance, Category B, UN3373" |
| Itemized list of contents | Required (inside secondary) | Recommended |
| 24-hr emergency contact | Required | Not required by DGR, good practice |
| Responsible person + phone | Required | Required on the outer package |

## Step 4 — Cold chain / OSHA overlap

- If shipped chilled/frozen with dry ice: add UN1845, net dry ice weight in **kg**, Class 9 handling,
  vented packaging (`cold-chain/03-dry-ice/`).
- Temperature-sensitive biologicals also carry a temp log — audit against `pharma/01-gdp-gmp/`.
- OSHA 29 CFR 1910.1030 governs the handling side (labeling of blood/OPIM containers as biohazard,
  handler training) — flag if internal handling documentation is absent.

## Review / practice checklist

- [ ] Classification correct (A vs B vs exempt) — the single most important call
- [ ] Correct UN number and proper shipping name for the classification
- [ ] Category A: DGD present, signed, PI 620 packaging certified; Category B: NO DGD, UN3373 mark present
- [ ] Triple packaging described; absorbent present for liquids
- [ ] Outer package ≥ 100 × 100 mm; UN3373 mark ≥ 50 mm side (Cat B)
- [ ] Responsible person name + 24-hr phone on the package
- [ ] Dry ice (if used) declared as UN1845 with net kg and Class 9 handling
- [ ] Shipper/consignee consistent across AWB, DGD (if any), and packing list
- [ ] Import permit / sender's permit present where the destination requires one

## Common findings

- 🔴 Category A shipment tendered without a Shipper's Declaration — Critical.
- 🔴 Infectious substance mis-classified as UN3373 when it meets Category A criteria — Critical.
- 🔴 No absorbent material for a liquid primary receptacle — Critical (leak risk).
- 🟡 UN3373 mark under 50 mm or missing proper shipping name beside it — Major.
- 🟡 Responsible-person phone number missing from outer package — Major.
- 🟢 Itemized content list omitted on a Category B shipment — Minor.

## Sources

- IATA DGR Infectious Substances program page: https://www.iata.org/en/programs/cargo/dgr/infectious-substances/
- 49 CFR 173.134 (Class 6.2 definitions): https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-C/part-173/subpart-D/section-173.134
- OSHA Bloodborne Pathogens 29 CFR 1910.1030: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1030
- WHO Guidance on regulations for the transport of infectious substances: https://www.who.int/publications/i/item/9789240010086
