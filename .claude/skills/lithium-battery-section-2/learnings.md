# Learnings — lithium-battery-section-2

Append after every run. Newest at the top. A few lines each.

```
## YYYY-MM-DD — <UN number / shipment ref>
- What the document did that the skill did not expect:
- What the skill got wrong or missed:
- Change to make:
```

---

## Provenance of the check order — read before reordering

Ordered by **consequence**, matching the other compliance skills. Section determination runs
first because every later check depends on it; aircraft limitation runs early because it is the
failure that puts a restricted package on a passenger aircraft.

Not ordered by observed failure rate — no dock observations exist yet. See the equivalent note
in the other skills' learnings files.

**Written deliberately without hardcoded thresholds.** Watt-hour ceilings, lithium content
limits and per-package limits are the most frequently revised figures in the DGR, and this skill
was written without a DGR copy to hand. Every threshold check says verify or record as
unverified. If a future run adds real figures, stamp the edition beside each one so staleness is
visible when the 68th ed. lands.

No runs yet. The first real review starts this file.

---

## 2026-09-08 — Check 4 asserted two mark requirements it had never verified

Automated review of PR #7, before this skill had been run against any real document.

- **"Section II shipments require the lithium battery mark"** was written as an absolute. The
  requirement turns on the packing instruction and section, and there are contained-in-equipment
  and small-cell cases where it does not attach. Stated flatly, this skill would reject
  compliant equipment shipments — likely the most common lithium consignment it will ever see.
- **"The telephone number is part of the mark, not optional decoration"** was asserted the same
  way. The reviewer says it was removed from the mark's required content in a recent edition.
  **That was not written in as fact.** Neither reading is verified here, so the check now says
  to verify it and to raise no finding either way until someone does.
- **The pattern to watch for:** this file already said "verify size against the DGR 67th ed."
  for the mark's dimensions. It knew the discipline and applied it to the easy detail while
  stating the underlying requirement as settled. Verifying a parameter of a rule you have not
  verified is worse than not checking at all — it looks rigorous.
- **Still unrun against a real document.** Every finding above came from reading the file, not
  from a shipment.

