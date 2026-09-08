# Standards of Precedence

Purpose: The order-of-precedence the auditor applies when two rules disagree. Every finding must
cite which level it comes from. When a stricter level applies, it wins — you never relax a
requirement because a lower level allows it. This is the compliance equivalent of the "Standing
rules" in `market-watch/n8n-analysis-prompt.md`.

> **Golden rule: the strictest applicable requirement governs.** Regulation, operator variation,
> and state variation stack — the shipment must satisfy all of them at once, not just the base rule.

---

## 1. Dangerous Goods by air (DGD, AWB handling, dry ice, lithium, biologicals)

Order of precedence, highest first:

1. **State variations** (origin, transit, AND destination country variations) — e.g. `USG`, `CAG`.
2. **Operator variations** (the specific airline's published variations) — e.g. `FXG`, `LHG`.
3. **IATA DGR, 67th Edition** (the edition Kenya is certified on) — the working ruleset.
4. **ICAO Technical Instructions** — the legal source IATA DGR is built on; IATA is equal-or-stricter.
5. **49 CFR (US DOT/PHMSA)** — governs the US ground legs and US domestic movement.

Rule of thumb: **IATA DGR is the day-to-day authority for air, but a state or operator variation
that is stricter overrides it.** If IATA and 49 CFR conflict on a US domestic ground leg, 49 CFR
governs that leg.

## 2. Cold chain / pharma temperature and quality (GDP/GMP, temp logs, CoA, excursions)

1. **The product's own label / marketing authorization storage condition** (e.g. "store 2–8 °C").
   This is the floor — never widen it.
2. **Destination-country GDP/GMP regulation** (e.g. EU GDP Guidelines 2013/C 343/01; FDA 21 CFR
   210/211 for US drug GMP).
3. **IATA CEIV Pharma / IATA Temperature Control Regulations (TCR)** for the air-transport leg.
4. **WHO TRS 961 Annex 9 / USP <1079>** as supporting good-practice references.
5. **Customer SOP / quality agreement**, when stricter than the above.

Rule of thumb: **the narrowest temperature range and the strictest retention/documentation
requirement win.** A CoA or temp log that meets IATA but violates the product label fails.

## 3. Customs / trade documentation (commercial invoice, packing list, entry)

1. **Destination-country customs law** (for US import: 19 CFR; CBP rulings).
2. **Origin-country export controls** (e.g. US EAR/OFAC/ITAR where applicable).
3. **Incoterms 2020** — governs cost/risk split; must be internally consistent with the invoice.
4. **Carrier / forwarder documentation requirements.**

Rule of thumb: **the destination customs authority has final say on classification and valuation.**
HS code and declared value must satisfy the import country, not just the shipper's convenience.

## 4. When documents in one shipment disagree with each other

The physical package and the most-regulated document win, in this order:

1. **What is actually on/in the package** (marks, labels, weighed quantity) — reality beats paper.
2. **Shipper's Declaration for Dangerous Goods** (for anything hazmat-related).
3. **Air Waybill / Bill of Lading** (the transport contract).
4. **Commercial Invoice** (value/classification).
5. **Packing List** (piece/weight detail).

Example: if the packing list says 4 cartons and the AWB says 3, and the pieces on the dock are 3,
the finding is "packing list overstates piece count — correct packing list to 3," not the reverse.

## 5. Severity mapping (how precedence becomes a flag)

- **🔴 Critical** — violates level 1–3 of the applicable DG chain, the product-label temperature, or
  destination customs law; or a mismatch that would get the shipment rejected, held, or make it
  unsafe/illegal to tender. Shipment does **not** go until fixed.
- **🟡 Major** — violates a lower-precedence rule, an internal document-to-document mismatch that is
  correctable before tender, or a missing non-safety field. Fix before tender.
- **🟢 Minor** — formatting, legibility, best-practice, or advisory items that don't block the
  shipment but should be cleaned up.

Every flag names the level it came from (e.g. "Critical — IATA DGR 67th ed., dry ice net weight
must be in kg; State variation USG also applies").
