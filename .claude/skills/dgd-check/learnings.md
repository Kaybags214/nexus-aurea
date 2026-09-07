# Learnings — dgd-check

Append after every run. Newest at the top. A few lines each.

```
## YYYY-MM-DD — <document ref>
- What the document did that the skill did not expect:
- What the skill got wrong or missed:
- Change to make:
```

---

## 2026-09-07 — UN1830 and UN3077 practice declarations (same set)

Run after patching the two gaps the first run exposed. Both declarations REJECT, but for a
completely different reason than the first one.

- **Classification was clean on both.** All columns mutually consistent, packaging described by
  type and specification code ("1 fibreboard box (4G)"), shipment type and aircraft limitation
  both correct. The UN3077 entry supplied the technical name in brackets for an n.o.s. entry —
  the element most often omitted on n.o.s. declarations.
- **The same five defects appear on all three declarations in the set:** no AWB number, no
  signature, no signatory title, no place of signing, emergency number without a country code.
  Five identical omissions across three documents is a **habit, not three mistakes**, and
  reporting it that way is more useful than three separate reports saying the same thing.
- **Change to make:** when several documents from one submitter are audited together, the report
  should carry a short cross-document pattern section naming defects that repeat. A defect on
  three of three is a different finding from a defect on one of three. Neither `dgd-check` nor
  `skill-contract.md` currently says to look for this.
- The patched check 1 shipment-type step was exercised on both and passed cleanly — which is the
  right outcome, and confirms the first declaration's radioactive marking was an outlier rather
  than a systematic misunderstanding.

## 2026-09-07 — Practice DGD, UN1845 + biological substance, IAD-ATL

**First run against a real filled document, unseen by the skill's author.**
4 Critical, 9 Major, 2 Minor. Verdict REJECT.

- **Check 2 earned its place.** The headline finding — UN3393 declared against a Category B
  shipping name, when Category B is UN3373 — came from the line-by-line "PSN must match the UN
  number" check. The document contradicted itself (class 6.2 matches 3373, not 3393), and that
  internal inconsistency is what confirmed it as a transposition rather than a different
  intended substance. **Cross-column consistency is a stronger signal than any single field.**
  Consider making it an explicit check-2 step: read the columns against each other, not just
  each against the DGR.
- **A check that does not exist caught nothing.** The shipment-type line (radioactive vs
  non-radioactive) was marked RADIOACTIVE on a dry-ice-plus-biological shipment. This was found
  by reading the raw form fields, **not** because any check file asks about it. Check 1 covers
  header and routing and check 3 covers aircraft limitation; neither covers shipment type.
  **Change to make: add shipment type to check 1.** It sits beside the aircraft lines on the
  form and is exactly as consequential.
- **Comparing the three declarations in the set was diagnostic.** The other two had the
  shipment-type fields filled correctly, which made the reversal on this one obviously an error
  rather than a misunderstanding. Where an operator submits several similar documents, reading
  them against each other finds things a single-document review will not.
- **Packing-group-where-none-exists** appeared twice (dry ice, and the Cat B entry). Check 2's
  Critical list names "a missing packing group where the entry requires one" but says nothing
  about a packing group supplied where none exists. **Change to make: name both directions.**
- The repo's own `completed-example-reference.md` supplied the dry-ice packing group citation,
  so no regulatory claim had to be made from memory. That is the contract working as intended.

## Provenance of the check order — read before reordering

The checks are ordered by **consequence**: what would be worst to miss runs first, and
deterministic checks that cost nothing run before expensive ones.

They are **not** ordered by observed failure rate. As of 2026-09-07 no dock observations exist
to order them by — the operator is building the system ahead of the role, per the standing rule
in `CLAUDE.md`. Consequence-ordering is the right default in that position, but it is a
default, not evidence.

**When real reviews start, that changes.** Record what actually fails, and reorder to match.
Until then nobody should read this order as validated by practice.

No runs yet. The first real review starts this file.
