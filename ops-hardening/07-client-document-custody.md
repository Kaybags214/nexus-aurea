# 07 — Client Document Custody

**Date:** 2026-09-06
**Status:** Decision guidance. No store has been selected, provisioned, or configured.

Answers the open question from the hardening session: *where do client documents live, once Nexus
Aurea is handling real shipper's declarations, air waybills, bills of lading, and commercial
invoices carrying names, addresses, and phone numbers?*

The current answer is "a laptop hard drive, because GitHub is not appropriate for it." The first
half of that is a correct instinct. The second half does not follow.

---

## 1. The premise needs one correction

**Keeping documents on a local laptop drive is not inherently more secure than a cloud store. It is
differently exposed.** Not pushing client documents to GitHub is right. Concluding that a laptop
drive is therefore the safe destination is a different claim, and it does not hold — because a
laptop drive fails on the three questions a client or an auditor will actually ask:

- **"Who accessed my documents, and when?"** A laptop cannot answer this. There is no access log. A
  business-tier cloud store or object store with access logging can answer it in seconds.
- **"Where is your backup?"** One drive failure loses records you are legally required to retain.
  A compliance obligation you cannot meet because the disk died is still an unmet obligation.
- **"What is your retention schedule, and what enforces it?"** Nothing on a laptop enforces
  "delete at 24 months," and nothing prevents deletion of a record under legal hold.

None of this means stop using the laptop. It means the laptop is a **working copy**, not the
**system of record**. Those are different roles and the distinction is the whole point of this
document.

---

## 2. Retention is the constraint that decides this

This is not a preference question. Storage duration is set by regulation, and the figures are long
enough that a single unbacked drive is not a candidate.

| Driver | Requirement | Verify against |
|---|---|---|
| Hazmat shipping papers — **offeror** | Retain a copy or electronic image **2 years** after the shipping paper is given to the initial carrier; **3 years** for hazardous waste | **49 CFR 172.201(e)** — confirm current text |
| Hazmat shipping papers — **carrier** | Shorter, typically 1 year; varies by mode | 49 CFR 174.24 / 175.30 / 176.24 / 177.817 |
| Air DG documentation | Minimum retention set by the operator and the State; the DGD travels with the shipment and a copy is retained | IATA DGR / ICAO TI; check the operator variation |
| GDP / GMP distribution records | Longer — **5 years** is the common working figure | EU GDP 2013/C 343/01; FDA 21 CFR 211.180 |

Verify each of these against the current text before writing them into a retention schedule. They
are cited here to establish the *shape* of the requirement, not as a compliance determination.

**The operative number: you need a system that reliably holds a client's shipping papers for two to
five years and produces them on demand.** That single fact eliminates an unbacked local drive as the
system of record, independent of any security argument.

---

## 3. The split that solves it

This is F-7 from `02-hardening-report.md`, stated as a storage architecture rather than a workflow
node. **Two tiers, not one store.**

### Tier 1 — GitHub holds the de-identified compliance record

| Included | Excluded |
|---|---|
| `submission_id` | Shipper / consignee names |
| Document `sha256` hash | Any street address |
| Status, confidence | Phone numbers, emails |
| Discrepancy *types* + cited standards | Signatory names, signatures |
| Missing-information *types* | Commercial values |
| Evidence **locators** — `page 1, quantity column, line 1` — and legibility | Quoted document text |
| Gate decision, reviewer identity, timestamps | Source PDFs, photos, any binary |

This is what makes the hash load-bearing. The git record proves **which** document was reviewed and
**what was found in it**, without containing the document. It stays fully auditable, fully
diffable, and contains nothing a client would object to.

An evidence locator survives redaction intact. `"page 1, quantity column, line 1 — legibility:
medium"` is completely reviewable by a qualified person without reproducing the shipper's address —
which is exactly why the envelope contract separates `locator` from `quote`
(`03-review-envelope-contract.md` §4).

### Tier 2 — a real document store holds the documents and the extracted values

Source PDFs and photographs, and every extracted field value. **Never git.**

---

## 4. Choosing Tier 2

| Option | Fits | Honest weakness |
|---|---|---|
| **Encrypted local + 3-2-1 backup** — FileVault/BitLocker, plus an encrypted offsite copy | The working copy you already have | No access log, no enforced retention, manual DR. Adequate as a working copy; not adequate as the system of record. |
| **Business cloud + signed DPA** — Box, Egnyte, Tresorit, Google Workspace or M365 Business tier | Humans browsing and handling documents | The **consumer tier will not do** — audit logs, retention policy, and legal hold are business-tier features. Tresorit and Proton are end-to-end encrypted, so the provider cannot read content. |
| **Object storage** — S3 or Backblaze B2, server-side encryption, **Object Lock**, access logging | **The n8n pipeline** — it needs a programmatic destination | Requires setup discipline. Costs pennies per month at this volume. Object Lock gives WORM retention, the strongest available answer to "prove this record was not altered after the fact." |
| **Self-hosted** — Nextcloud on a VPS | Maximum control | You become the security team, the patching team, and the backup team. For a small operation this is usually a net downgrade in practice, not an upgrade. |

**Recommendation: object storage for the pipeline, a business cloud drive for the humans, laptop
stays as the working copy.**

The reason is structural, not preferential: **n8n Cloud cannot write to a laptop hard drive.** The
workflow runs in a cloud tenant and needs a reachable, authenticated destination. So Tier 2 has to
exist as a network-addressable store regardless of what is used day to day — the only question is
which one.

Whichever is chosen, it must support all four of:

1. Encryption at rest and in transit.
2. Per-user access control and an **access audit log**.
3. Retention policy **and** legal hold — these conflict by design, and the retention schedule is
   what resolves the conflict.
4. Deletion on request, and a documented procedure for performing it.

---

## 5. The item that gates all of it

Storage is the second question. The first is that **these workflows send client documents to a
third-party AI API.**

`compliance-auditor/n8n-workflow-setup.md` already states the rule: *"Do not run real customer
documents with confidential data through a third-party API without the customer's agreement."*

Before any client document enters the pipeline, three things need to exist in writing:

1. **Client consent** covering AI processing of their shipping documents — naming that a third-party
   model provider processes the content.
2. **The provider's data-handling and retention terms**, confirmed and referenced in that agreement.
   Do not rely on a recollection of what the terms say; get the current terms.
3. **A written retention schedule** — how long each document class is held, when it is deleted, and
   how legal hold overrides deletion.

That third document is the one that makes the whole arrangement defensible, and it is also the one
that tells you which Tier 2 features you actually need. Write it before provisioning a store, not
after.

---

## 6. Do this regardless of which store is chosen

The DG workflows **currently commit extracted document content to GitHub** — finding C-1 in
`02-hardening-report.md`. The 2026-09-05 Class 3 artifact contains a real name, street address, and
working phone number.

Today that is survivable because it is Nexus Aurea's own paperwork. The moment a client's document
runs through the same unchanged pipeline, it is not.

**Turn off the field-value commit before the first client document, not after the storage question
is settled.** These are independent changes. F-7's allow-list redaction split can ship while Tier 2
is still being chosen — the public record is well-defined on its own, and until Tier 2 exists the
working copy simply stays local. That ordering costs nothing and closes the exposure now.

---

## 7. Sequence

| # | Step | Blocked by |
|---|---|---|
| 1 | Stop committing field values to git (F-7 allow-list) | Nothing — do this first |
| 2 | Write the retention schedule | Nothing |
| 3 | Draft the client agreement, incl. AI processing consent | Step 2 |
| 4 | Confirm the AI provider's data-handling terms in writing | Nothing |
| 5 | Select and provision Tier 2 | Steps 2 and 4 |
| 6 | Point the workflow's document output at Tier 2 | Step 5 |
| 7 | First real client document | Steps 1–6, all complete |

Steps 1, 2 and 4 can start immediately and none of them requires the storage decision to be made.

---

## 8. Scope note

This is operational guidance on document custody, not legal advice. The retention figures in §2 are
starting points to verify against current regulation, and a client agreement covering AI processing
of third-party commercial documents should be reviewed by counsel before it is used.
