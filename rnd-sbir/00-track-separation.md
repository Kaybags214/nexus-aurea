# 00 — Track Separation

Why "pharma logistics, housing, robots, and property acquisition" cannot be one proposal, and what
belongs where.

---

## 1. The three tracks

### Track 1 — Human-in-the-loop physical-AI compliance for regulated logistics
**Vehicle: SBIR Phase I. Near-term. This is the proposal.**

> A human-approved, sensor-and-vision system that captures physical shipment evidence, detects
> documentation and handling exceptions, and produces an auditable compliance record.

Assets already in hand:
- A review engine with demonstrated behaviour on live documents — per-field read confidence,
  explicit abstention, cited standards (`../ops-hardening/00-inspection-report.md` §3.1).
- A structured output contract with an enforceable schema
  (`../ops-hardening/schemas/review-envelope.schema.json`).
- A human approval gate with a code-enforced no-op boundary (`../ops-hardening/04-approval-gate/`).
- A written order of precedence for conflicting regulation
  (`../compliance-auditor/standards-of-precedence.md`).
- **Domain credibility.** IATA DGR certification and hands-on pharma air-freight experience. For a
  regulated-logistics proposal this is not decoration — it is the reason a reviewer believes the
  team can define what "correct" means.

### Track 2 — Autonomous multifamily building operations
**Vehicle: a separate future proposal or a commercial pilot. Not this one.**

Design only, simulated events, nothing built:
`../ops-hardening/06-rnd-multifamily-sandbox-concept.md`.

It may reuse Track 1's envelope and approval gate. It must never become a dependency of Track 1, and
it must not appear in the Phase I proposal as scope.

### Track 3 — Six-to-eight-unit property acquisition
**Vehicle: conventional real-estate capital. Not an SBIR activity at all.**

A separate investment decision on its own timeline and its own financing. It is not a milestone of
either R&D track, and no federal R&D award pays for it.

---

## 2. Why one proposal cannot hold all three

**Reviewers score focus.** A Phase I is six to eighteen months of feasibility work on one technical
risk. A proposal spanning logistics compliance, building automation, and real estate does not read
as ambitious — it reads as unfocused, and it invites the reviewer to conclude that the applicant has
not identified which problem they are actually solving.

**The technical risks are unrelated.** Document-and-package reconciliation under regulatory
accountability and building-sensor event triage share an *architecture*, not a *research question*.
Sharing plumbing is not sharing a hypothesis. A proposal that claims otherwise will be pressed on it.

**Property acquisition changes the reading of the whole thing.** A federal R&D proposal that
mentions buying a building invites exactly one question — is this an R&D project or a financing
vehicle? — and the applicant loses regardless of the answer. Track 3 does not appear in the
proposal. Not as scope, not as a milestone, not as motivation.

---

## 3. The firewall

| | Rule |
|---|---|
| **Proposal scope** | Track 1 only. Track 2 may appear as future commercial direction, in one sentence, if it strengthens the market narrative. Track 3 does not appear at all |
| **Technical dependency** | Track 1 depends on nothing in Track 2. Deleting the multifamily sandbox tomorrow must leave Track 1 untouched (`06-rnd-multifamily-sandbox-concept.md` §8) |
| **Systems** | Separate n8n projects, webhook paths, credentials, and audit stores |
| **Accounting** | If an award lands, Track 1 costs are segregated from all other company activity. Do not commingle. This is a condition of the award, not a preference |
| **Personnel time** | PI time charged to the award is Track 1 work. Track 2 and 3 time is not chargeable |

---

## 4. What SBIR money does not buy

Verify each against **NSF 26-510** and the applicable federal cost principles — this section is
directionally right and specifically unverified, since NSF's own site is unreachable from here.

| Cost | Treatment |
|---|---|
| **Real property — land or buildings** | Not allowable. Federal awards do not fund real-property acquisition, and this is a hard rule, not a negotiation |
| **Equipment / capital purchases** | Tightly restricted at NSF Phase I; general-purpose equipment is normally unallowable. Assume no, budget accordingly, and confirm |
| **Construction, renovation** | Not allowable |
| **Existing debt, prior costs, cost of proposal preparation** | Not allowable |
| **Personnel, subawards, materials, consultants, cloud/compute, travel** | Normally allowable within budget rules — this is where the money actually goes |

**The practical consequence:** the prototype in `03-phase1-prototype-spec.md` is deliberately built
from simulated events, stock imagery, and cloud services. That is not only a scoping decision — it
keeps Phase I inside what the funding can actually pay for. A proposal whose plan requires buying
hardware is a proposal with a budget problem.

---

## 5. How the tracks connect over time

```
now ─────────────── 6–18 months ──────────── later ─────────────────────

Track 1  pitch → proposal → Phase I feasibility → Phase II → commercial
                                    │
                                    │ proven: envelope, gate,
                                    │ calibration method, audit record
                                    ▼
Track 2                      separate proposal or pilot, reusing the pattern

Track 3  ······································· conventional financing,
                                                  independent of both
```

The sequencing argument is straightforward and worth stating in the market section of the pitch:
Track 1 produces a validated pattern for human-approved AI decisions under regulatory
accountability. Track 2 is that pattern applied to a second domain. Track 3 is an unrelated
investment that happens to be made by the same person.

**Track 3's independence is a feature, not a concession.** Nothing about the technology roadmap
depends on it, which is precisely why it can proceed or not without disturbing anything else.
