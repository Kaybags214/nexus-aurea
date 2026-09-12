# Service coverage — the website against the skills

`nexusaureainc.com` is a public promise. This file checks it against what
`.claude/skills/` can actually do. Reviewed 2026-09-08.

**A promise on the website is a specification.** Where the two disagree, either build the skill
or change the page — but do not discover the gap on an invoice.

## What the site promises

- Human-led documentation review and discrepancy flagging for **Class 3, 8 and 9** dangerous
  goods and temperature-sensitive pharmaceutical shipments
- Documents reviewed: Shipper's Declaration, Air Waybill and DG notations, commercial invoices,
  packing lists, **Safety Data Sheets**, temperature-control records, certificates of analysis,
  **chain-of-custody records**, cross-document consistency
- **$250** per shipment-document package, up to five standard documents, written discrepancy report
- **$100** corrected-package re-review
- Expedited available; complex or out-of-scope priced before work begins

## Coverage

| Promised | Skill | Status |
|---|---|---|
| Shipper's Declaration | `dgd-check` | ✅ tested on four real declarations |
| Air Waybill + DG notations | `awb-review` | ✅ tested, 9/9 on the fixture |
| Commercial invoices | `commercial-invoice-review` | ✅ one real run |
| Temperature-control records | `excursion-assessment` | ⚠️ built, never run |
| Certificates of analysis | `coa-review` | ⚠️ built, never run |
| Cross-document consistency | every skill's final check | ✅ found the top defect in Set B |
| **Packing lists** | — | ❌ **no skill** |
| **Safety Data Sheets** | — | ❌ **no skill, not on the build list** |
| **Chain-of-custody records** | — | ❌ **no skill** |

## The gap with a price on it

**The $100 corrected-package re-review is sold, and nothing implements it.**

It is not a repeat of the first review. It is a different job: take the findings from v1, take the
corrected package, and confirm **each finding was actually fixed** — while checking that the
correction did not introduce something new. A re-review that silently re-runs the original checks
will miss a Critical the client thinks they closed.

This is the first thing to build. It has a price attached, so a client can buy it today.

## Class coverage is uneven

The site sells three hazard classes. The repository's depth is not evenly spread across them.

| Class | Depth in the repo |
|---|---|
| **Class 9** | Strongest. `dry-ice-un1845`, `lithium-battery-section-2`, UN1845 and biologicals references |
| **Class 3** | Generic only. `dgd-check` handles any declaration; there is no Class 3 reference lane |
| **Class 8** | Generic only. Same |

`dgr/01-iata` and `dgr/02-49cfr` are both empty. The generic declaration checks do work on Class
3 and Class 8 — the practice declarations included UN1830 (Class 8) and UN1863 (Class 3), and
both were audited — but there is no class-specific knowledge to lean on when a question gets
harder than the form.

Not a blocker. Worth knowing which class a first client is likely to bring.

## What the site gets right, and it is not luck

Three lines match the system's own guardrails exactly:

> *"No shipment certification, tendering, or automatic clearance."*
> *"Findings are for review support only; the shipper remains responsible for classification,
> packaging, acceptance, and transport decisions."*
> *"human-led"*

That is `skill-contract.md` rule 5 stated in the client's language. The site and the machine
agree on the most important thing: **nothing here clears, certifies or signs.** Keep that
wording — it is the honest position and it is also the one that limits liability.

## Two things the site does not say, and should

**1. Nothing about confidentiality or data handling.** A pharma client will ask what happens to
their paperwork. `compliance/02-sops/data-handling.md` has the answer; the site does not carry
it. A short paragraph — where documents are held, how long, who processes them — is a
differentiator for a solo operator, not boilerplate.

This also matters for the standing rule that a client agrees to processing before their document
goes through any AI service. That agreement has to happen somewhere, and the site is where a
client first learns it is being asked.

**2. No turnaround time.** "Expedited review may be available for an additional fee" implies a
standard turnaround, but the standard is never stated. Every client asks. Decide it before one
does, and state it.

## Build order this implies

1. **`corrected-package-review`** — a priced product with nothing behind it
2. **`packing-list-review`** — promised, straightforward, and the reference template exists
3. **Run `coa-review` and `excursion-assessment` on real documents** — both are sold and neither
   has ever seen one
4. **SDS review** — promised and entirely unbuilt; decide whether to build it or drop it from the
   page
5. **Chain-of-custody** — same decision
