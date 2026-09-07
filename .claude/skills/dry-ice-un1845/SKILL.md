---
name: dry-ice-un1845
description: Verify dry ice (UN1845, Carbon dioxide solid) documentation on an air shipment — net weight per package in kg, Class 9 marking, PI 954 limits, AWB handling information, and weight agreement across AWB, DGD, invoice and packing list. Use when a document mentions dry ice, UN1845, carbon dioxide solid, a refrigerant, frozen or -20C/-70C shipping, or when reviewing any cold-chain air shipment that could be refrigerated with dry ice.
---

# Dry ice / UN1845 verification

One job: decide whether the dry ice on this shipment is documented correctly, and produce the
findings. Nothing else. If the document also has lithium batteries or a temperature excursion,
that is a different skill's work — note it and move on.

Governed by `compliance-auditor/standards-of-precedence.md`. State variation > operator
variation > IATA DGR 67th ed. > ICAO TI > 49 CFR. The strictest applicable requirement governs.

## Before you start

Read `audit-lab/dry-ice-un1845/dry-ice-review-checklist.md`. It is the operator's own checklist
and it wins over anything in this file.

## The checks, in order

Run all of them. Do not stop at the first failure.

### 1. Identity
- [ ] UN number reads exactly **UN1845**
- [ ] Proper shipping name is **"Dry ice"** or **"Carbon dioxide, solid"** — no other wording
- [ ] Class **9** is shown

### 2. Net weight — the highest-risk field
- [ ] Net weight of dry ice is stated **per package**, not as a shipment total only
- [ ] The unit is **kilograms**. Pounds alone is a Critical finding, not a formatting nit
- [ ] The figure is a number you can read, not "as required" or a blank
- [ ] Quantity per package is within the PI 954 limit — **verify the current limit against the
      operator's own DGR 67th ed. copy** rather than trusting a remembered figure, and check the
      passenger vs. cargo-aircraft column that matches this shipment

A missing or pounds-only dry ice net weight is the single most common reject at acceptance.
Treat it as Critical every time.

### 3. Marking and labelling
- [ ] Class 9 label on each package
- [ ] UN1845 and the proper shipping name marked on the outer package
- [ ] Shipper and consignee name and address marked on the package
- [ ] Packaging permits the release of carbon dioxide gas — a sealed, non-venting outer is Critical

### 4. Air Waybill handling information
- [ ] Nature and Quantity of Goods, or Handling Information, carries the dry ice entry
- [ ] Number of packages containing dry ice is shown
- [ ] Net quantity per package in kg appears here too, not only on the DGD
- [ ] Temperature-control instruction present where the product is temperature-controlled

### 5. Cross-document weight agreement
Build this table every time more than one document is present. Any disagreement is Critical.

| Document | Packages w/ dry ice | Net kg per package | Total net kg |
|---|---|---|---|
| AWB | | | |
| DGD (if present) | | | |
| Packing list | | | |
| Invoice | | | |

- [ ] The per-package figures agree across every document that states one
- [ ] Package count agrees with the AWB piece count
- [ ] Shipper and consignee agree across all documents

### 6. Is a DGD even required?
Dry ice used **solely as a refrigerant for non-dangerous goods** does not require a Shipper's
Declaration — the AWB entry carries it. Do not raise a Critical finding for a missing DGD in
that case. If the contents are themselves dangerous goods, the DGD is required and dry ice is
declared on it. Say which case you concluded and why.

## What you may not do

- Do not guess a net weight to fill a blank. Unreadable is **"cannot verify from image"**.
- Do not compute a sublimation allowance and present it as the declared weight. If asked whether
  the ice will last the transit, verify against the packaging's own tested sublimation rate and
  the actual door-to-door time — and label it an estimate, separate from the audit findings.
- Do not clear the shipment. Verdict is HOLD or REJECT while a Critical is open.

## Output

Findings only, in the severity shape from `compliance-auditor/audit-report-template.md`:

```
### 🔴 Critical
- **[C-1]** Dry ice net weight per package absent from AWB Nature and Quantity of Goods.
  **Standard:** IATA DGR 67th ed. — net quantity of dry ice per package required in kg.
  **Fix:** Enter "UN1845 Dry ice, 3 x 2.5 kg" in Nature and Quantity of Goods.
```

Every finding names the level it came from. A flag without a cited standard is not a finding.

Append anything you learned about this document type to `learnings.md` in this folder.
