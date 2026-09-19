# Nexus Aurea — Compliance Audit

- **Audit date:** 2026-09-07
- **Auditor:** `dgd-check` skill (Nexus Aurea) — reviewed by Kenya Bagwell
- **Document type(s):** Shipper's Declaration for Dangerous Goods (column format, fillable)
- **Governing reference(s):** `compliance-auditor/standards-of-precedence.md`,
  `dgr/05-checklists/dg-checklist-non-radioactive-reference.md`,
  `pharma/03-biological-substances/biological-substances-reference.md`
- **Shipper:** Apex INC., 654 Stone Lane, Stafford VA 22554
- **Consignee:** ABC Flyers, 456 Rockaway Lane, Blacksburg VA 24060
- **Origin → Destination:** IAD → ATL (US domestic)
- **Mode:** Air
- **Commodity:** Dry ice + biological substance
- **Dangerous goods involved:** UN1845; second entry declared as UN3393 — see C-1
- **Source:** practice declaration, dated 9/3/2026. Training document, not a live shipment.

### Extracted fields

| Field | Value read | Expected | OK? |
|---|---|---|---|
| Entry 1 UN | UN1845 | UN1845 | ✅ |
| Entry 1 PSN | Carbon Dioxide (solid) | "Carbon dioxide, solid" or "Dry ice" | ❌ |
| Entry 1 Class | 9 | 9 | ✅ |
| Entry 1 Packing group | II | *none — dry ice has no PG* | ❌ |
| Entry 1 Quantity | 2 packaing 1.5 kg net 3.0 kg | qty + packaging type | ❌ |
| Entry 1 PI | 954 | 954 | ✅ |
| Entry 2 UN | **UN3393** | UN3373 | ❌ |
| Entry 2 PSN | Biological Substances category B | "Biological substance, Category B" | ❌ |
| Entry 2 Class | 6.2 | 6.2 *(matches UN3373, not UN3393)* | ⚠ |
| Entry 2 Packing group | I | *none under PI 650* | ❌ |
| Entry 2 Quantity | 2 Glass Container 0.5 L net 1.0 L | qty + triple packaging described | ❌ |
| Entry 2 PI | 650 | 650 | ✅ |
| Air Waybill No | *blank* | AWB number | ❌ |
| Page / of pages | 1 of 1 | — | ✅ |
| Shipment type | **RADIOACTIVE marked; non-radioactive blank** | non-radioactive | ❌ |
| Aircraft | Passenger and Cargo marked; CAO blank | one selected | ✅ |
| Emergency contact | "Emergancy Contact 703-XXX-XXXX" | 24-hr number with country code | ❌ |
| Name / title | Kenya Bagwell | name **and title** | ❌ |
| Place / date | 9/3/2026 | place **and** date | ❌ |
| Signature | *blank* | signed | ❌ |

### 🔴 Critical findings — shipment does NOT tender until fixed

- **[C-1] Wrong UN number on the biological entry.** The declaration shows **UN3393** against
  the proper shipping name "Biological Substances category B". Category B is **UN3373**.
  UN3393 is an organometallic substance, solid, pyrophoric — Class 4.2, a different hazard
  entirely. The document contradicts itself: the class column shows 6.2, which matches UN3373
  and not UN3393. **Standard:** proper shipping name must match the UN number — precedence
  level 3, IATA DGR 67th ed.; `pharma/03-biological-substances/biological-substances-reference.md`
  Step 1. **Fix:** correct to `UN3373`. Almost certainly a 3373 → 3393 transposition.

- **[C-2] Shipment declared RADIOACTIVE.** The "radioactive" shipment-type line is marked and
  the "non-radioactive" line is left blank. Neither dry ice nor a biological substance is
  radioactive material. **Standard:** IATA DGR 67th ed. shipment-type declaration.
  **Fix:** mark non-radioactive and clear the radioactive line. Note the same fields are filled
  correctly on the UN1830 and UN3077 declarations in this set — this one is reversed.

- **[C-3] The declaration is unsigned.** The signature field is empty.
  **Standard:** IATA DGR 67th ed. certification requirements; `dgd-check` check 4.
  **Fix:** a declaration cannot be corrected into a signed one — it must be signed by a person
  with current DG training before tender.

- **[C-4] Air Waybill number absent.** The field is blank, so the declaration cannot be tied to
  any transport document. **Standard:** `dg-checklist-non-radioactive-reference.md`,
  Documentation. **Fix:** enter the AWB number.

### 🟡 Major findings — correct before tender

- **[M-1] Packing group "II" assigned to UN1845.** Dry ice has no packing group.
  **Standard:** `dgr/03-shipper-declarations/completed-example-reference.md` — "no packing
  group assigned to dry ice". **Fix:** leave blank.
- **[M-2] Packing group "I" assigned to the biological entry.** Category B under PI 650 carries
  no packing group. **Standard:** `biological-substances-reference.md` Step 3.
  *Confirm against a DGR 67th ed. copy before citing as absolute.* **Fix:** leave blank.
- **[M-3] Entry 1 proper shipping name deviates.** "Carbon Dioxide (solid)" — the DGR name is
  "Carbon dioxide, solid" (comma, not parentheses) or "Dry ice". **Fix:** use the exact name.
- **[M-4] Entry 2 proper shipping name deviates.** "Biological Substances category B" — the DGR
  name is "Biological substance, Category B": singular, comma, capital C. **Fix:** exact name.
- **[M-5] Packaging type not described on either entry.** "2 packaing" and "2 Glass Container"
  state a count but not the packaging. The other two declarations in this set do it correctly —
  "1 fibreboard box (4G)". For the Category B entry, triple packaging is required and none is
  described. **Standard:** `biological-substances-reference.md` Step 2.
  **Fix:** name the outer packaging and its specification.
- **[M-6] Emergency telephone number has no country code.** **Fix:** enter in international
  format. Also confirm the number is monitored 24 hours — not verifiable from the document.
- **[M-7] Signatory title absent.** A name is present, no title. **Fix:** add title.
- **[M-8] Place of signing absent.** Only the date, 9/3/2026, was entered. **Fix:** add place.
- **[M-9] A Shipper's Declaration is not required for this shipment.** Category B under PI 650
  requires no DGD, and dry ice as a refrigerant requires none either. **Standard:**
  `biological-substances-reference.md` Step 3 table — Category B, Shipper's Declaration:
  "Not required". Filing one over-declares the shipment as fully regulated DG and can cause
  acceptance to apply requirements that do not attach. **Fix:** confirm whether a declaration
  was intended. As a training exercise it is valid practice; as a real tender it should be an
  AWB entry instead.

### 🟢 Minor findings

- **[m-1]** "Emergancy Contact" — spelling. **Fix:** "Emergency".
- **[m-2]** "2 packaing" — spelling. **Fix:** "packages".

### Cannot verify

- **Red hatched border and form condition.** This audit read the PDF's form-field data, not a
  rendered page. Border, print quality and any alteration are **unverified — not findings of
  absence.**
- **PI 954 and PI 650 quantity limits.** No DGR 67th ed. copy was available to this run.
  1.5 kg dry ice per package and 0.5 L per glass container are plausible but unconfirmed.
- **Whether the emergency number is monitored 24 hours.**
- **State and operator variations.** IAD → ATL is US domestic; per `standards-of-precedence.md`
  §1, 49 CFR governs the US ground legs. No USG or operator variations were checked — no source
  was available to this run.

### Check 6 — agreement with the AWB: NOT PERFORMED

No Air Waybill was submitted, and the declaration's own AWB field is blank (C-4). This
declaration has **not** been reconciled against a transport document.

### Corrected version — the two entries

```
[CORRECTED: was "UN3393" → now "UN3373"]
[CORRECTED: was PG "II" (entry 1) → now blank — dry ice has no packing group]
[CORRECTED: was PG "I"  (entry 2) → now blank — no packing group under PI 650]
[CORRECTED: was "Carbon Dioxide (solid)" → now "Carbon dioxide, solid"]
[CORRECTED: was "Biological Substances category B" → now "Biological substance, Category B"]
[CORRECTED: shipment type — radioactive cleared, non-radioactive marked]

UN1845 | Carbon dioxide, solid | 9 |   | 2 x [NEEDS INPUT: packaging type],
        1.5 kg net each, 3.0 kg total | 954 |
UN3373 | Biological substance, Category B | 6.2 |   | 2 x [NEEDS INPUT: outer packaging,
        triple packaging per PI 650], 0.5 L net each, 1.0 L total | 650 |

[NEEDS INPUT: Air Waybill number]
[NEEDS INPUT: signatory title]
[NEEDS INPUT: place of signing]
[NEEDS INPUT: emergency number with country code]
```

### Final verdict

- [ ] ✅ PASS
- [ ] ⏸️ HOLD FOR CORRECTION
- [x] ⛔ **REJECT — DO NOT TENDER**

**Reason:** Unsigned, and declares a UN number for a pyrophoric Class 4.2 substance against a
Category B biological shipping name while marking the shipment radioactive. An unsigned form is
not correctable in place — a fresh, corrected declaration is required.

---

*Research/operations support, not legal advice or a certifying signature. A qualified person
signs before tender. Practice document; contact number redacted in this record.*
