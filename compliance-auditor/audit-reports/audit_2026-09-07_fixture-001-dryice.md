# Nexus Aurea — Compliance Audit

- **Audit date:** 2026-09-07
- **Auditor:** `dry-ice-un1845` skill (Nexus Aurea) — reviewed by Kenya Bagwell
- **Document type(s):** Air Waybill, Packing List, Commercial Invoice (extracts)
- **Governing reference(s):** `compliance-auditor/standards-of-precedence.md`,
  `audit-lab/dry-ice-un1845/dry-ice-review-checklist.md`
- **Shipper:** Meridian Biologics, Richmond VA
- **Consignee:** Klinik Zentrallabor GmbH, Frankfurt
- **Origin → Destination:** RIC → JFK → FRA
- **Mode:** Air
- **Commodity:** Temperature-controlled pharmaceutical product
- **Temperature range:** +2 °C to +8 °C (per invoice and packing list)
- **Dangerous goods involved:** UN1845 dry ice, as refrigerant only
- **Source:** `audit-lab/test-fixtures/FIXTURE-001-awb-dryice.md` — **synthetic test fixture**

### Check 1 — Is a Shipper's Declaration required?

**Concluded: no DGD required.** Dry ice is used solely as a refrigerant for non-dangerous
contents. Evidence: the invoice and packing list describe an ordinary +2/+8 °C pharmaceutical
product, 120 vials; no UN number, class, division or proper shipping name appears for the
product itself anywhere in the set.

**The absence of a DGD is therefore correct and is not raised as a finding.**

One verification point, not a finding: the shipper name "Meridian Biologics" and a vialled
product leave open whether the contents are a biological substance. Nothing in the document set
classifies them as UN3373 or UN2814. If they are, PI 650 still requires no declaration, but the
packaging and marking requirements change. **Confirm the product's classification with the
shipper** before tender.

### Extracted fields

| Field | Value read | Expected | Source | OK? |
|---|---|---|---|---|
| UN number | UN1845 | UN1845 | AWB Nature & Quantity | ✅ |
| Proper shipping name | DRY ICE | "Dry ice" or "Carbon dioxide, solid" | AWB | ✅ |
| Class | *not shown* | 9 | AWB | ❌ |
| Dry ice quantity | 12 LBS | net kg **per package** | AWB | ❌ |
| Packages containing dry ice | *not shown* | count | AWB | ❌ |
| Dry ice per carton | 4 kg | — | Packing list | — |
| Cartons | 4 | — | Packing list | — |
| Pieces (RCP) | 3 | — | AWB | ❌ |
| Temperature instruction | "Keep cool. Perishable." | +2 °C to +8 °C | AWB handling info | ❌ |
| Aircraft type | *not determinable* | passenger or CAO | AWB | ❌ |
| Package marking / labels | *cannot verify from image* | — | — | — |

### 🔴 Critical findings — shipment does NOT tender until fixed

- **[C-1]** Dry ice quantity stated in **pounds only** — "12 LBS". **Standard:** IATA DGR 67th
  ed., net quantity of dry ice required in kilograms; precedence level 3.
  **Fix:** restate in kg.
- **[C-2]** Dry ice shown as a **shipment total, with no net weight per package**.
  **Standard:** IATA DGR 67th ed. — net quantity per package. **Fix:** enter per-package kg.
- **[C-3]** **Number of packages containing dry ice is not shown** in the AWB entry.
  **Standard:** IATA DGR 67th ed. AWB entry requirements. **Fix:** state the package count.
  With no DGD in this shipment, the AWB entry is the only declaration — there is no fallback
  document carrying this information.
- **[C-4]** **Dry ice quantity conflicts across documents.** AWB 12 lb ≈ 5.44 kg; packing list
  4 kg × 4 cartons = **16 kg**. Roughly a threefold discrepancy.
  **Standard:** `standards-of-precedence.md` §4 — document-to-document consistency.
  **Fix:** establish the true quantity by weighing before tender. This cannot be resolved on
  paper: the AWB outranks the packing list, but the physical package outranks both and has not
  been observed.
- **[C-5]** **Package count conflict.** AWB shows 3 pieces; packing list shows 4 cartons.
  **Standard:** `standards-of-precedence.md` §4. **Fix:** physical count governs; correct
  whichever document is wrong once counted. Compounds C-4 — the 16 kg figure assumes 4 cartons.

### 🟡 Major findings — correct before tender

- **[M-1]** **No temperature range in handling information.** "Keep cool. Perishable." for a
  product the invoice and packing list both state as +2/+8 °C.
  **Standard:** IATA CEIV Pharma / TCR; `standards-of-precedence.md` §2.
  **Fix:** enter "Maintain +2 °C to +8 °C".
- **[M-2]** **Class 9 not shown** in the AWB dry ice entry. **Standard:** IATA DGR 67th ed. AWB
  entry format — **verify the exact required entry format against the operator's DGR copy**
  before citing this as a hard requirement. **Fix:** include the class in the entry.
- **[M-3]** **Shipper address truncated on the AWB** — "1400 Innovation Dr, Richmond VA" against
  "1400 Innovation Drive, Suite 200, Richmond VA 23219" on the invoice and packing list. Suite
  and postal code dropped. **Standard:** `standards-of-precedence.md` §4.
  **Fix:** carry the full address onto the AWB.
- **[M-4]** **Aircraft type not determinable from the AWB.** Routing is RIC/AA → JFK/LH → FRA
  with no passenger/cargo-aircraft indication, so the correct PI 954 quantity column cannot be
  selected. **Fix:** state the aircraft type.

### Cannot verify

- **All package marking, labelling and venting (check 3).** This submission is a transcription,
  not photographs of the packages. Class 9 label, UN1845 marking, address marking, and whether
  the outer permits CO₂ release are **unverified — not findings of absence.** Request package
  photographs.
- **PI 954 quantity limit.** Cannot be checked: no per-package kg figure exists (C-2), the
  aircraft type is undetermined (M-4), and no DGR 67th ed. copy was available to this run.

### Cross-document consistency

| Check | AWB | Packing list | Invoice | Match? |
|---|---|---|---|---|
| Shipper | Truncated | Full | Full | ❌ |
| Consignee | Klinik Zentrallabor GmbH | Same | Same | ✅ |
| Packages w/ dry ice | Not stated | 4 | — | ❌ |
| Net kg per package | Not stated | 4 kg | — | ❌ |
| Total dry ice | ≈5.44 kg (12 lb) | 16 kg | — | ❌ |
| Piece count | 3 | 4 | — | ❌ |
| Temperature | "Keep cool" | 2–8 C | 2–8 C | ❌ |

### Noted, but belonging to other skills

Not audited here — passed to the skill that owns them:

- AWB number `020-4471 8823` — **check digit appears to fail**; `awb-review` ch.1 owns it
- Chargeable weight 38.0 kg is **below** gross weight 41.2 kg; `awb-review` ch.3
- Declared value for carriage is **blank** — neither a figure nor NVD; `awb-review` ch.5
- Invoice terms "CIF" on an air shipment, with no named place; `commercial-invoice-review` ch.3

### Corrected version — AWB entry

```
NATURE AND QUANTITY OF GOODS
  Pharmaceutical product, temperature controlled
  [NEEDS INPUT: UN1845, Dry ice, 9, <n> packages x <n> kg net each]
  [CORRECTED: was "UN1845 DRY ICE 12 LBS"]

HANDLING INFORMATION
  [CORRECTED: was "Keep cool. Perishable."
   now "Maintain +2 C to +8 C. Perishable. Contains dry ice."]

SHIPPER
  [CORRECTED: was "1400 Innovation Dr, Richmond VA"
   now "1400 Innovation Drive, Suite 200, Richmond VA 23219"]
```

The dry ice quantity is left as `[NEEDS INPUT]` deliberately. Two irreconcilable figures exist
and the correct one cannot be determined from paper — it must be weighed.

### Final verdict

- [ ] ✅ PASS
- [x] ⏸️ **HOLD FOR CORRECTION**
- [ ] ⛔ REJECT

**Reason:** Five Critical findings, including an unresolved threefold conflict in declared dry
ice quantity and a package count that does not agree between documents.

---

*Research/operations support, not legal advice or a certifying signature. A qualified person
signs before tender. Run against a synthetic fixture; no real shipment is described.*
