# Skills — the L1/L2 layer

`compliance-auditor/AUDIT-ENGINE-PROMPT.md` is one large prompt that does everything. These
skills are the same competence cut into narrow units, so the same document reviewed twice
produces the same findings.

Structure follows the ARMS guide's Skills **Level 2** pattern: `SKILL.md` is a short router,
the detail lives in a `checks/` folder inside the skill, and the router tells the agent to read **only** the file that
matches the job.

| Skill | One job |
|---|---|
| `awb-review` | Is this Air Waybill complete and internally consistent? |
| `dgd-check` | Is this Shipper's Declaration complete, correctly classified and signed? |
| `dry-ice-un1845` | Is the dry ice on this shipment documented correctly? |
| `excursion-assessment` | How far outside its range did this product go, and what does a QP need? |
| `coa-review` | Is this Certificate of Analysis complete and traceable to the shipment? |
| `commercial-invoice-review` | Is this invoice sufficient for customs and internally consistent? |
| `lithium-battery-section-2` | Which UN number, PI and section apply, and does the shipment meet them? |
| `corrected-package-review` | Were the prior findings actually closed, and did fixing them break anything? |

## The shape

```
.claude/skills/<name>/
├── SKILL.md          router — triggers, check table, the contract. Under 60 lines.
├── checks/          one file per check group
│   ├── 01-....md     one file per check group, read only when reached
│   └── 02-....md
└── learnings.md      appended after every run
```

## Rules all of them follow

1. **One task, one defined way.** "Verify dry ice net weight per package" is a skill.
   "Review this shipment" is not — that is the engine calling several skills.
2. **Shared rules are cited, never restated.** `compliance-auditor/skill-contract.md` holds the
   ground rules and the sidecar-log spec; `standards-of-precedence.md` decides conflicts;
   `audit-report-template.md` is the output shape. A skill that contradicts them is wrong.
3. **No regulatory limit from memory.** Packing instruction quantities, specification limits,
   shelf-life minima: verified against the governing document, or recorded as unverified.
4. **Unreadable is a valid answer.** "Cannot verify from image" beats a guess, always.
5. **Nothing clears, releases or signs.** Skills flag and correct.
6. **Every report gets a sidecar JSON** — the audit trail that lets a finding be defended later.

## Conventions that are ours, not the guide's

- `learnings.md` per skill, rolled up into `docs/agentic-os/second-brain.md` when a lesson
  reaches beyond the skill that found it
- The sidecar log, adapted from the `/generate` guide's media log into an audit trail
- `checks/` as the sub-file name

## Still to build

`packing-list-review`, `sds-review`, `chain-of-custody-review` — all three promised on the
website with nothing behind them, see `compliance-auditor/service-coverage.md`. Then
`bol-review` (ocean), `hs-code-research`, `gdp-record-review`, `cbp-entry-review`.

Copy an existing skill's shape. Router under 60 lines, one file per check group, contract
cites `skill-contract.md` rather than repeating it.
