# Nexus Aurea 49 CFR Compliance Reference Library — Changelog

## v1.0.1 — 2026-09-09 — Document-control release

**v1.0.1 adds no regulatory coverage.** It corrects how the library is versioned, sourced,
cited and flagged. Eight Critical findings remain open and the library is still
**NOT RELEASED FOR AUDIT USE**.

### Source of record

`nexus_aurea_cfr_library.json` is authoritative. `nexus-aurea-cfr-library.md` is generated
from it by `tools/build_library.py` and must never be hand-edited.

```
python3 tools/build_library.py           # regenerate the Markdown
python3 tools/build_library.py --check   # fail if the Markdown has drifted from the JSON
```

This closes J-01 mechanically rather than by promise: the two artifacts can no longer diverge
without `--check` failing.

### Closed in v1.0.1

| ID | What changed |
|---|---|
| J-01 | JSON designated source of record; Markdown generated; drift check added |
| J-02 | Standing rule 3 now reads Pass / Fail / Warning / Unable to Verify / **Not Applicable**, matching the 16 checks and the status definitions that already used it |
| J-03 | The three `effective_date` Federal Register claims removed — including §173.140's implausible "unamended since 1993". Replaced per-part with `citation_verification: UNVERIFIED`. **No currency date is recorded**, because no primary-source check was performed |
| J-04 | §175.10 withdrawn from the cargo checks; retained in Part 175 with an explicit `scope_warning` that it covers passenger baggage only |
| J-05 | Scope now states the domestic/international boundary and that findings on international air must not be issued from this library alone |
| F-14 | Closed by generation — the Markdown now inherits the JSON's correct "emergency response telephone number" wording |
| F-17 | Document control block added: document number, author, technical reviewer, approver, effective date, review cycle, change history. **Approver is UNASSIGNED** — the document cannot be released until a named human fills it |
| F-18 | PH-005 moved out of the active checklist into `pending_checks`, blocked on the IATA DGR 67th Edition |
| F-20 | Worked example now varies sequence only; the hazard class of UN2744 is no longer altered |

### Held, not closed

| ID | What changed |
|---|---|
| F-01 | The wrong citation is gone, but the right one (§173.217) is not in the library, so C9-002 and PH-001 now carry `source: PENDING` and return Unable to Verify. **The checks are held, not fixed** — F-01 closes only when F-02 closes |
| F-09 | Class 3 packing group table carries a warning that its source points at the Hazardous Materials Table rather than §173.121, and that the PG I flash point threshold is disputed |
| F-12 | OECD TG 439 moved from `test_methods_accepted` to `test_methods_under_review` with a note that it is an irritation method. Moved rather than deleted because F-12 is Unable to Verify — the accepted list in §173.137 has not been checked |

### Still open — these block release

F-02 (§173.217 absent), F-03 (lithium batteries — zero checks), F-04 (no temperature values),
F-05 (no cross-document reconciliation), F-06 (Subparts D–H), F-07 (§175.30, §175.33 NOTOC,
§175.75), F-08 (pharma checks without authority), plus F-10, F-11, F-13, F-15, F-16, F-19.

Each is now represented in the library itself as a `missing_sections` stub naming the section,
what it covers, and its finding ID — so a user meets the gap at the point of use rather than
only in a separate report. An `open_findings` register carrying all 25 findings is embedded in
the JSON and rendered near the top of the Markdown.

### Why no content was added

Every remaining finding requires regulatory text this environment cannot reach — `ecfr.gov`,
`govinfo.gov` and `law.cornell.edu` are all blocked by network egress policy. Writing those
sections from memory would breach the library's own Standing Rule 5 ("Never invent a missing
regulation") at a larger scale than any defect found so far. Two new standing rules were added
to make that boundary explicit:

> 7. Never state or imply that a citation in this library has been verified against primary
>    source while `cfr_verification_status` reads NOT VERIFIED.
> 8. A check whose source is marked PENDING is not an active check. It returns Unable to
>    Verify and must not be scored Pass or Fail.

### Next step

One primary-source pass from an environment with eCFR access, working the ❓ list in
`audit-findings/cfr-library-v1.0-audit-findings.md`. That unblocks the content work; nothing
else does.

### Files

| Path | Role |
|---|---|
| `nexus_aurea_cfr_library.json` | Source of record |
| `nexus-aurea-cfr-library.md` | Generated — do not edit |
| `tools/build_library.py` | Generator and drift check |
| `archive/nexus-aurea-cfr-library-v1.0-as-received.md` | v1.0 Markdown as received, unaltered |
| `audit-findings/` | Full findings detail |

---

## v1.0 — 2026-09-09 — Initial build

49 CFR Parts 171, 172 Subpart C, 173 (Classes 3, 8, 9), 175; pharmaceutical /
temperature-sensitive section; standard document audit scope. Built by Abacus. Delivered as
two artifacts — JSON and Markdown — which carried the same version number and divergent
content; see J-01.
