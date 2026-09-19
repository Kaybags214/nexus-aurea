# Check 3 — Aircraft limitation

The declaration carries two shipment-type lines: passenger-and-cargo aircraft, and cargo
aircraft only. Exactly one survives.

- [ ] The non-applicable line is **deleted**, not left standing
- [ ] Where the entry is cargo-aircraft-only, the AWB handling information says so too
- [ ] Where quantities exceed the passenger-aircraft column, cargo-aircraft-only is selected

## Both lines left intact

**Critical.** Acceptance cannot determine what was declared. This is not a formatting nit — it
is the difference between a package being legal and being loaded onto a passenger aircraft it
is barred from.

## Quantity drives the selection

If the per-package quantity exceeds the passenger-aircraft limit for that packing instruction,
cargo-aircraft-only is not optional. A declaration showing passenger-eligible with an
over-limit quantity is Critical, and the finding names both facts.
