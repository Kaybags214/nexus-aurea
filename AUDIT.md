# Audit — index

The working document-review system. Start here for anything about reviewing a shipping or
pharma document.

## What is sold vs what is built

`compliance-auditor/service-coverage.md` — the website's promises checked against the skills.
Three promised document types have no skill, and the $100 re-review is priced with nothing
implementing it. Read before quoting a client.

## Governance — read before any review

| File | What it decides |
|---|---|
| `compliance-auditor/standards-of-precedence.md` | Which rule wins when two disagree. Four chains plus the severity mapping. **The authority.** |
| `compliance-auditor/skill-contract.md` | Ground rules every skill obeys, and the sidecar-log spec |
| `compliance-auditor/audit-report-template.md` | The exact output shape every audit produces |
| `compliance-auditor/AUDIT-ENGINE-PROMPT.md` | The system prompt for chat and the n8n vision node |

## Skills — `.claude/skills/`

Each is a router: `SKILL.md` plus a `checks/` folder inside each skill, read one at a time.

| Skill | One job |
|---|---|
| `awb-review` | Air Waybill completeness and consistency; check-digit arithmetic |
| `dgd-check` | Shipper's Declaration classification, aircraft limitation, signature |
| `dry-ice-un1845` | Dry ice identity, net kg per package, marking, cross-document weight |
| `excursion-assessment` | Cold-chain excursion against the labelled range; decision package |
| `coa-review` | Certificate of Analysis completeness and lot traceability |
| `commercial-invoice-review` | Customs sufficiency, arithmetic, Incoterms, HS plausibility |
| `corrected-package-review` | Closure of prior findings, and regressions the correction introduced |
| `lithium-battery-section-2` | PI 965-970, which section applies, state of charge, lithium battery mark |

`.claude/skills/README.md` covers the shape and what is still to build.

## Intake and output

- `compliance-auditor/intake/` — submission point; `README.md` explains the flow
- `compliance-auditor/gmail-intake-setup.md` — **client documents from `kenya@nexusaureainc.com`
  into the laptop.** Client store, never git, replies as drafts only
- `compliance-auditor/n8n-headless-setup.md` — wires the intake page to the skills via
  Claude Code headless on the laptop. The one that actually runs `.claude/skills/`
- `compliance-auditor/n8n-workflow-setup.md` — the older API-node webhook. Runs the monolithic
  prompt, no repo access, no skills. Fallback when the laptop is off
- `scripts/audit-document.sh` — the headless runner n8n calls
- `compliance-auditor/audit-reports/` — completed reports and their sidecar logs land here

## Proof of work — `audit-lab/`

- `audit-lab/README.md` — what the lab is for
- `audit-lab/dry-ice-un1845/dry-ice-review-checklist.md` — operator checklist; **outranks the
  dry-ice skill** where they differ
- `audit-lab/dry-ice-un1845/sample-dry-ice-audit-001.md` — a worked example
- `audit-lab/sample-findings/audit-findings-template.md` — findings shape
