# Check 2 — Identity and net weight

## Identity

- [ ] UN number reads exactly **UN1845**
- [ ] Proper shipping name is **"Dry ice"** or **"Carbon dioxide, solid"** — no other wording
- [ ] Class **9** is shown

## Net weight — the field that gets shipments rejected

- [ ] Net weight is stated **per package**, not as a shipment total only
- [ ] The unit is **kilograms**. Pounds alone is Critical, not a formatting nit
- [ ] The figure is a readable number, not "as required" and not blank
- [ ] Quantity per package is within the PI 954 limit for the aircraft type on this routing

## On the PI 954 limit

Verify against the operator's own DGR 67th ed. copy, and use the column matching this
shipment — passenger-and-cargo aircraft and cargo-aircraft-only differ.

If no DGR copy is to hand, record the check as unverified in the sidecar log's `unverified`
array. Do not supply a remembered figure. See `skill-contract.md` rule 3.

## Where the aircraft type comes from

The routing and the operator, read off the AWB — not assumed. If the AWB does not make the
aircraft type determinable, that is itself a finding: the packing instruction limit cannot be
checked without it.
