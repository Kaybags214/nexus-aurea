# Shipper's Declaration — Completed Example Walkthrough

Purpose: Notes for reviewing a filled-out (not blank) Shipper's Declaration for Dangerous Goods, to compare against practice attempts in `audit-lab/`.

## What a Completed Example Should Show

- Every field from `templates/02-shipper-declaration/shippers-declaration-reference.md` filled with plausible, internally consistent data.
- UN number, proper shipping name, class/division, and packing group that are all mutually consistent (e.g., UN1845 / Carbon Dioxide, Solid / Class 9 — no packing group assigned to dry ice).
- Packing instruction number that matches the packing group and quantity limits in IATA DGR Section 5.
- "Cargo Aircraft Only" vs. "Passenger and Cargo Aircraft" marked correctly based on the quantity shipped and any state/operator variations.
- A 24-hour emergency contact number in the format required (not a placeholder).
- Printed name, signature, and date on the certification line.

## How to Use This for Practice

1. Pull the official blank fillable form (see link below) and fill it out with a hypothetical shipment.
2. Compare your filled form against the field-by-field checklist in `templates/02-shipper-declaration/shippers-declaration-reference.md`.
3. Deliberately introduce one error (e.g., wrong packing instruction number) and practice catching it — this mirrors the discrepancy-review exercises in `audit-lab/`.

## External Example for Reference

- Wright State University — Shipper's Declaration of Dangerous Goods Example Form: https://www.wright.edu/sites/www.wright.edu/files/page/attachments/Declaration-of-Dangerous-Goods-Example-Form_0.pdf
  (An institutional training example showing a filled-out form layout — useful for seeing how fields are populated in practice.)

## Related Files

- `templates/02-shipper-declaration/shippers-declaration-reference.md` — blank field reference and official IATA source links
- `audit-lab/dry-ice-un1845/` — practice audit files for dry ice shipments, which often require a linked DGD
