# Blockchain Adoption Tracker

Purpose: Track claimed blockchain adoption in logistics, pharma, and compliance, and record whether each claim was verified. Counterpart to filing-tracker.md, which does the same job for SEC filings.

A claim is not evidence. This file exists to force the difference.

## Evidence Levels

- **Announcement** — a press release or partnership statement. No proof of use.
- **Pilot** — a limited deployment with a defined scope and end date.
- **Production** — running in a live business process with real volume.
- **Stale** — was true once, no evidence of current activity.
- **False** — checked against a primary source and contradicted.

## Tracker

| Date Reviewed | Network | Claim | Source Date | Evidence Level | Finding | Action |
|---|---|---|---|---|---|---|
| 2026-07-28 | HBAR | EU DPP rules will drive pharma blockchain adoption | 2026 | **False** | ESPR Art. 1(2) excludes medicinal products for human and veterinary use. Pharma is out of scope. | Do not carry this thesis forward |
| 2026-07-28 | HBAR | Merck + Hashgraph Group DPP on Hedera, M-Trust authentication | 2026-06 | Announcement | Real deployment. Entity is Merck KGaA Darmstadt (pigments/materials), not Merck & Co pharma. Primary sources 403'd — confirm entity. | Confirm entity; watch for production volume |
| 2026-07-28 | HBAR | NHS vaccine cold-chain monitoring via Everyware | 2021-01 | **Stale** | Two hospitals, South Warwickshire, COVID-era. Wider rollout planned, no evidence it happened. | Stop citing as current evidence |
| 2026-07-28 | VET | AMRC / Rekord DPP deployment, 300k+ events onchain | 2026-01-15 | Production | Real usage number. Advanced manufacturing, not pharma. | Track event count next quarter |
| 2026-07-28 | VET | Decent partnership — safety inspections, audits, compliance reports onchain | 2026-02-19 | Announcement | Compliance-evidence pattern, directly relevant to audit-lab lane. | Watch for deployment proof |
| 2026-07-28 | TRAC | GS1 membership, EPCIS/CBV 2.0 standards work | ongoing | Production | Strongest finding. Same standard DSCSA interoperability requires. | Study EPCIS 2.0 directly |
| 2026-07-28 | TRAC | Sustainable Medicines Partnership w/ AstraZeneca, Pfizer, GS1 | 2023-01 | Announcement | No 2026 confirmation of continued activity found. | Verify SMP is still active |
| 2026-07-28 | LINK | Oracle data for temperature, GPS, shipment status, proof of delivery | — | **Unverified** | Traction is financial/RWA (Swift, Canton, ANZ, BNY Mellon), not logistics telemetry. | Correct the relevance claim in watchlist |
| 2026-07-28 | — | DSCSA runs on blockchain | 2024-11-27 | **False** | Runs on EPCIS 1.3 → 2.0 JSON-LD, a GS1 data standard. Blockchain is an optional trust layer. | Study EPCIS, not chains |

## Open Questions

- Is the Sustainable Medicines Partnership still active, and is Trace Labs still a member?
- Which Merck entity is in the Hashgraph deal — confirm Merck KGaA vs Merck & Co from a primary source.
- Did the VeChain AMRC deployment grow past 300k events in Q2 2026?
- What did MediLedger's FDA pilot actually conclude, in the FDA's own words?
- Does any production pharma system in the US or EU use a public blockchain as a system of record? So far the answer appears to be no.

## Review Rules

- Record the source date, not just the review date. Recycled old news is the most common failure mode.
- Check regulatory claims against the regulation, not against commentary.
- Downgrade a claim to Stale if no activity is found within roughly 18 months.
- An announcement with named Fortune 500 partners is still an announcement.
- Track whether pilots ended, not just whether they started. Quiet pilots usually died.
