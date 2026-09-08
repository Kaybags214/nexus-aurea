# Audit Report Template

The exact output shape every audit produces. Saved to `compliance-auditor/audit-reports/` as
`audit_YYYY-MM-DD_<doctype>.md`. Copy this structure for both chat and n8n outputs.

---

## Nexus Aurea — Compliance Audit

- **Audit date:**
- **Auditor:** Compliance Auditor (Nexus Aurea) — reviewed by Kenya Bagwell
- **Document type(s):**
- **Governing reference(s):** (e.g. `templates/02-shipper-declaration/…`, `pharma/01-gdp-gmp/…`)
- **Shipper:**
- **Consignee:**
- **Origin → Destination:**
- **Mode:** (air / ocean / ground)
- **Commodity:**
- **Temperature range:** (if cold chain)
- **Dangerous goods involved:** (UN number(s) / none)

### Extracted fields

| Field | Value read | Expected | Source | OK? |
|-------|-----------|----------|--------|-----|
|  |  |  |  |  |

*(Mark any field that can't be read from the photo as "cannot verify from image.")*

### 🔴 Critical findings — shipment does NOT tender until fixed

- **[C-1]** _Finding._ **Standard:** _cited rule/level._ **Fix:** _…_

### 🟡 Major findings — correct before tender

- **[M-1]** _Finding._ **Standard:** _…_ **Fix:** _…_

### 🟢 Minor findings — cleanup / best practice

- **[m-1]** _Finding._ **Standard:** _…_ **Fix:** _…_

### Cross-document consistency (only if multiple documents submitted)

| Check | AWB/BOL | Invoice | Packing list | DGD | Match? |
|-------|---------|---------|--------------|-----|--------|
| Shipper |  |  |  |  |  |
| Consignee |  |  |  |  |  |
| Piece count |  |  |  |  |  |
| Gross weight |  |  |  |  |  |
| UN number / PSN |  |  |  |  |  |
| Dry ice net kg |  |  |  |  |  |
| Reference / AWB no. |  |  |  |  |  |

### Corrected version

> Restated document with fixes applied. Each change tagged `[CORRECTED: was X → now Y]`.
> Each item you can't supply tagged `[NEEDS INPUT: …]`.

### Final verdict

- [ ] ✅ **PASS** — clear to tender
- [ ] ⏸️ **HOLD FOR CORRECTION** — fix the items above, then re-audit
- [ ] ⛔ **REJECT — DO NOT TENDER**

**Reason (one line):**

---

*Research/operations support, not legal advice or a certifying signature. A qualified person signs
the actual document before tender.*
