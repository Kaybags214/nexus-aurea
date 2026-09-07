# Check 3 — Incoterms 2020 and currency

- [ ] Incoterm stated
- [ ] Incoterm is a valid **Incoterms 2020** rule
- [ ] **Named place** given with the term — the term alone is incomplete
- [ ] The rule set is identified (e.g. "Incoterms 2020")
- [ ] Currency stated, and stated once — no mixed currencies across lines

## The named place

`EXW` is not a term. `EXW Richmond VA, Incoterms 2020` is. Without the named place the
cost-and-risk split is undefined, which is a **Major** finding and a routine cause of a
valuation query.

## Consistency with the charges

- [ ] Where the term puts freight on the seller (CIP, CPT, DAP, DDP), freight treatment on the
      invoice matches
- [ ] Where the term puts insurance on the seller (CIF, CIP), insurance appears
- [ ] Where the term is EXW or FCA, seller-paid freight lines are explained rather than assumed

A term that contradicts the charge lines is **Major**: the declared customs value is built from
this, and the two cannot both be right.

## Air shipments

Sea-only terms — FAS, FOB, CFR, CIF — on an air waybill shipment are a **Major** finding. They
are defined for sea and inland waterway carriage. The usual intent is FCA or CIP; name that in
the fix rather than assuming which.
