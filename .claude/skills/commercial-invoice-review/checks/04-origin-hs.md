# Check 4 — Country of origin and HS heading

## Country of origin

- [ ] Stated per line where lines differ in origin
- [ ] A country, not a region or a trading bloc
- [ ] Not confused with country of export or country of purchase

Origin is where the goods were produced or last substantially transformed. An invoice showing
the seller's country as origin by default is a **Major** finding — it may be right, but nothing
on the document shows that it was determined rather than assumed.

## HS heading

- [ ] An HS or HTS number is present where the destination requires it on the invoice
- [ ] Digit count is plausible for the destination — 6 international, often 8 or 10 national
- [ ] The heading is not obviously inconsistent with the goods description

## The limit of this check

**Do not assign, correct, or confirm an HS code.** Classification is a determination for the
destination authority or a licensed customs broker, and per `standards-of-precedence.md`
section 3 the destination has final say.

What you may report:

- The code is **absent** where required → Major
- The code has an **implausible digit count** → Major
- The code and the description are **facially inconsistent** — e.g. a heading for machinery
  against a described pharmaceutical → Major, phrased as a query, not a reclassification
- The **same goods carry different codes** across documents → Critical

Phrase every heading finding as "verify with the broker", never as "the correct code is".
