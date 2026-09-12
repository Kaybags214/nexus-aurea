# Nexus Aurea — Compliance Audit

- **Audit date:** 2026-09-07
- **Auditor:** `dgd-check` skill (Nexus Aurea) — reviewed by Kenya Bagwell
- **Document type(s):** Shipper's Declaration for Dangerous Goods (column format)
- **Governing reference(s):** `compliance-auditor/standards-of-precedence.md`,
  `dgr/05-checklists/dg-checklist-non-radioactive-reference.md`
- **Shipper:** Apex INC., 654 Stone Lane, Stafford VA 22554
- **Consignee:** ABC Flyers, 754 Rockaway Lane, Blacksburg VA 24060
- **Origin → Destination:** BWI → ATL (US domestic)
- **Commodity / DG:** UN3077 Environmentally hazardous substance, solid, n.o.s. (copper sulfate)
- **Source:** operator practice declaration dated 9/3/2026. Not a live shipment.

### Classification block — correct, including the part most often missed

| Column | Value | Assessment |
|---|---|---|
| UN number | UN3077 | ✅ |
| Proper shipping name | Environmentally hazardous substance, solid, n.o.s. **(copper sulfate)** | ✅ |
| Class | 9 | ✅ |
| Subsidiary risk | *blank* | ✅ correctly blank |
| Packing group | III | ✅ correct for this entry |
| Quantity and packing | 1 fibreboard box (4G), 5 kg net | ✅ packaging described |
| Packing instruction | 956 | ⚠ see unverified |

**The technical name is correctly supplied in brackets.** UN3077 is an n.o.s. entry, and n.o.s.
entries require the technical name of the substance alongside the generic shipping name.
"(copper sulfate)" satisfies that. It is the single most commonly omitted element on n.o.s.
declarations and it is right here.

Shipment type correctly marked **non-radioactive**. Aircraft limitation shows passenger and
cargo, cargo-aircraft-only left clear.

### 🔴 Critical findings

- **[C-1] The declaration is unsigned.** Signature field empty. **Standard:** IATA DGR 67th ed.
  certification. **Fix:** must be signed. Not correctable in place.
- **[C-2] Air Waybill number absent.** **Standard:**
  `dg-checklist-non-radioactive-reference.md`, Documentation. **Fix:** enter the AWB number.

### 🟡 Major findings

- **[M-1] Signatory title absent.**
- **[M-2] Place of signing absent.** Only the date, 9/3/2026.
- **[M-3] Emergency telephone has no country code.** Confirm 24-hour monitoring.

### 🟢 Minor findings

- **[m-1]** "Emergancy Contact" — spelling.

### Cannot verify

- **PI 956 and its quantity limit** for Class 9 PG III solid on passenger aircraft. No DGR 67th
  ed. copy available to this run. 5 kg net is plausible but unconfirmed.
- **Whether copper sulfate is the correct technical name** for the material actually shipped,
  and whether it meets the environmentally hazardous criteria for UN3077. The declaration is
  internally consistent; the classification decision itself cannot be checked from the document.
- **Red hatched border and form condition.**
- **State and operator variations** for the BWI–ATL domestic leg; 49 CFR governs the ground legs.

### Check 6 — agreement with the AWB: NOT PERFORMED

No Air Waybill submitted, and the declaration's own AWB field is blank (C-2).

### Final verdict

- [ ] ✅ PASS
- [ ] ⏸️ HOLD FOR CORRECTION
- [x] ⛔ **REJECT — DO NOT TENDER**

**Reason:** Unsigned. Classification is clean; the only substantive defects are the signature
and the missing AWB number.

---

*Research/operations support, not legal advice or a certifying signature. Practice document;
contact number redacted in this record.*
