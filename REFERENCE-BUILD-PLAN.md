# Reference build plan — what to write, in what order

What to add to the knowledge lanes, ordered by what the business actually sells. Written
2026-09-08 for the next working session.

## Read this first — do not copy the DGR

The IATA DGR is copyrighted. Do not transcribe tables, packing instructions, or the alphabetical
list into this repository.

**Write the operator's own work instead:**

| Write this | Not this |
|---|---|
| "PI 954 quantity limit is in DGR §5, table 5.x. Verified 2026-09-08 against 67th ed.: **N kg**" | The packing instruction reproduced |
| "For a Class 3 PG II liquid, check the passenger column before accepting the aircraft marking" | The Class 3 quantity table |
| "UN1263 is paint related material; UN1863 is aviation turbine fuel. Both Class 3, both PG II — the class column will not catch a transposition" | The alphabetical list |
| "Common finding: PG supplied where the entry has none" | — |

A **pointer plus a verified value plus the edition it came from** is more useful than a copy, and
it is the operator's own work. Stamp the edition beside every figure so staleness is visible
when the 68th edition lands.

## Priority 1 — the classes actually sold

The site sells Class 3, 8 and 9. Depth exists only for Class 9.

### `dgr/01-iata/` — the map
- Which DGR section holds what, so a lookup is one hop
- The columns of the alphabetical list, in order, and what each governs
- How to read a packing instruction entry
- Where state and operator variations live and how to check them

### Class 3 — flammable liquids
- Packing groups and what separates them
- Which packing instructions apply, passenger vs cargo
- **UN numbers that are one transposition apart and share a class** — UN1263 / UN1863 is the live
  example from the practice set, and it is exactly the error the column checks cannot catch
- Common findings on Class 3 declarations

### Class 8 — corrosive materials
- Packing groups
- Inner packaging compatibility — the UN1830 practice declaration said "1 inner bottle" without
  the material, and that is the finding this lane should make obvious
- Which packing instructions, passenger vs cargo

### `dgr/04-lithium-batteries/` — the skill has no lane to lean on
- Section IA / IB / II, and what changes between them
- Watt-hour and lithium-content thresholds, **each stamped with the edition**
- State-of-charge rule for UN3480
- The lithium battery mark: what it carries, minimum size
- Which UN numbers are forbidden on passenger aircraft

## Priority 2 — sold and unbuilt

The website promises these; nothing implements them.

### `packing-list-review` skill
The reference template already exists in `templates/04-packing-list/`. Straightforward and
overdue.

### Safety Data Sheets
Promised on the site with no skill and no reference. **Decide first: build it or remove it from
the page.** If building, the lane needs the 16 GHS sections, which of them a shipping review
actually uses, and how an SDS is cross-checked against a declaration.

### Chain-of-custody records
Same decision. Currently promised and entirely unsupported.

## Priority 3 — closing the empty folders

| Folder | What it needs |
|---|---|
| `dgr/02-49cfr/` | The US ground legs. Per precedence §1, 49 CFR governs those — and every IAD–ATL practice shipment had them |
| `cold-chain/05-excursions/` | `excursion-assessment` cites no lane reference. MKT, time-out-of-range conventions, what a QP actually asks for |
| `customs/03-hs-codes/` | Not classification — the *process*: where headings come from, what a broker needs, how to phrase a query |
| `compliance/01-regulations/` | The regulation index: what applies to this business and where to find it |
| `compliance/03-training/` | DG training currency. Certification dates, renewal, what expires when |
| `templates/05-sop-templates/`, `06-checklist-templates/` | The blanks the audit lane keeps rebuilding by hand |

## Priority 4 — the operator's own record

Nothing in this list matters more over time than these two.

### Verified values, with editions
One file. Every regulatory figure ever confirmed against a physical DGR, with the edition and
the date checked. Right now **every skill records these as unverified**, every run, forever —
because there has never been a copy to hand. One afternoon with the DGR removes that from every
future report.

### Findings seen in practice
What actually fails, and how often. Every skill's `learnings.md` currently says the check order
is by **consequence, not observed failure rate**, because no dock observations exist. This is
the file that changes that.

## The honest sequence

1. **Class 3 and Class 8** — sold today, thinnest coverage
2. **Verified values with editions** — removes "unverified" from every future report
3. **`packing-list-review`** — promised, easy, template exists
4. **Decide on SDS and chain-of-custody** — build or remove from the page
5. Everything else

## What raises the ceiling most

Not volume. **Two things:**

- **A DGR copy consulted once, with the figures written down and stamped.** Every skill is
  currently written to say "verify or record as unverified" — which is correct, and it means
  every report carries an unverified list. Filling it in is the single largest quality jump
  available.
- **Real findings from real documents.** The system has been tested on one fixture and five
  practice declarations, all written by the same person who built the checks. The first ten real
  client documents will teach it more than any amount of reference writing.
