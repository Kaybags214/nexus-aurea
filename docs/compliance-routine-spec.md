# Compliance & documentation routine — starting notes

Draft picked up mid-conversation; nothing here is settled. Read this first next session
so the work starts from the current state rather than re-deriving it.

## Current state (scanned 2026-08-30)

The compliance side of this repo is scaffolding, not content.

| Area | Files | Real content |
|---|---|---|
| `compliance/` | 6 | 1 — `05-forms/forms-index.md` |
| `dgr/` | 8 | 2 — shipper declaration example, non-radioactive checklist |
| `customs/` | 4 | 1 — CBP entry forms reference |
| `cold-chain/` | 8 | 2 — temperature log template, dry ice UN1845 |
| `templates/` | 10 | 4 — AWB, shipper declaration, commercial invoice, packing list |
| `audit-lab/` | 4 | 3 — findings template, dry ice checklist and sample audit |
| `tax-infrastructure/` | 6 | 5 — 1120 overview, close checklist, deadlines, CPA notes, IRS links |

Everything else is a `.gitkeep`. Most of the real content arrived on 2026-08-30 when six
abandoned branches were merged; before that it was unreachable.

**Implication:** a daily "what changed" routine has almost nothing to report and would
produce noise. The useful shape is a routine that *fills gaps on a cadence*, one section
per run, and opens a PR for review rather than committing straight to `main` — compliance
content should not land unreviewed.

## The question to settle first

What this work is actually for changes the whole design, and it was never established:

1. **Certification study** — a calendar entry references CBLE (Customs Broker License Exam).
   If that's the driver, the routine should build study material and practice sets against
   the exam outline, and the `06-practice/` directories are the target.
2. **Operating compliance for Nexus Aurea** — if the business ships regulated goods, the
   routine should build real SOPs, checklists and audit trails, and accuracy against current
   CFR/IATA/GDP text matters far more than volume.
3. **Regulatory currency** — tracking amendments to IATA DGR, 19 CFR, GDP guidance and
   flagging what changed.

These need different sources, different cadences and different review bars. Do not guess —
ask, then design.

## Proposed shape (unvalidated)

- **Weekly, not daily.** There isn't daily change here.
- **One section per run**, working a written backlog, so each run has a defined deliverable.
- **Opens a PR**, never commits to `main` directly.
- **Cites primary sources** — eCFR, IATA, FDA, CBP — with retrieval dates. Regulatory text
  paraphrased from memory is a liability, not a document.
- **Never asserts a regulatory requirement without a citation.** An unsourced compliance
  document is worse than no document.

## Constraints already learned

- Routines can carry MCP connectors, but only when attached from the claude.ai Routines UI —
  the `connectors` parameter is unavailable to sessions on this account.
- Cron is UTC and does not follow daylight saving. See `market-watch/flow-brief-routine.md`.
- Two routines scheduled in the same minute that both push to `main` will race and one will
  be rejected. Stagger them.
