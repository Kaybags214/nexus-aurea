# Check 1 — AWB number and check digit

Format: **3-digit airline prefix + 8-digit serial**, eleven digits total. The eighth digit of
the serial is a check digit.

## The arithmetic

> Take the first 7 digits of the serial as a number, divide by 7. The remainder is the check digit.

Worked example — serial `4471882`:

```
4471882 ÷ 7 = 638840 remainder 2   →  check digit 2  →  020-4471 8822 is valid
                                       020-4471 8823 is not
```

## Checks

- [ ] Eleven digits present
- [ ] Check digit arithmetic passes — **show your working in the finding**
- [ ] Airline prefix matches the carrier named on the document
- [ ] The same number appears on every other document referencing it

## Why this runs first

It is deterministic and costs nothing. It catches transcription errors that a visual read
slides past, and a bad number invalidates every cross-reference in check 6 — better to know
before building that table.

A failed check digit is Critical. Do not "correct" it to the nearest valid number; the real
number has to come from the carrier.
