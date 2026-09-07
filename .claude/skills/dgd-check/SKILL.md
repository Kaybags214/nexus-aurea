---
name: dgd-check
description: Check a Shipper's Declaration for Dangerous Goods for completeness, correct classification, packing instruction, aircraft limitation, emergency contact and signature, and agreement with the Air Waybill. Use when reviewing a DGD, Shipper's Declaration, dangerous goods declaration, or any air shipment carrying a UN number that requires declared dangerous goods.
---

# Shipper's Declaration for Dangerous Goods

One job: audit the DGD. The AWB belongs to `awb-review`; dry ice specifics belong to
`dry-ice-un1845`. Where this document and the AWB disagree, the DGD outranks the AWB — but the
physical package outranks both.

Governed by `compliance-auditor/standards-of-precedence.md`. **State variations for origin,
transit and destination all apply, and stack with operator variations.** A shipment that
satisfies IATA DGR but violates a destination state variation still fails.

## Before you start

Read `dgr/05-checklists/dg-checklist-non-radioactive-reference.md`. Where it and this file
differ, it wins.

## 1. Classification block — line by line

For each entry in Nature and Quantity of Dangerous Goods:

- [ ] **UN or ID number**, correct for the substance
- [ ] **Proper shipping name**, matching the UN number exactly — not a trade name, not a
      paraphrase, and technical name in brackets where the entry requires one
- [ ] **Class or division**, with subsidiary risk shown where one applies
- [ ] **Packing group**, where the entry has one
- [ ] **Quantity and type of packing** — net quantity per package with unit, and the packaging
      described
- [ ] **Packing instruction number**, and it is the right one for this UN number, aircraft type
      and quantity — **verify against the operator's own DGR 67th ed. copy**, not from memory
- [ ] **Authorization** field completed where a special provision, state approval or exemption
      applies

Quantity per package over the packing instruction limit is Critical. So is a proper shipping
name that does not match its UN number.

## 2. Aircraft limitation
- [ ] The shipment type line shows exactly one of passenger-and-cargo aircraft or cargo aircraft
      only — the non-applicable one **deleted**, not left standing
- [ ] Where the entry is CAO, the AWB handling information says so too
- [ ] Where quantities exceed the passenger-aircraft column, CAO is selected

Both lines left intact is a Critical finding. It leaves acceptance unable to determine what was
declared.

## 3. Header and routing
- [ ] Shipper name and full address
- [ ] Consignee name and full address
- [ ] Air Waybill number, matching the AWB itself
- [ ] Page **n of n** completed on every page
- [ ] Airport of departure and airport of destination

## 4. Emergency and certification
- [ ] 24-hour emergency response telephone number present, with country code, and monitored
- [ ] Additional handling information completed where required
- [ ] Certification statement intact and unaltered
- [ ] Name and title of signatory
- [ ] Place and date
- [ ] Signature present

An unsigned DGD is Critical. A missing or unreachable 24-hour number is Critical.

## 5. Form condition
- [ ] Printed with the required red hatched border on both vertical edges
- [ ] Legible, in English (plus any required additional language)
- [ ] **No erasures or overwriting.** Amendments must be made and signed by the same person who
      signed the declaration; anything scratched out and written over is Critical and needs a
      fresh form, not a correction in place
- [ ] Sufficient copies provided for the operator

## 6. Agreement with the AWB

| Check | DGD | AWB | Match? |
|---|---|---|---|
| Shipper | | | |
| Consignee | | | |
| AWB number | | | |
| UN number(s) / PSN | | | |
| Number of packages | | | |
| Net quantity per package | | | |
| Aircraft limitation | | | |

Any disagreement here is Critical. This is the pairing acceptance checks first.

## What you may not do

- Do not supply a packing instruction, PSN or UN number you are not certain of. Say
  **"cannot verify — confirm against DGR 67th ed."** and leave it open.
- Do not treat an unsigned or altered form as correctable in the report. The fix is a new form.
- Do not sign, certify, or clear. You flag and correct; a qualified person signs before tender.
- Do not issue PASS while any Critical is open.

## Output

Severity-grouped findings per `compliance-auditor/audit-report-template.md`, each naming its
standard and the precedence level it came from, then the corrected declaration with
`[CORRECTED: was X → now Y]` and `[NEEDS INPUT: …]`, then the verdict.

Append what you learned to `learnings.md` in this folder.
