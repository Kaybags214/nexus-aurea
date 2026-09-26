# Check 2 — Classification, line by line

For **each entry** in Nature and Quantity of Dangerous Goods, in the DGR column order:

- [ ] **UN or ID number**, correct for the substance
- [ ] **Proper shipping name**, matching the UN number exactly — not a trade name, not a
      paraphrase; technical name in brackets where the entry requires one
- [ ] **Class or division**, with subsidiary risk where one applies
- [ ] **Packing group** — present where the entry has one, and **absent where it does not**
- [ ] **Quantity and type of packing** — net quantity per package with unit, packaging described
- [ ] **Packing instruction number**, correct for this UN number, aircraft type and quantity
- [ ] **Authorization** completed where a special provision, state approval or exemption applies

## Critical conditions

- A proper shipping name that does not match its UN number
- Quantity per package over the packing instruction limit
- A missing packing group where the entry requires one

## Packing group runs in both directions

A packing group **supplied where the entry has none** is a finding too, and it is the more
common error. Dry ice (UN1845) has no packing group. Neither does a Category B biological
substance under PI 650. Writing "II" or "I" into those rows invents a classification the entry
does not carry, and can drive the wrong packaging selection.

Severity **Major** for a packing group added where none exists; **Critical** for one missing
where the entry requires it. Cite the reference that establishes which — for dry ice,
`dgr/03-shipper-declarations/completed-example-reference.md` states it directly.

## Read the columns against each other

The strongest signal in this check is not any single field against the DGR — it is the columns
against **each other**. UN number, proper shipping name, class and packing instruction all
describe the same substance, so a mismatch between any two of them localises the error.

A declaration reading UN3393 / "Biological substance, Category B" / class 6.2 / PI 650 is
self-contradicting: three columns agree on UN3373 and one does not. That is a transposed digit,
not a different intended substance — and saying so in the finding is more useful than reporting
four separate deviations.

## Verifying limits

Check the packing instruction and its quantity limits against the operator's own DGR 67th ed.
copy. If no copy is to hand, record it in the sidecar `unverified` array rather than asserting
a figure. See `skill-contract.md` rule 3.

## State and operator variations

Check origin, transit and destination state variations, plus the operator's own. They stack.
Name the ones you checked in the sidecar log — "none applicable" is a valid entry, "did not
check" is not.
