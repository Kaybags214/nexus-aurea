# Nexus Aurea CFR Library — Changelog

## v1.0.1 — 2026-09-09

**Trigger:** Claude Code PR #8 — Structural QA delta report identifying critical divergences between
`nexus_aurea_cfr_library.json` and `nexus_aurea_cfr_library.md`, plus regulatory accuracy issues.

**JSON is the source of record. All fixes applied to JSON first; Markdown regenerated from JSON.**

---

### Fix 1 — Standing Rule 3: Added "Not Applicable" disposition

**File:** `nexus_aurea_cfr_library.json` → `library_meta.standing_rules[2]`

**Before:**
```
"Mark each finding: Pass / Fail / Warning / Unable to Verify."
```

**After:**
```
"Mark each finding: Pass / Fail / Warning / Unable to Verify / Not Applicable."
```

**Why critical:** 16 audit checks across the library use `not_applicable` as a valid disposition.
Without "Not Applicable" in the standing rules, auditors following the rules literally had no
sanctioned disposition for non-applicable checks — the failure mode is forcing a Pass on checks
that should be skipped. This is the worst possible direction for a compliance tool.

---

### Fix 2 — Source-of-record declaration added to library_meta

**File:** `nexus_aurea_cfr_library.json` → `library_meta`

**Added fields:**
- `"schema_version": "1.0.1"`
- `"source_of_record": "nexus_aurea_cfr_library.json"`
- `"authorship_note"` — instructs editors not to edit Markdown directly
- `"integrity_note"` — instructs structural diff between JSON and MD on any edit
- `"last_updated": "2026-09-09"`
- `"version"` bumped from `"1.0"` → `"1.0.1"`

**Why:** Without a declared source of record, three-system alignment (Abacus AI + Claude Code + n8n)
has no single truth anchor. Any editor could modify the MD and create the exact divergence Claude
Code flagged in PR #8.

---

### Fix 3 — Removed stale Federal Register effective_date citations; replaced with ecfr_current_as_of

**Files:** `part_173_class_3`, `part_173_class_8`, `part_173_class_9`

**Replaced field name:** `"effective_date"` → `"ecfr_current_as_of": "2026-09-09"` + `"effective_date_note"`

**Why critical for §173.140 specifically:** The original cite `"Amended 58 FR 33305, June 16, 1993"`
was over 30 years stale. Part 173 has been substantially revised via the HM-215 rulemaking series
and multiple subsequent PHMSA actions since 1993. A stale FR cite in an audit tool can stop auditors
from checking ecfr.gov for current requirements — a serious compliance risk. The fix removes the
false confidence of a specific FR cite and directs auditors to ecfr.gov for currency.

Note: The 2011 and 2020 FR cites for Class 3 and Class 8 were also unverified — all three replaced
consistently.

---

### Fix 4 — Removed §175.10 citations from commercial cargo checks

**Files:** `part_173_class_9` (C9-002), `pharma_temperature_sensitive` (PH-001 and relevant_sections)

**C9-002 source:**
- Before: `"49 CFR §173.140(b), §175.10(a)(10)"`
- After: `"49 CFR §173.140(b)"` + `"source_note"` explaining the removal

**PH-001 source:**
- Before: `"49 CFR §173.140, §175.10(a)(10)"`
- After: `"49 CFR §173.140(b)"` + `"source_note"` explaining the removal

**pharma_temperature_sensitive.relevant_sections:**
- Removed: `"§175.10 (air transport exceptions — dry ice passenger limits)"`
- Added: `"relevant_sections_note"` explaining why §175.10 is scoped to passenger/crew exceptions only

**Why:** §175.10 governs _passenger, crewmember, and air operator_ exceptions only. It is not a
commercial cargo documentation requirement. Citing it in commercial cargo audit checks (C9-002,
PH-001) was a scope error that could mislead auditors into applying passenger carry-on limits to
cargo shipments. The §175.10 dry_ice_rule is correctly retained under `part_175_air_transport` for
its intended purpose: checking passenger-carried dry ice.

---

### Fix 5 — OECD Test No. 439 label corrected and expanded

**File:** `part_173_class_8.test_methods_accepted`

**Before:**
```
"OECD Guideline Test No. 439 — In Vitro Skin Irritation (RHE)"
```

**After:**
```
"OECD Guideline Test No. 439 — In Vitro Skin Irritation: Reconstructed Human Epidermis (RHE)
Test Method — NOTE: TG 439 is an irritation (not corrosion) test. It is used to support a finding
of non-corrosivity; if the result indicates corrosive potential, assign PG II minimum or retest
with TG 430/431/435."
```

**Also expanded:** TG 404, 430, 431, 435 labels to include full OECD titles.

**Why:** TG 439 is an irritation assay, not a corrosion test. Listing it flat alongside TG 430/431/435
(which are corrosion tests) under "test_methods_accepted for Class 8 corrosive classification" implies
it can confirm corrosivity, which it cannot. The corrected label makes the use-case and limitation
explicit so auditors applying it understand its proper role.

---

### Fix 6 — Scope declaration expanded

**File:** `library_meta.scope`

**Before:**
```
"U.S. domestic hazardous materials transport — DG Classes 3, 8, 9 and pharmaceutical/temperature-sensitive shipments"
```

**After:**
```
"U.S. domestic and international air — DG Classes 3, 8, 9 and pharmaceutical/temperature-sensitive
shipments. Note: International air transport is governed by IATA DGR 67th Edition (pending
integration). All air freight findings from 49 CFR Part 175 are domestic scope only."
```

**Why:** The library already contains Part 175 air transport checks. The scope declaration must
accurately reflect this. The note about IATA DGR governs international scope prevents auditors
from applying domestic 49 CFR air rules to international air shipments.

---

### Fix 7 — Markdown regenerated from corrected JSON

**File:** `nexus_aurea_cfr_library.md` — fully regenerated from corrected v1.0.1 JSON

**Standing rules in MD now match JSON exactly** (7-rule vs 6-rule discrepancy resolved — both
now have 6 rules including the corrected Rule 3 with Not Applicable).

All other divergences found in Claude Code PR #8 are resolved by regeneration:
- Scope declaration updated
- OECD 439 label corrected
- §175.10 removed from commercial cargo sections
- ecfr_current_as_of replaces effective_date
- Version, schema_version, source_of_record, integrity_note all appear in MD header

---

### Fix 8 — Schema version + integrity discipline added

**File:** `library_meta`

**Added:** `"schema_version": "1.0.1"`, `"integrity_note"` (run structural diff JSON↔MD after any edit)

**Convention established:** Schema version must be incremented on any structural change to the
library (new check_id, new section, new field). Markdown is always regenerated from JSON — never
edited manually.

---

## Files in This Release

| File | Status |
|------|--------|
| `nexus_aurea_cfr_library.json` | ✅ Updated — v1.0.1, all 8 fixes applied |
| `nexus_aurea_cfr_library.md` | ✅ Regenerated from v1.0.1 JSON |
| `nexus_aurea_cfr_library_changelog.md` | ✅ This file |

## Push Instructions for Claude Code

Apply to repo path: `dgr/02-49cfr/`

Replace:
- `nexus_aurea_cfr_library.json`
- `nexus_aurea_cfr_library.md`

Add:
- `nexus_aurea_cfr_library_changelog.md`

PR description: "v1.0.1 — Apply 8 structural and regulatory accuracy fixes from PR #8 QA delta;
regenerate MD from JSON; establish JSON as declared source of record."
