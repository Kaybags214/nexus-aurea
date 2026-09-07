# Agentic OS — Idea Capture

Status: captured, not yet built. Saved so the idea does not get lost.

## Source

- Video: **"The NEW Agentic OS standard for Claude 5 Models is here (Full Breakdown)"**
- Channel: **RoboNuggets** (Jay E)
- URL: https://www.youtube.com/watch?v=8NSyI-npJCU
- Site / newsletter: https://www.robonuggets.blog
- Community: https://robonuggets.us (Skool)

## PDF status — NOT retrieved

The downloadable guide is **gated behind the RoboNuggets Skool community**, not a direct
public link. This session's network egress proxy also blocks youtube.com, robonuggets.us,
and robonuggets.blog, so the PDF could not be fetched or attached here.

To get it: join the free Skool community linked in the video description and download the
Agentic OS guide from the classroom section. Drop the PDF into this folder as
`robonuggets-agentic-os-guide.pdf` and it can be parsed and mapped in full.

Everything below is reconstructed from public search results describing the video and the
framework, not from the PDF itself. Treat it as a working reconstruction, not a citation.

## The framework — ARMS

Four layers. Ordered here bottom-up by dependency, which is how it should be built:

| Layer | Name | What it is |
|-------|------|-----------|
| L0 | **Memory** | Persistent context. Without it every session restarts from zero. |
| L1 | **Skills** | Small, single-purpose units. One task, one defined way. Each carries a `learnings.md`. |
| L2 | **Routines** | Scheduled / triggered execution. Cloud-run, unattended. |
| L3 | **Applications** | The surface a non-technical person operates without a terminal. |

The three gaps it closes: **memory** (forgets every session), **consistency** (same question,
two different answers), **access** (only the terminal operator can run it).

## Mapping onto Nexus Aurea

This repo is already most of L0. The gap is L1 → L3.

- **L0 Memory** — `compliance/`, `dgr/`, `cold-chain/`, `customs/`, `pharma/`,
  `templates/`, `tax-infrastructure/`, `market-watch/`, `audit-lab/`
- **L1 Skills** — AWB review, Shipper's Declaration check, dry ice UN1845 net-weight
  verification, CoA review, cold-chain excursion review, HS code lookup, commercial
  invoice review
- **L2 Routines** — daily market-watch flow brief, weekly excursion review, tax deadline
  watch, watchlist screener run
- **L3 Applications** — `compliance-auditor/intake` (chat + n8n webhook), severity-flagged
  findings report, corrected document output, leave-behind packets

## Visual

`nexus-agentic-os.html` in this folder is the architecture visual.

Published Artifact: https://claude.ai/code/artifact/50370611-d383-4c04-9451-8a0ee603bce6

## Operating rule (unchanged)

Build the system before chasing the opportunity.
