# Check 1 — UN number, packing instruction, section

Decide all three before auditing anything. Everything downstream depends on them.

## The four UN numbers

| UN | What it covers | Packing instruction |
|---|---|---|
| **UN3480** | Lithium **ion** cells/batteries shipped **alone** | PI 965 |
| **UN3481** | Lithium **ion** packed with, or contained in, equipment | PI 966 (packed with) / PI 967 (contained in) |
| **UN3090** | Lithium **metal** cells/batteries shipped **alone** | PI 968 |
| **UN3091** | Lithium **metal** packed with, or contained in, equipment | PI 969 (packed with) / PI 970 (contained in) |

Two questions settle it:

1. **Ion or metal?** Rechargeable is normally ion; primary/non-rechargeable is normally metal.
   If the document does not say, it is not determinable — say so rather than inferring from the
   device type.
2. **Alone, packed with equipment, or contained in equipment?** These are three different
   states with three different packing instructions. "Packed with" and "contained in" are not
   interchangeable.

- [ ] UN number stated and consistent with ion/metal and with the packing arrangement
- [ ] Packing instruction stated and matching that UN number
- [ ] **Section stated — IA, IB or II**

## Section is not optional information

The same UN number under Section IA, IB and II carries different documentation, marking and
aircraft rules. A document naming PI 965 without naming the section has not said enough to be
audited. Treat a missing section as a finding, not something to infer from quantity.

## Verify the pairing

Check the UN-number-to-packing-instruction pairing against the operator's DGR 67th ed. copy.
If no copy is available, record it in the sidecar `unverified` array — do not assert the
pairing from memory, even where it looks obvious.

## Cross-column reading

As in `dgd-check` check 2: read UN number, shipping name, class and packing instruction against
**each other**. All four describe one arrangement. Where three agree and one does not, the
outlier is usually a transposed digit rather than a different intended shipment — say so.
