# NEXUS AUREA INC. — SHARED OPERATING CONTEXT
### The single source of truth read by all AI systems working on this project

> **Version:** 1.0 | **Last Updated:** 2026-09-09
> **Owner:** Kaybags (kobb214@gmail.com) | **GitHub:** Kaybags214
> **Rule:** This file is the master router for both Abacus AI and Claude Code.
> Neither system overrides what is written here. If a rule here conflicts with
> a rule elsewhere, this file wins. Edit here first, then propagate.

---

## 1. WHAT NEXUS AUREA IS

A remote documentation review business for:
- Dangerous Goods (DG Classes 3, 8, 9)
- Pharmaceutical / temperature-sensitive shipments

**Revenue model:** Review fee per shipment document package. Client submits documents → AI reviews → human-verified DRAFT findings delivered.

**Live site:** https://www.nexusaureainc.com/

**Status:** Pre-launch build phase.

---

## 2. THE THREE-SYSTEM ARCHITECTURE

```
ABACUS AI          ←→         GITHUB REPO         ←→         CLAUDE CODE
(Builder/Operator)           (Shared Brain)              (Analyst/QA)
       ↓                           ↓                           ↓
 Builds files              Source of record             Reads & audits
 Runs n8n                  JSON → MD always             Structural QA
 Manages GitHub            Never edit MD directly       PR reviews
 Email/terminal            Schema version on change     Deep code analysis
 Scheduled tasks           Changelog every fix          Repo intelligence
       ↓                           ↓                           ↓
                              n8n WORKFLOW
                         (Execution layer)
                    Reads JSON, runs automations,
                    triggers compliance reviews
```

**Ground rule:** All three systems read from the same files. No system invents its own version of a rule, a regulation, or a procedure.

---

## 3. ARMS MAPPING FOR NEXUS AUREA

This project follows the ARMS framework (RoboNuggets). Here is how each layer maps to the Nexus build:

### S — Skills
- Location: `.claude/skills/` (Claude Code) | `skills/` (Abacus AI)
- Built skills (8 total, all committed):
  1. DG Class 3 compliance review
  2. DG Class 8 compliance review
  3. DG Class 9 compliance review
  4. Pharmaceutical / temperature-sensitive shipment review
  5. SDS (Safety Data Sheet) cross-check
  6. Chain-of-Custody (CoC) review
  7. Air Waybill / Shipper's Declaration audit
  8. (8th — confirm name)
- Rule: Any skill that both systems use must have **identical trigger logic and guardrails**. If one system updates a skill, the other must be notified via a changelog entry.

### M — Memory
- Abacus AI memory: persistent global memory store (memory IDs 1–4 active)
- Claude Code memory: CLAUDE.md master router + area index files in repo
- **Shared memory layer:** This file (`NEXUS_SHARED_CONTEXT.md`) — lives in repo root, readable by both
- Alignment rule: Facts that both systems need (standing compliance rules, library locations, architecture decisions) live HERE, not in either system's private memory only

### R — Routines
- Abacus AI: scheduled tasks (Abacus AI platform)
- Claude Code: local routines + potential cloud machine (Syncthing/VPS per ARMS L2)
- Current status: No routines active yet — next build phase
- Rule: Routines must not duplicate each other's work. Abacus handles execution-layer automations. Claude handles repo-level analysis routines.

### A — Applications (Connectors)
- Abacus AI active connectors: Gmail, GitHub, terminal/bash, n8n (MCP)
- Claude Code active connectors: GitHub, Webull (Anthropic-native), filesystem
- Webull: **Claude only** — Anthropic added this connector ~Sept 2026. Abacus does not have it yet.
- Rule: Never route live brokerage/trading actions through Abacus until a verified Webull connector exists. Financial analysis using exported data is fine.

---

## 4. COMPLIANCE LIBRARY — SOURCE OF RECORD

| File | Location | Status |
|------|----------|--------|
| `nexus_aurea_cfr_library.json` | `dgr/02-49cfr/` | ✅ v1.0.1 — authoritative |
| `nexus_aurea_cfr_library.md` | `dgr/02-49cfr/` | ✅ Generated from JSON |
| `nexus_aurea_cfr_library_changelog.md` | `dgr/02-49cfr/` | ✅ v1.0.1 fixes documented |

**Schema discipline:**
- JSON is ALWAYS the source of record
- Markdown is ALWAYS generated from JSON — never edited directly
- Increment `schema_version` on any structural change
- Run structural diff JSON↔MD after any edit
- Every fix gets a changelog entry with before/after

**Pending additions:**
- IATA DGR 67th Edition (2026) — user has licensed copy
- IMDG Code — user will provide
- IATA DGR 66th Edition — user will provide

---

## 5. STANDING COMPLIANCE RULES

> **These rules are non-negotiable. Neither AI system may override them.**

1. All findings are DRAFT. Human review required before any action is taken.
2. Never issue "clearance," "approved," or "safe to ship" conclusions.
3. Mark each finding: **Pass / Fail / Warning / Unable to Verify / Not Applicable.**
4. Cite the specific regulatory section for every finding.
5. Never invent a missing regulation, shipping name, weight, or approval.
6. Findings must identify discrepancies and missing data only.

---

## 6. SECOND BRAIN PRINCIPLES (from RoboNuggets guide)

These principles govern how both systems handle memory and retrieval for this project:

1. **Research before build** — No system guesses at structure. Check what's in the repo before building anything new.
2. **Stand on proven shoulders** — Prefer existing library files and router files over inventing new ones.
3. **Deterministic before model** — Strip to keywords → score from index → open one file → read one section → invoke model once. No wading.
4. **Small index, always true** — Every new fact gets a line in the router. A stale pointer is worse than no pointer.
5. **Prove it** — Test retrieval against a fresh session. If the brain isn't clearly cheaper, keep optimizing.

**Applied to Nexus:** When either AI needs a compliance rule, it reads from `nexus_aurea_cfr_library.json` — not from memory, not from training data. The JSON is the evidence. The model answers once, with the evidence attached.

---

## 7. COMMAND CENTER TARGET

Target interface: **RUBRIC Agentic OS-style** (dark theme, central neural globe, surrounding module ring)

Planned modules:
- Email Intake
- Calendar / Review Queue
- Skills Deck
- Routines Board
- Micro-Apps
- Shipment Review Queue

**Status:** NOT being built yet. Foundation (Skills + Memory + CFR Library) must be complete first.
**Build system:** Abacus AI will build the command center web app when ready.
**Rule:** The command center is a window — it reads the repo and the compliance library. It does not store truth. Artifacts stay files.

---

## 8. WHAT EACH SYSTEM DOES — HARD LINES

| Task | Abacus AI | Claude Code |
|------|-----------|-------------|
| Build new files | ✅ | ❌ |
| Structural QA / PR review | ❌ | ✅ |
| Push to GitHub | ✅ | ✅ |
| Webull / live trading data | ❌ (no connector) | ✅ |
| n8n workflow management | ✅ | ❌ |
| Scheduled tasks (platform) | ✅ | ❌ |
| Email / Gmail | ✅ | ❌ |
| Terminal / bash | ✅ | ✅ (on user's machine) |
| Compliance library maintenance | ✅ (builds) | ✅ (reviews) |
| Shipping paper review (live) | ✅ | ❌ |
| Deep repo code analysis | ❌ | ✅ |

---

## 9. RULES FOR CONFLICT RESOLUTION

If Abacus AI and Claude Code produce different answers to the same compliance question:
1. Check which JSON version each system was reading
2. The system reading the higher schema version is correct
3. If same version, Claude Code's structural read wins (it reads the file directly; Abacus may be working from context)
4. Log the conflict in the changelog — it means the library needs a clarification entry

If this file (`NEXUS_SHARED_CONTEXT.md`) conflicts with either system's private memory or CLAUDE.md:
- **This file wins**
- Update the private memory / CLAUDE.md to match
- Note the fix with a date

---

## 10. PLATFORM PLAN

| Platform | Role | Plan |
|----------|------|------|
| Abacus AI | Builder / Operator | $100/month (when credits allow) |
| Anthropic / Claude | Analyst / QA / Webull | $100/month |
| OpenAI / ChatGPT | — | Likely dropping |
| n8n | Execution layer | Self-hosted on user's machine |

---

## 11. NEXT BUILD AGENDA

1. ~~Push CFR library v1.0.1 to `dgr/02-49cfr/`~~ (tonight)
2. SDS lesson — 16 GHS sections, which apply to shipping review
3. Chain-of-Custody skill + document
4. Standard Operating Procedures (SOPs)
5. Encryption + security layer
6. Payment / banking configuration
7. Command center (after foundation complete)
8. IATA DGR 67th Edition integration (user has licensed copy)

---

_This file is maintained by Abacus AI and committed to the repo root._
_Claude Code: add a pointer to this file in your CLAUDE.md master router._
_Last editor: Abacus AI | 2026-09-09_
