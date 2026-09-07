# Check 6 — Cross-document agreement

| Check | DGD (if any) | AWB | Invoice | Packing list | Match? |
|---|---|---|---|---|---|
| Shipper | | | | | |
| Consignee | | | | | |
| UN number | | | | | |
| Proper shipping name | | | | | |
| Packing instruction / section | | | | | |
| Number of packages | | | | | |
| Net quantity per package | | | | | |
| **Aircraft limitation** | | | | | |
| Watt-hours / lithium content | | | | | |

## Severity

- **Aircraft limitation mismatch → Critical.** See check 3. This is the row that matters most
  on this commodity.
- UN number or packing instruction mismatch → Critical
- Package count or quantity mismatch → Critical
- Party mismatch → Critical
- Description wording differs but describes the same arrangement → Major

## Resolving

Per `standards-of-precedence.md` §4: physical package, then DGD, then AWB, then invoice, then
packing list. Name which document is wrong; never edit two toward each other.

## Where documents are missing

Say which were submitted and mark the rest not performed. A lithium shipment reviewed on the
AWB alone has not been checked against a declaration, and the report must not read as though it
had been.
