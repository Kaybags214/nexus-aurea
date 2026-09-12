# Check 5 — Agreement with the AWB and packing list

| Check | Invoice | AWB | Packing list | Match? |
|---|---|---|---|---|
| Shipper / seller | | | | |
| Consignee / buyer | | | | |
| Goods description | | | | |
| Piece count | | | | |
| Gross weight | | | | |
| Net weight | | | | |
| Lot / batch number | | | | |
| Invoice reference | | | | |
| Declared value | | | | |

## Severity

- Party mismatch → **Critical**
- Value on the invoice contradicting the AWB declared value for customs → **Critical**
- Lot number mismatch → **Critical**, and cross-refer to `coa-review`
- Piece or weight mismatch → **Critical**
- Description differs in wording but describes the same goods → **Major**

## Resolving

Per `standards-of-precedence.md` section 4 within one shipment: physical package, DGD, AWB,
commercial invoice, packing list. The invoice outranks the packing list on value and
classification; the AWB outranks the invoice on transport facts.

Name which document is wrong. Never edit two toward each other.

## Where only the invoice was submitted

Say so and mark this check not performed. An invoice reviewed alone has not been reconciled to
the shipment, and the report must not read as though it had been.
