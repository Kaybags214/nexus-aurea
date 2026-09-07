# Check 4 — Nature and Quantity, and handling information

## Nature and Quantity of Goods

- [ ] Goods described in plain terms, not a commodity code alone
- [ ] Description does not contradict the invoice goods description
- [ ] Dangerous goods referenced where present, with UN number and proper shipping name
- [ ] Dry ice entry present where used as a refrigerant, with net kg per package
- [ ] Temperature range shown for temperature-controlled product

## Handling information

- [ ] Carries any DG, cold-chain or aircraft-limitation instruction
- [ ] **"Cargo Aircraft Only"** shown where the DG requires it, and consistent with the DGD
- [ ] Temperature-control handling instruction present for cold-chain product
- [ ] Special handling codes consistent with the commodity

## Aircraft limitation mismatch

Where the DGD says cargo aircraft only and the AWB does not, that is **Critical**. Acceptance
reads the AWB; a shipment can be loaded onto a passenger aircraft on the strength of it.

Detailed dry ice verification belongs to `dry-ice-un1845`. Detailed classification belongs to
`dgd-check`. Here you are only confirming the AWB carries what those documents require it to.
