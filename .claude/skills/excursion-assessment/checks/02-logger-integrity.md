# Check 2 — Logger and data integrity

Gate for everything after it. An excursion characterised from untrustworthy data is worse than
no assessment, because it looks authoritative.

- [ ] Logger identified — make, model, serial
- [ ] **Calibration certificate current** at the time of the trip, with the expiry date read
- [ ] Logging interval stated, and short enough to catch a real excursion
- [ ] Start and stop timestamps cover the whole lane, with no gap
- [ ] Timestamps carry a timezone, and the trip's timezone changes are accounted for
- [ ] Logger placement stated — with product, in the shipper wall, or on the ULD

## Critical conditions

- **Calibration expired or absent.** The data does not support any quality decision.
- **A gap in the record.** An unmonitored interval is not a compliant interval; the worst case
  during the gap is unknown and must be treated as such.
- Logging interval so coarse that a short excursion could pass unrecorded.

## Placement changes the meaning

A logger in the shipper wall reads differently from one against product. Say where it was. An
ambient logger showing an excursion is not the same finding as a product-adjacent one, and
conflating them either over- or under-states the risk.

## Do not repair the data

Do not interpolate across a gap, discard an outlier, or re-baseline a drifting logger. Those
are quality decisions. Report the defect.
