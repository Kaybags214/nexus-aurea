# Audit — index

The working document-review system. Start here for anything about reviewing a shipping or
pharma document.

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

`.claude/skills/README.md` covers the shape and what is still to build.

## Intake and output

- `compliance-auditor/intake/` — submission point; `README.md` explains the flow
- `compliance-auditor/n8n-workflow-setup.md` — the self-hosted webhook
- `compliance-auditor/audit-reports/` — completed reports land here. **Currently empty**

## Proof of work — `audit-lab/`

- `audit-lab/README.md` — what the lab is for
- `audit-lab/dry-ice-un1845/dry-ice-review-checklist.md` — operator checklist; **outranks the
  dry-ice skill** where they differ
- `audit-lab/dry-ice-un1845/sample-dry-ice-audit-001.md` — a worked example
- `audit-lab/sample-findings/audit-findings-template.md` — findings shape
