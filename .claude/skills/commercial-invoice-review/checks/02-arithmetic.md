# Check 2 — Line items and arithmetic

Recompute everything. This is the cheapest place to catch a problem and it is deterministic.

For each line:

| Field | Present? | Recomputed |
|---|---|---|
| Goods description | | |
| Quantity + unit of measure | | |
| Unit price | | |
| Line total | | quantity × unit price |

- [ ] Every line has a description specific enough to classify — not "goods", "samples", "parts"
- [ ] Every line has a quantity **with its unit of measure**
- [ ] Every line has a unit price
- [ ] **Every line total equals quantity × unit price** — recompute each one
- [ ] **Invoice total equals the sum of line totals** plus stated charges
- [ ] Freight, insurance and other charges shown separately where the term requires it
- [ ] Any discount shown as a line, not silently absorbed into a unit price

## Findings

- Line total ≠ quantity × unit price → **Critical**. Show both figures in the finding
- Invoice total ≠ sum of lines → **Critical**. Show your sum
- Description too vague to classify → **Major**; it is the most common cause of a customs query
- Missing unit of measure → **Major**; "500" of an unstated unit is not a quantity

## Do not correct silently

If a line is out by a rounding step, say so and show the arithmetic. Do not adjust a unit price
to make the total work — you do not know which of the three numbers is the wrong one, and
guessing changes the declared value.
