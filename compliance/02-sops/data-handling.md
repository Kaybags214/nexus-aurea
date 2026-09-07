# Data Handling — client documents

Nexus Aurea reviews other companies' regulated shipping paperwork. That paperwork is their
commercial data, not ours. This file is the standing position on what happens to it.

It exists because a rule this repository carried until 2026-09-07 does not work.

## The rule that failed

`CLAUDE.md` said: *redact before anything is committed.*

That is sound for practice documents and **impossible for real ones.** Cross-document checking
*is* matching shipper, consignee, piece count and weight across the AWB, the declaration and the
invoice. Strip the party names and the check cannot run. The names are not metadata around the
evidence — they **are** the evidence.

So redaction is not the control. Separation is.

## The split

Two kinds of work, handled differently, and never mixed.

### Practice and proof-of-work — repository is fine

Invented parties. `Apex Inc.`, `ABC Flyers`, fictional addresses. The whole point is that it can
be shown to a prospective client or employer.

Lives in `audit-lab/` and `compliance-auditor/audit-reports/`. Committed, pushed, public to
anyone with repository access. Good.

### Real client work — never touches the repository

A real client's documents **and the reports about them** stay out of git entirely.

This is stricter than it first appears, and the reason is worth stating: **the report is as
sensitive as the document.** It names the shipper, the consignee, the commodity, the AWB number,
the declared value. A findings report on a real shipment is a description of that client's
business, and committing it is the same disclosure as committing the document.

| | Client document | Report about it |
|---|---|---|
| Enters git | **Never** | **Never** |
| Where it lives | Encrypted store outside the repo | Same store |
| Who sees it | Operator, and the client it belongs to | Same |
| Deleted | Per retention below | Per retention below |

## Where client work lives

Outside the repository, on encrypted storage, in a directory the repository cannot reach:

```
~/nexus-aurea-client/          <- NOT inside ~/nexus-aurea
  incoming/                    <- as received
  reports/                     <- findings and corrected copies
  delivered/                   <- sent to the client, awaiting retention expiry
```

**Encryption at rest is a requirement, not a preference.** Options depend on the machine —
a `gocryptfs` mount, a LUKS container, or per-file `age` encryption all satisfy it. Verify what
is available before relying on any one of them; full-disk encryption alone is not sufficient if
the machine is left unlocked.

`docs/cloud-architecture.md` already lists "Encryption at Rest and in Transit" as a guiding
principle. This is where that principle stops being aspirational.

## Retention

**Default: delete 30 days after delivery.** Both the document and the report.

The reasoning: the client has their copy, the work is paid, and every additional day of storage
is risk without benefit. A client who wants longer retention can ask, and that becomes a term of
the engagement rather than a default.

What survives deletion: a line in a work log — date, client, document type, verdict, invoice
reference. No party names, no shipment detail, no findings. Enough to prove work happened and
bill for it; not enough to disclose anything.

## Third-party processing

Documents are read by AI services. That is a disclosure to a third party and clients are
entitled to know which ones.

- **Name every service** a document passes through. Adding a second one doubles what has to be
  explained and contracted for; it should earn that cost.
- **Check each vendor's data-retention position** before real client work goes through it, and
  record what it says with the date checked.
- **Never send a real client document to a vendor before the client has agreed** to that
  processing.

## What this file is not

**This is not legal advice, and it is not a contract.** Whether Nexus Aurea needs a data
processing agreement, what its liability is, and what a client contract must say are questions
for a lawyer. Pharma clients will eventually ask them.

This file governs practice. It does not create legal cover.

## The rule in one line

**Invented parties go in git. Real ones never do — not the document, not the report.**
