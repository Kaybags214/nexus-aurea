# Check 3 — Regression

**Corrections break things.** This check is the reason a re-review is a different job from a
re-run, and it is what the client is actually paying for.

## Where regressions come from

- **A corrected field now disagrees with a document that was never touched.** Fixing the weight
  on the declaration makes it disagree with the AWB, which was right before.
- **A retyped document loses something.** A field that was correct on v1 is absent from v2
  because the whole form was re-entered.
- **A fix applied to the wrong document.** The AWB was corrected when the packing list was the
  document at fault — per `standards-of-precedence.md` §4, precedence decides which one moves.
- **A fresh form loses a signature.** Very common: an unsigned-declaration finding is closed by
  producing a new form, and the new form is also unsigned.
- **The correction is right and the aircraft limitation no longer follows.** Change a quantity
  and the packing instruction column can change with it.

## Run these

- [ ] **Full cross-document check, again.** Not the fields that changed — all of them. This is
      where a corrected field colliding with an untouched document shows up
- [ ] Every field that was **correct in v1** is still correct in v2
- [ ] Signatures, dates and certification present on any **replacement** form
- [ ] Aircraft limitation and packing instruction still follow from the corrected quantities
- [ ] Page count and pagination intact on any reissued multi-page document

## A new Critical is a Critical

Do not soften a regression because the client was trying to help. A shipment that was two
Criticals from tender and is now one different Critical from tender is still not tendering.

Report it in its own section — **New findings, not present in the first review** — so the client
can see it is not a finding they already paid to have told to them.
