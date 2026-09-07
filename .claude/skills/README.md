# Skills — the L1 layer

The audit engine in `compliance-auditor/AUDIT-ENGINE-PROMPT.md` is one large prompt that does
everything. These skills are the same competence cut into narrow, single-purpose units, which is
what makes the output repeatable: the same document reviewed twice produces the same findings,
because the method is written down rather than re-improvised each session.

| Skill | One job |
|---|---|
| `dry-ice-un1845` | Is the dry ice on this shipment documented correctly? |
| `awb-review` | Is this Air Waybill complete and internally consistent? |
| `dgd-check` | Is this Shipper's Declaration complete, correctly classified and signed? |

## Rules these all follow

1. **One task, one defined way.** "Verify dry ice net weight per package" is a skill. "Review
   this shipment" is not — that is the engine calling several skills.
2. **Precedence is not restated, it is cited.** `compliance-auditor/standards-of-precedence.md`
   is the single source. A skill that disagrees with it is wrong.
3. **Every finding names its standard.** A flag without a cited rule is not a finding.
4. **Unreadable is a valid answer.** "Cannot verify from image" beats a guess, always.
5. **Nothing clears a shipment.** Skills flag and correct. A qualified person signs.
6. **Each skill keeps a `learnings.md`.** Append after every run — what surprised you, what the
   skill missed, what to change. That file is how a skill's second month beats its first.

## Adding the next one

Still to build, in the order the build plan puts them:

- `commercial-invoice-review` — value, HS heading, Incoterms consistency
- `coa-review` — Certificate of Analysis against the product specification
- `excursion-assessment` — temperature excursion against the product label range
- `lithium-battery-section-II` — PI 965–970 Section II
- `hs-code-lookup` — classification research, destination-country first

Copy an existing skill's shape: frontmatter with `name` and `description` that says when to
trigger, a stated single job, ordered checks, an explicit "what you may not do", and the output
shape from `compliance-auditor/audit-report-template.md`.
