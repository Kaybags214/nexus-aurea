# Nexus Aurea — master router

Kenya Bagwell, Nexus Aurea Inc. Pharma air freight compliance — IATA DGR, GDP/GMP cold chain,
customs — plus the company's own tax, market research and career infrastructure.

**This file is a map, not documentation.** Each area below points to a one-page index. Read the
index for the area you need, then the file it names. Do not scan the whole repository.

## Areas

| Area | What lives there | Index |
|---|---|---|
| **Audit** | The working document-review system: engine, skills, precedence, proof of work | `AUDIT.md` |
| **Reference** | Regulatory knowledge by lane: DGR, cold chain, pharma, customs, compliance | `REFERENCE.md` |
| **Templates** | Blank and reference forms: AWB, DGD, invoice, packing list, BOL | `TEMPLATES.md` |
| **Markets** | Public-company research, flow briefs, the screener package | `MARKETS.md` |
| **Business** | Business development, job search, resumes, leave-behind packets | `BUSINESS.md` |
| **Money** | Form 1120, bookkeeping, CPA questions, deadlines | `MONEY.md` |

The agentic OS itself — architecture, command centre, the ARMS mapping — is documented in
`docs/agentic-os/README.md`.

## Standing rules

1. **Official sources first.** Keep research and speculation separate and labelled.
2. **Never store unredacted customer documents.** Redact before anything is committed.
3. **Compliance work runs through the skills**, not ad-hoc prompting. Six exist in
   `.claude/skills/` — see `AUDIT.md`. They are governed by
   `compliance-auditor/skill-contract.md` and `compliance-auditor/standards-of-precedence.md`.
4. **No regulatory limit from memory.** Verify against the governing document, or record it as
   unverified. This applies to answers in chat as much as to skill output.
5. **Nothing here clears, certifies, releases or signs.** A qualified person does that.
6. **Build the system before chasing the opportunity.**

## The router rule

**When a file moves, an area changes, or a new project starts, update this router and the
affected index in the same turn.** A stale pointer is worse than no pointer — it sends a cold
session confidently to the wrong place.
