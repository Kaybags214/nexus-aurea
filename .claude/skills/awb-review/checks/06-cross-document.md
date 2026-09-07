# Check 6 — Cross-document agreement

Build this table whenever more than one document is present.

| Check | AWB | Invoice | Packing list | DGD | Match? |
|---|---|---|---|---|---|
| Shipper | | | | | |
| Consignee | | | | | |
| Piece count | | | | | |
| Gross weight | | | | | |
| UN number / PSN | | | | | |
| Dry ice net kg | | | | | |
| AWB reference no. | | | | | |
| Goods description | | | | | |

## Severity

- Party mismatch, UN number mismatch, weight mismatch → **Critical**
- Description wording differs but describes the same goods → **Major**
- Formatting, abbreviation, letter case → **Minor**

## Resolving

Order of precedence for one shipment, per `standards-of-precedence.md` section 4:
physical package, DGD, AWB, commercial invoice, packing list.

Name which document is wrong and what it should say. Never edit two documents toward each
other to make them agree — one of them is correct, and the report must say which.

## Where only one document was submitted

Say so explicitly and mark the cross-document check as not performed. Do not present a
single-document review as if consistency were confirmed.
