# Fixture 001 — answer key

**Do not read this before running a skill against the fixture.** It exists so a run can be
scored: a finding that is not on this list is a false positive, and an item here that the run
missed is a miss.

Nine defects were planted deliberately. Two more (#10, #11) were present without being
noticed by the fixture author and were added after a run found them — see the note at the end.

| # | Defect | Expected severity | Which skill should catch it |
|---|---|---|---|
| 1 | AWB `020-4471 8823` — check digit fails. 4471882 ÷ 7 = 638840 r2, so the valid number ends `8822` | Critical | `awb-review` ch.1 |
| 2 | Dry ice quantity in **pounds only**, no kg | Critical | `dry-ice-un1845` ch.2 |
| 3 | Dry ice shown as a **shipment total**, no per-package figure on the AWB | Critical | `dry-ice-un1845` ch.2 / ch.4 |
| 4 | Dry ice weight **contradicts** the packing list — AWB 12 lb (≈5.44 kg) vs packing list 4 kg × 4 cartons = 16 kg | Critical | `dry-ice-un1845` ch.5 |
| 5 | **Piece count mismatch** — AWB 3, packing list 4 cartons | Critical | `awb-review` ch.3 / ch.6 |
| 6 | **Chargeable weight 38.0 kg is less than gross weight 41.2 kg** — arithmetically impossible | Critical | `awb-review` ch.3 |
| 7 | **Shipper address truncated** on the AWB — "1400 Innovation Dr, Richmond VA" vs "1400 Innovation Drive, Suite 200, Richmond VA 23219". Suite and postcode dropped | Major | `awb-review` ch.2 / ch.6 |
| 8 | **Declared value for carriage is blank** — not NVD, not a figure | Major | `awb-review` ch.5 |
| 9 | **No temperature range in handling information.** "Keep cool. Perishable." is not +2/+8 °C | Major | `dry-ice-un1845` ch.4 / `awb-review` ch.4 |

| 10 | **No document other than the AWB carries the AWB number.** The packing list references `MB-2026-0912` and the invoice `MB-INV-4471`; neither ties back to `020-4471 8823` | Major | `awb-review` ch.6 |
| 11 | **Declared value contradiction.** The AWB declares `NCV` for customs while the invoice shows `USD 5,760.00` | Major | `awb-review` ch.5 / `commercial-invoice-review` |

## Note on #10 and #11 — the key was wrong before it was right

These were not planted. They were present in the fixture because the author wrote a realistic
document set without noticing, and a graded run reported them as findings. Under the strict rule
below they scored as false positives, which was the key's fault, not the run's.

**A finding absent from this list is not automatically a false positive.** Check whether the
defect is genuinely in the fixture first. A key that penalises correct findings trains the wrong
behaviour, and a run that reports a real defect is doing its job even when the key is silent.

## Also present, and correct — should NOT be flagged

- No Shipper's Declaration. Dry ice is a pure refrigerant for non-DG pharmaceutical product,
  so none is required. **A missing-DGD finding here is a false positive** — this is the trap
  `dry-ice-un1845` check 1 exists to prevent.
- Class 9 label and package marking cannot be seen in a transcription. Correct handling is
  "cannot verify from image", not a finding of absence.

## Borderline — either call is defensible

- `CIF` on an air shipment is a sea-only Incoterm and has no named place. Real, but it belongs
  to `commercial-invoice-review` ch.3, not to the two skills under test. Noting it is fine;
  raising it as an AWB finding is not.
