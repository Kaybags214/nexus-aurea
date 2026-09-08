# GDP / GMP Records — Review Reference

Purpose: Field-by-field reference for reviewing Good Distribution Practice (GDP) and Good
Manufacturing Practice (GMP) records that accompany pharmaceutical shipments. Original summary built
from EU GDP Guidelines (2013/C 343/01), FDA 21 CFR Parts 210/211, WHO TRS 961 Annex 9, and Cold
Chain 4.0 digital-record practice. Not a copy of any proprietary SOP.

## Governing standard (see standards-of-precedence.md, section 2)

Product label storage condition (floor) > destination-country GDP/GMP > IATA CEIV Pharma / TCR for
the air leg > WHO TRS 961 / USP <1079> supporting practice > customer quality agreement if stricter.
**The narrowest temperature range and strictest documentation/retention requirement win.**

## Records that should accompany or back a GDP/GMP shipment

- Product name, strength, dosage form
- Batch / lot number
- Expiry date (and retest date if applicable)
- Quantity shipped
- Storage condition on the label (e.g. "Store at 2–8 °C", "Do not freeze", "Store below 25 °C")
- Manufacturer / MAH (marketing authorization holder) and distributor
- Wholesale distribution authorization / license number (GDP)
- Certificate of Analysis reference (see `../02-certificate-of-analysis/`)
- Temperature log / data-logger record for the lane (see `cold-chain/02-temperature-control/`)
- Chain-of-custody / handover signatures

## Core GDP review points

- [ ] Storage condition on the record matches the product label exactly (never widened)
- [ ] Batch/lot number on the record matches the CoA and the physical labels
- [ ] Expiry date present and not expired / not expiring inside the transit + shelf window
- [ ] Distributor holds a valid wholesale distribution authorization
- [ ] Temperature was continuously monitored for the whole lane, logger calibration current
- [ ] Any excursion has a documented investigation and a product disposition decision
- [ ] Falsified-medicines safety features intact where required (tamper-evidence, serialization)
- [ ] Retention period for the record documented and met (GDP typically ≥ 5 years; confirm locally)

## Core GMP review points (where a batch record / release doc is in scope)

- [ ] Batch record signed by the authorized/qualified person (QP for EU)
- [ ] In-process and finished-product test results present and within specification
- [ ] Deviations and CAPAs referenced and closed
- [ ] Labeling and packaging reconciliation complete

## Cold Chain 4.0 / digital-record points

- [ ] Data-logger file (not just a summary) archived and traceable to the shipment
- [ ] Logger ID and calibration certificate reference on the record
- [ ] No time gaps in the digital time-series; alarms acknowledged
- [ ] Digital record immutable / audit-trailed (who changed what, when)

## Common findings

- 🔴 Storage condition on paperwork is wider than the product label (e.g. label says 2–8 °C, record
  says "ambient") — Critical.
- 🔴 Temperature excursion with no investigation or disposition — Critical.
- 🔴 Expired lot, or expiry before delivery + minimum shelf life — Critical.
- 🟡 Logger calibration certificate expired at ship date — Major.
- 🟡 Batch number mismatch between CoA and shipping record — Major.
- 🟢 Missing retention-period notation — Minor.

## Sources

- EU GDP Guidelines 2013/C 343/01: https://health.ec.europa.eu/medicinal-products/good-manufacturing-practice-and-good-distribution-practice_en
- FDA 21 CFR Parts 210 & 211: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211
- WHO TRS 961 Annex 9 (storage & distribution): https://www.who.int/publications/m/item/annex-9-trs-961
- USP <1079> Good Storage and Distribution Practices.
