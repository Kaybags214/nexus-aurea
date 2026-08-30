# Compliance Auditor

Purpose: An agentic document-review workflow for Nexus Aurea. You photograph a shipping/compliance
document, the auditor reads it, checks it against the repo's own reference standards, flags every
issue by severity, and returns a corrected version — the same way `market-watch/` runs on the
watchlist, but for paperwork instead of tickers.

This lane is the **operational** side. `audit-lab/` stays as the practice / proof-of-work area.

## What it audits

| # | Document | Reference standard used |
|---|----------|-------------------------|
| 1 | Air Waybill (AWB) | `templates/01-awb/awb-reference-template.md` (IATA Res. 600a) |
| 2 | Shipper's Declaration for Dangerous Goods (DGD) | `templates/02-shipper-declaration/` + `dgr/` (IATA DGR 67th ed. / 49 CFR) |
| 3 | Commercial Invoice | `templates/03-commercial-invoice/` (CBP / export.gov) |
| 4 | Packing List | `templates/04-packing-list/` |
| 5 | Bill of Lading (ocean) | `templates/07-bill-of-lading/bill-of-lading-reference.md` |
| 6 | Dry Ice / UN1845 docs | `cold-chain/03-dry-ice/` + `audit-lab/dry-ice-un1845/` |
| 7 | Cold-chain temperature log | `cold-chain/02-temperature-control/temperature-log-template.md` (EU GDP / WHO TRS 961 / USP <1079>) |
| 8 | Pharma — Certificate of Analysis (CoA) | `pharma/02-certificate-of-analysis/` |
| 9 | Pharma — GDP/GMP records | `pharma/01-gdp-gmp/` |
| 10 | Biological substances (UN3373 / UN2814 / UN2900) | `pharma/03-biological-substances/` |
| 11 | CBP entry (Form 7501 / 3461) | `customs/05-import-export/cbp-entry-forms-reference.md` |

## How to use it

### Option A — In chat (works today, no setup)
1. Take clear photos of the document(s). One shipment can have several documents — send them together.
2. Send them and say which document type(s) they are (or let the auditor detect it).
3. You get back:
   - a **flagged findings report** (Critical / Major / Minor, color-coded), and
   - a **corrected version** of the document with the fixes applied.
4. Reports are saved to `compliance-auditor/audit-reports/` and pushed to GitHub, dated
   `audit_YYYY-MM-DD_<doctype>.md`.

### Option B — n8n webhook (self-hosted, hands-off)
See `n8n-workflow-setup.md`. You POST an image to a webhook (or email it in); the workflow runs the
same audit prompt through a vision model and emails/commits the result. Same brain, automated.

## The brain

- `AUDIT-ENGINE-PROMPT.md` — the system prompt the auditor runs on. This is the core file. It
  encodes what to extract, how to score severity, and the standing rules.
- `standards-of-precedence.md` — the order-of-precedence: which regulation wins when two conflict.
  Read this first; it governs every finding.
- `audit-report-template.md` — the exact output shape (flagged report + corrected version).

## Operating rule

Documents outrank memory. Photograph the actual paper, audit against the written standard, cite the
rule behind every flag. Never pass a shipment that has an unresolved Critical finding. Do not store
confidential customer documents here unless redacted — use `intake/` only for redacted practice
scans, and keep real customer data out of git.
