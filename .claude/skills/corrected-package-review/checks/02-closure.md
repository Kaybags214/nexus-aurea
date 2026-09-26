# Check 2 — Closure, finding by finding

Take the prior report's findings **in order**. Every one gets a row. No finding is skipped, and
no finding is closed by silence.

| Prior | Finding | Status | Evidence |
|---|---|---|---|
| C-1 | | | |
| C-2 | | | |
| M-1 | | | |

## The four statuses

- **Closed** — the defect is gone and the replacement is correct against the standard
- **Not closed** — unchanged, or changed in a way that does not address the finding
- **Partially closed** — some of it fixed. A partially closed Critical is still Critical
- **Closed incorrectly** — the field changed, the original defect is gone, and **the new value
  is also wrong.** This is the status that matters most, and it is the one a diff-based review
  misses entirely

## Do not confuse "changed" with "fixed"

A field that moved is not evidence of correctness. Re-check the new value against the same
standard the original finding cited.

Worked example. A prior finding read *"dry ice quantity in pounds only — restate in kg."* The
corrected document says `5.44 kg`. That is not automatically closed:

- Is 5.44 kg the true weight, or an arithmetic conversion of a figure that was itself wrong?
- Does it now agree with the packing list, which said 4 kg × 4 cartons?
- Is it stated **per package**, which was the other half of the original finding?

One finding can require several things to be true. Closing it needs all of them.

## Re-run every Critical from first principles

Do not rely on the prior report's reasoning. Re-read the field, re-apply the check, reach the
conclusion again. If it disagrees with the prior report, **say so** — the first review may have
been wrong, and that is worth more to the client than a consistent error.

## Evidence, not assertion

Every status names what was read: the field, the value now, the value before. A client
disputing a status should be able to check it against their own document without asking you what
you meant.
