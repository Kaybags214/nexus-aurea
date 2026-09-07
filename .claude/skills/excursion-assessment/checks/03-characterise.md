# Check 3 — Characterise the excursion

Only run this once check 2 says the data can be trusted.

For **each** discrete excursion, record:

| Field | Value |
|---|---|
| Direction | above or below range |
| Peak temperature | with units |
| Time of onset | with timezone |
| Duration out of range | hours and minutes |
| Range bound breached | e.g. +8 °C |
| Magnitude beyond bound | peak minus bound |
| Lane segment | origin dock, flight, transit, delivery |

Then across the whole trip:

- [ ] **Number of discrete excursions**
- [ ] **Cumulative time out of range**, summed across all of them
- [ ] Whether any single excursion, or the cumulative total, exceeds a documented allowance

## Cumulative is where reviews fail

Three separate 40-minute excursions are not three minor events; they are two hours out of
range. Report the total as prominently as the peak. A review that lists excursions individually
and never sums them has missed the finding.

## Above and below are different

An excursion above range and one below are separate events with separate consequences —
freezing damage is not the mirror of heat exposure. Never net them off or average across them.

## Severity

Any confirmed breach of the labelled range is **Critical** for the purposes of this report —
the shipment does not proceed to release without a documented quality decision. Severity here
means "this must be decided by someone qualified", not "the product is spoiled".
