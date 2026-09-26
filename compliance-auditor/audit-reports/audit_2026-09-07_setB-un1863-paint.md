# Nexus Aurea — Compliance Audit

- **Audit date:** 2026-09-07
- **Auditor:** `dgd-check` skill (Nexus Aurea) — reviewed by Kenya Bagwell
- **Document type(s):** Shipper's Declaration for Dangerous Goods **and** Air Waybill (handwritten)
- **Governing reference(s):** `compliance-auditor/standards-of-precedence.md`,
  `dgr/05-checklists/dg-checklist-non-radioactive-reference.md`
- **Shipper:** Nexus Aurea Inc., 456 Rockway Ln., Blacksburg VA 24060
- **Consignee:** ABC Logistics, 654 Stone Ln., Stafford VA 22555
- **Origin → Destination:** IAD (Dulles) → ATL (Hartsfield-Jackson Atlanta)
- **Commodity / DG:** UN1863 declared, "Paint related material", Class 3, PG II, 1 steel drum × 60 L
- **Source:** operator practice document set. Not a live shipment.

> **Check 6 was performed.** This is the first submission carrying both a declaration and its
> matching Air Waybill. That check found the most serious defect in the set.

### 🔴 Critical findings — shipment does NOT tender until fixed

- **[C-1] The declaration and the Air Waybill contradict each other on aircraft limitation.**
  - Declaration: **PASSENGER AND CARGO AIRCRAFT** (cargo-aircraft-only deleted)
  - Air Waybill handling information: **"Dangerous Goods as per attached Shipper's Declaration —
    Cargo Aircraft only (CAO)"**

  These cannot both be true. **Standard:** `dgd-check` check 3 and check 6;
  `standards-of-precedence.md` §4. **Why it is Critical:** acceptance reads the AWB, but the
  loading decision follows the declaration. A package barred from a passenger aircraft can be
  loaded onto one on the strength of whichever document is read first.

  **Which document is wrong is NOT established, and no correction is prescribed.**

  An earlier version of this finding said the quantity showed the AWB was right and the
  declaration wrong, and instructed the shipper to alter the declaration. That was withdrawn on
  review, for two reasons:

  - It rested on 60 L being "above any plausible passenger-aircraft limit" — a limit that was
    never verified. `skill-contract.md` rule 3 forbids resting a finding on a remembered figure,
    and a prescribed correction is the strongest form of resting on one.
  - It contradicted the standard it cited. `standards-of-precedence.md` §4 places the Shipper's
    Declaration **above** the Air Waybill. Absent physical evidence from the package, that order
    points the opposite way to the conclusion drawn.

  **Fix:** do not tender. Establish, in this order: (1) the Class 3 PG II passenger-aircraft
  quantity limit for this packing instruction in the DGR 67th ed., together with any state or
  operator variation on the routing; (2) what is physically on the drum — the package marking and
  whether a Cargo Aircraft Only label is affixed. Whichever document those two facts contradict
  is the one to correct. Until then the shipment is held on the contradiction itself, which is
  disqualifying regardless of which side is at fault.

- **[C-2] The declaration is unsigned.** Signature box empty.
  **Standard:** IATA DGR 67th ed. certification; `dgd-check` check 4.
  **Fix:** not correctable in place — a signed declaration is required.

- **[C-3] Date of signing is blank.** The certification carries neither date nor place.
  **Standard:** `dgd-check` check 4. **Fix:** complete on the replacement form.

- **[C-4] The UN number and proper shipping name pairing requires verification, and there is
  specific reason to doubt it.** The declaration reads **UN1863** against
  **"PAINT RELATED MATERIAL"**.

  My understanding is that paint related material is **UN1263**, and that UN1863 is
  *Fuel, aviation, turbine engine*. Both are Class 3 and both can carry PG II — which is exactly
  why the class and packing-group columns do not flag it. **Per `skill-contract.md` rule 3 this
  is not asserted**, and it is logged as unverified.

  **This is the same shape as the UN3373 → UN3393 error on the other declaration:** a
  transposed digit inside a valid-looking UN number, where the surrounding columns are
  compatible with both readings and so conceal it.

  **Fix:** verify the pairing against the DGR 67th ed. alphabetical list before this form is
  used. If paint is intended, the UN number, and possibly the packing instruction, change.

### 🟡 Major findings

- **[M-1] Place of signing absent.**
- **[M-2] Packaging specification not stated.** "1 Steel Drum × 60 L" gives the type but no UN
  specification marking. Your own UN1830 and UN3077 declarations do this correctly —
  "1 fibreboard box **(4G)**". **Fix:** add the specification code for the drum.
- **[M-3] Packing instruction 364 requires verification** for this UN number, aircraft type and
  quantity. Unverified — no DGR copy available to this run. Note that PI and aircraft limitation
  are linked: resolving C-1 may change the correct PI.
- **[M-4] Air Waybill number check digit.** `123 4744 667x` — the arithmetic:
  `4744667 ÷ 7 = 677809 remainder 4`, so a valid number ends **6674**. The final digit could not
  be resolved with confidence from the photograph on either document.
  **Fix:** confirm the last digit on both, confirm they match each other, and confirm it is 4.

### 🟢 Minor findings

- **[m-1]** Destination named inconsistently — "Hartsfield-Jackson Atlanta" on the declaration,
  "ATL/Atlanta" on the AWB. Same airport; make the form consistent.
- **[m-2]** Shipper postcode on the declaration is overwritten. On a handwritten form an
  overwritten field in the header is worth rewriting cleanly.

### Noted, belonging to `awb-review`

- **The signature is in the wrong box.** "Signature of Issuing Carrier or its Agent" is signed
  *Nexus Aurea Inc., K. Bagwell* — but Nexus Aurea is the **shipper** on this AWB. Meanwhile
  "Signature of Shipper or his Agent" is blank. The shipper cannot execute as the issuing
  carrier.
- **Gross weight appears blank** on the AWB. 60 L of liquid has substantial weight.
- **"ALL CAPS" appears in quotation marks** inside Nature and Quantity of Goods — a note to
  self left on the document.
- Executed-on date and place both blank.

### Repeating-defect pattern — across all four declarations audited

Per `skill-contract.md`, defects that repeat across a submitter's documents are reported once
as a pattern.

| Defect | Typed set (3 forms) | This form | Status |
|---|---|---|---|
| No Air Waybill number | 3 of 3 | ✅ present | **fixed** |
| No signatory title | 3 of 3 | ✅ "DGD specialist" | **fixed** |
| Emergency number without country code | 3 of 3 | ✅ "+1 888 325 2791" | **fixed** |
| **Unsigned** | 3 of 3 | ❌ still unsigned | **persists — 4 of 4** |
| **No place of signing** | 3 of 3 | ❌ still absent | **persists — 4 of 4** |
| Date of signing | present on 3 | ❌ now also blank | **regressed** |

**Three of the five repeating defects are fixed.** The certification block is the one that has
not moved: no signature and no place on any of the four, and this form drops the date as well.
That block is the remaining habit, and it is what makes every one of these forms a REJECT rather
than a HOLD.

### Cannot verify

- The UN number / proper shipping name pairing (C-4) and PI 364 (M-3) — no DGR 67th ed. copy.
- Passenger-aircraft quantity limit for Class 3 PG II — the reasoning under C-1 depends on it.
- Final digit of the AWB number on both documents (M-4) — photograph legibility.
- Red hatched border, package marking, Cargo Aircraft Only label — not visible in the images.
- State and operator variations for the IAD–ATL domestic leg; 49 CFR governs the ground legs.

### Final verdict

- [ ] ✅ PASS
- [ ] ⏸️ HOLD FOR CORRECTION
- [x] ⛔ **REJECT — DO NOT TENDER**

**Reason:** The declaration and Air Waybill contradict each other on aircraft limitation, the
declaration is unsigned and undated, and the UN-number-to-shipping-name pairing is in doubt.

---

*Research/operations support, not legal advice or a certifying signature. A qualified person
signs before tender. Practice document set.*
