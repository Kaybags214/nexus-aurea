# Nexus Aurea — Security & Reliability Hardening Pass

**Date:** 2026-09-06 · **Status: PROPOSALS ONLY.**

Nothing in the live n8n Cloud tenant was published, activated, deleted, overwritten, or altered.
This session had no n8n credential and no n8n API access, so no live workflow could be reached,
inspected, or changed. Every node map here is a proposal to review before anything is applied.

## Read in this order

| File | State |
|---|---|
| `00-inspection-report.md` — what exists, what doesn't, the evidence base | complete |
| `01-backup-and-export-sop.md` — run this before any change | complete |
| `02-hardening-report.md` — findings + proposed node maps, workflow by workflow | complete |
| `03-review-envelope-contract.md` — the structured output contract | complete |
| `04-approval-gate/human-approval-exception-gate.draft.json` — importable, inactive, credential-free | complete |

## Not written yet — session ended early

- `schemas/review-envelope.schema.json` and the worked example (referenced by `03`)
- `04-approval-gate/README.md` — gate spec and reuse notes
- `05-portal-predeploy-checklist.md` — client-intake portal pre-deployment gate
- `06-rnd-multifamily-sandbox-concept.md` — Autonomous Multifamily Operations Sandbox concept note

`03-review-envelope-contract.md` §4 and §7 describe the schema and example in enough detail to
finish them, and `02-hardening-report.md` §7 carries the prohibited-actions policy the gate enforces.

## The five findings that matter most

1. **Unredacted live document content is committed to GitHub** — `Nexus-Core/dg-reviews/class-3/2026-09-05_203737.md`
   carries a real shipper name/address, consignee name/address, named signatory and working
   emergency phone number. (`00` §3.2 D1, `02` C-1, remediation options in `02` §6.)
2. **A document was reviewed under the wrong class and filed anyway** — a declaration carrying only
   UN1845 (Class 9) and a Division 6.2 line produced a full "Class 3" review, committed to
   `class-3/`. (`00` §3.2 D2, `02` C-2, fix F-5.)
3. **No machine-readable status field exists** — nothing downstream can branch; no gate can be
   enforced. This blocks every other control. (`00` §3.2 D3, `02` C-3, fix F-6.)
4. **No traceability from artifact to source document** — the header emits a form-field key, not a
   filename or hash. (`00` §3.2 D4, `02` C-4, fix F-3.)
5. **No backup of any workflow exists anywhere.** (`01`.)

## The AI layer is sound — do not rebuild it

The review engine refuses to infer, carries per-field read confidence, and caught real shipper
errors on live documents. The defects are in the plumbing — routing, output contract, redaction,
traceability. Harden the pipe; leave the engine alone. (`00` §3.1.)

## Open questions

- **Market Watch** appears to be a claude.ai Routine, not an n8n workflow. Which is live?
- **Physical AI — Shipment Capture Sandbox** has no definition, no output, no design note anywhere.
  Does it exist yet?
- **Compliance Auditor** is documented with a full node map but isn't in the list of five. Built,
  folded in, or abandoned?
- **Clock reliability** — `market-watch/ROUTINE-PROMPT.md` says the environment clock "has been
  observed running days behind". Every `dg-reviews/` filename and `Generated:` header comes from a
  clock. (`02` F-M2.)
