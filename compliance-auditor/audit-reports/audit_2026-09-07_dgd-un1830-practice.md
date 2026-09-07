# Nexus Aurea — Compliance Audit

- **Audit date:** 2026-09-07
- **Auditor:** `dgd-check` skill (Nexus Aurea) — reviewed by Kenya Bagwell
- **Document type(s):** Shipper's Declaration for Dangerous Goods (column format)
- **Governing reference(s):** `compliance-auditor/standards-of-precedence.md`,
  `dgr/05-checklists/dg-checklist-non-radioactive-reference.md`
- **Shipper:** Apex INC., 654 Stone Lane, Stafford VA 22554
- **Consignee:** ABC Flyers, 754 Rockaway Lane, Blacksburg VA 24060
- **Origin → Destination:** IAD → ATL (US domestic)
- **Commodity / DG:** UN1830 Sulphuric acid, Class 8, PG II
- **Source:** operator practice declaration dated 9/3/2026. Not a live shipment.

### Classification block — correct

| Column | Value | Assessment |
|---|---|---|
| UN number | UN1830 | ✅ |
| Proper shipping name | Sulphuric acid with more than 51% acid | ✅ matches UN1830 |
| Class | 8 | ✅ |
| Subsidiary risk | *blank* | ✅ correctly blank |
| Packing group | II | ✅ correct for this entry |
| Quantity and packing | 1 fibreboard box (4G), 1 inner bottle, 0,5 L net | ✅ packaging described |
| Packing instruction | 851 | ⚠ see unverified |

**All four classification columns agree with each other.** UN number, shipping name, class and
packing group describe the same substance. Packaging is properly identified by type and
specification code — this is the standard the other declarations in this set should meet.

Shipment type is correctly marked **non-radioactive**. Aircraft limitation shows passenger and
cargo aircraft, with cargo-aircraft-only left clear — one line selected, as required.

### 🔴 Critical findings

- **[C-1] The declaration is unsigned.** Signature field empty. **Standard:** IATA DGR 67th ed.
  certification. **Fix:** must be signed by a person with current DG training. Not correctable
  in place — a signed form is required.
- **[C-2] Air Waybill number absent.** **Standard:**
  `dg-checklist-non-radioactive-reference.md`, Documentation. **Fix:** enter the AWB number so
  the declaration ties to a transport document.

### 🟡 Major findings

- **[M-1] Signatory title absent.** Name present, no title.
- **[M-2] Place of signing absent.** Only the date, 9/3/2026.
- **[M-3] Emergency telephone has no country code.** **Fix:** international format. Confirm the
  number is monitored 24 hours.
- **[M-4] Inner packaging material not stated.** "1 inner bottle" does not say what the bottle
  is made of. Sulphuric acid above 51% requires an inner compatible with the substance.
  **Standard:** `dg-checklist-non-radioactive-reference.md`, Packing — inner packaging
  compatible with the substance. **Fix:** name the material.

### 🟢 Minor findings

- **[m-1]** "Emergancy Contact" — spelling.
- **[m-2]** Quantity uses a comma decimal separator, "0,5 L", on a US domestic declaration where
  the rest of the set uses a period. Not an error; worth making consistent to avoid a reader
  taking "0,5" for five.

### Cannot verify

- **PI 851 and its quantity limit for Class 8 PG II on passenger aircraft.** No DGR 67th ed.
  copy available to this run. 0,5 L net is plausible but unconfirmed. Confirm both the packing
  instruction number and the limit.
- **Red hatched border and form condition** — form-field data was read, not a rendered page.
- **State and operator variations** for the IAD–ATL domestic leg. Per
  `standards-of-precedence.md` §1, 49 CFR governs the US ground legs.
- Whether the emergency number is monitored 24 hours.

### Check 6 — agreement with the AWB: NOT PERFORMED

No Air Waybill submitted, and the declaration's own AWB field is blank (C-2).

### Final verdict

- [ ] ✅ PASS
- [ ] ⏸️ HOLD FOR CORRECTION
- [x] ⛔ **REJECT — DO NOT TENDER**

**Reason:** Unsigned. The classification is sound and would otherwise support a HOLD, but an
unsigned declaration cannot be corrected in place.

---

*Research/operations support, not legal advice or a certifying signature. Practice document;
contact number redacted in this record.*
