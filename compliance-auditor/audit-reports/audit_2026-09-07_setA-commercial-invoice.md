# Nexus Aurea — Compliance Audit

- **Audit date:** 2026-09-07
- **Auditor:** `commercial-invoice-review` skill — **first run against a real document**
- **Document type:** Commercial Invoice (handwritten), ship date 7/11/26
- **Seller:** Apex Inc., 654 Stone Ln., Stafford VA 22554 — contact Jimmy Hill
- **Buyer:** ABC Flyers, 456 Rockway Ln., Blacksburg VA 24060 — contact Steve Jay
- **AWB reference:** 771-221-2765
- **Source:** operator practice document set. Not a live shipment.

### What is right

- Both parties carry full address, named contact, telephone and email — more complete than most
  real invoices.
- Country of manufacture stated per line (USA, USA).
- **HS heading `2811.21` for carbon dioxide is plausible and correctly formatted** — six digits,
  and the heading is consistent with the goods described. Correctly done.
- Description references the same quantities as the declaration and AWB.

### 🔴 Critical findings

- **[C-1] Net weight reads "30kg" against 3.0 kg on the declaration and Air Waybill.** A factor
  of ten on a customs document. **Standard:** `standards-of-precedence.md` §4 — document
  consistency; §3 — destination customs has final say on valuation.
  **Fix:** confirm the true weight and restate. A tenfold overstatement inflates the declared
  basis and would be queried at entry.

### 🟡 Major findings

- **[M-1] No invoice number.** The field is blank. **Fix:** assign one — it is how the entry,
  the payment and the shipment are tied together.
- **[M-2] No Incoterm and no terms of sale.** The Terms of Sale field is blank, so the
  cost-and-risk split is undefined and the customs value cannot be built.
  **Standard:** `commercial-invoice-review` check 3. **Fix:** state the rule and the named
  place — e.g. "FCA Stafford VA, Incoterms 2020". Note that on an air shipment a sea-only term
  such as CIF or FOB would itself be a finding.
- **[M-3] No currency code.** Values are written as bare numbers. USD is presumable from a
  domestic US shipment but presumption is not declaration. **Fix:** state the currency.
- **[M-4] HS heading on line 2 is not a valid code.** Written as `A B2` against "Biological
  Substances category B". That is not an HS format — headings are numeric, six digits
  internationally. **Fix:** obtain the correct heading **from a licensed broker**.
  Per `commercial-invoice-review` check 4, this skill does not assign classifications; it
  reports that one is absent or malformed.
- **[M-5] Line arithmetic cannot be reconciled.** Line 1 shows a unit value that appears to read
  200 against a line total of 250.00; the subtotal figure is not legible with confidence.
  **Standard:** check 2 — every line total must equal quantity × unit price, and the invoice
  total must equal the sum of lines. **Fix:** restate legibly. Recomputation is the cheapest
  check at entry and it must reconcile exactly.
- **[M-6] Purpose of shipment blank.** Blank on a shipment containing a biological substance.
  Sale, sample, clinical trial material and return are valued and treated differently.
  **Fix:** state it.
- **[M-7] No payment terms.**
- **[M-8] Importer of record not identified**, and no tax or trade identifier for either party.
  On a US domestic movement this may not attach — but the field is on the form and it is blank.

### 🟢 Minor

- **[m-1]** "Total Units" reads 1 for each line while "No. of Packages" reads 2. If two packages
  each contain one unit, the units column should read 2. Ambiguous as written.
- **[m-2]** Insurance, freight, packing, handling and other all show 0.00 with no Incoterm to
  explain who bears them (see M-2).

### Cross-document

Reconciles with the declaration and AWB on parties, AWB reference, UN quantities and piece
count. The single break is the net weight (C-1).

### Cannot verify

- Whether `2811.21` is the correct heading for the goods as actually constituted — plausible and
  well-formed, but classification is the destination authority's determination.
- The line arithmetic and subtotal — handwriting legibility. Restate and re-audit.
- Whether an importer of record is required for this movement.

### Final verdict

- [ ] ✅ PASS
- [x] ⏸️ **HOLD FOR CORRECTION**
- [ ] ⛔ REJECT

**Reason:** A tenfold net weight discrepancy against the transport documents, and the commercial
terms — invoice number, Incoterm, currency, purpose — are absent, so the customs value cannot be
constructed from this document as written.

---

*Research/operations support, not legal advice, and not a customs classification. A licensed
broker determines HS classification. Practice document set.*
