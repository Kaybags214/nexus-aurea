---
name: awb-review
description: Review an Air Waybill for completeness and internal consistency — 11-digit AWB number check digit, shipper and consignee, piece count, gross and chargeable weight, handling information, DG and dry ice references, and agreement with the invoice and packing list. Use when reviewing an AWB, air waybill, MAWB or HAWB, or when a shipment's transport document needs checking before tender.
---

# Air Waybill review

One job: audit the AWB itself and its agreement with the other documents in the same shipment.
Dry ice specifics belong to `dry-ice-un1845`; the Shipper's Declaration belongs to `dgd-check`.
Call those out as separate findings rather than duplicating their work here.

Governed by `compliance-auditor/standards-of-precedence.md`. Within one shipment the AWB
outranks the invoice and packing list, and is outranked by the DGD and by the physical package.

## 1. AWB number — run the check digit

Format is **3-digit airline prefix + 8-digit serial**, eleven digits total. The eighth digit of
the serial is a check digit:

> take the first 7 digits of the serial as a number, divide by 7, the remainder is the check digit

Worked example: serial `4471882`, `4471882 ÷ 7 = 638840 remainder 2`, so a valid AWB ends in `2`
— `020-4471 8822`. If the document reads `020-4471 8823`, the number is invalid on its face.

- [ ] Eleven digits present
- [ ] Check digit arithmetic passes — show your working in the finding
- [ ] Airline prefix matches the carrier named on the document
- [ ] The same AWB number appears on every other document that references it

A failed check digit is Critical. It is not a typo to be quietly corrected — it means the AWB
number on the paperwork does not exist, and the fix needs the real number from the carrier.

## 2. Parties and routing
- [ ] Shipper name **and full address** in box 1, not a name alone
- [ ] Consignee name and full address in box 2
- [ ] Issuing agent name and IATA code
- [ ] Airport of departure and airport of destination both named
- [ ] Requested routing / to-by carrier fields consistent with the named airports
- [ ] Shipper and consignee match the invoice and packing list exactly — an abbreviated or
      truncated name is a Major finding, a different party is Critical

## 3. Pieces and weight
- [ ] Number of pieces / RCP stated
- [ ] Gross weight stated with its unit (kg or lb) — the unit must be explicit
- [ ] Rate class and chargeable weight present
- [ ] Chargeable weight is not less than gross weight
- [ ] Piece count agrees with the packing list; if it does not, the physical count governs and
      the packing list is what gets corrected

## 4. Nature and Quantity of Goods
- [ ] Goods described in plain terms, not just a commodity code
- [ ] Dangerous goods referenced where the shipment contains them, with UN number and PSN
- [ ] Dry ice entry present where used as a refrigerant, with net kg per package
- [ ] Temperature range shown for temperature-controlled product
- [ ] Description does not contradict the invoice goods description

## 5. Handling information and declarations
- [ ] Handling information carries any DG, cold-chain, or aircraft-limitation instruction
- [ ] "Cargo Aircraft Only" indicated where the DG requires it
- [ ] Shipper's certification box signed
- [ ] Carrier execution box has place, date and signature
- [ ] Declared value for carriage and for customs completed, or "NVD" / "NCV" entered — a blank
      is a Major finding, not a minor one

## 6. Cross-document table

| Check | AWB | Invoice | Packing list | DGD | Match? |
|---|---|---|---|---|---|
| Shipper | | | | | |
| Consignee | | | | | |
| Piece count | | | | | |
| Gross weight | | | | | |
| UN number / PSN | | | | | |
| Dry ice net kg | | | | | |
| AWB reference no. | | | | | |

## What you may not do

- Do not infer a field because it is usually present. Blank is a finding; illegible is
  **"cannot verify from image"**.
- Do not silently normalise a name or address to make two documents agree. The mismatch is the
  finding.
- Do not issue a PASS while any Critical is open.

## Output

Severity-grouped findings per `compliance-auditor/audit-report-template.md`, each naming its
standard, then the corrected AWB with `[CORRECTED: was X → now Y]` and `[NEEDS INPUT: …]` tags,
then a one-line verdict.

Append what you learned to `learnings.md` in this folder.
