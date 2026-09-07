# Check 2 — Classification, line by line

For **each entry** in Nature and Quantity of Dangerous Goods, in the DGR column order:

- [ ] **UN or ID number**, correct for the substance
- [ ] **Proper shipping name**, matching the UN number exactly — not a trade name, not a
      paraphrase; technical name in brackets where the entry requires one
- [ ] **Class or division**, with subsidiary risk where one applies
- [ ] **Packing group**, where the entry has one
- [ ] **Quantity and type of packing** — net quantity per package with unit, packaging described
- [ ] **Packing instruction number**, correct for this UN number, aircraft type and quantity
- [ ] **Authorization** completed where a special provision, state approval or exemption applies

## Critical conditions

- A proper shipping name that does not match its UN number
- Quantity per package over the packing instruction limit
- A missing packing group where the entry requires one

## Verifying limits

Check the packing instruction and its quantity limits against the operator's own DGR 67th ed.
copy. If no copy is to hand, record it in the sidecar `unverified` array rather than asserting
a figure. See `skill-contract.md` rule 3.

## State and operator variations

Check origin, transit and destination state variations, plus the operator's own. They stack.
Name the ones you checked in the sidecar log — "none applicable" is a valid entry, "did not
check" is not.
