# Nexus Aurea — R&D / SBIR Preparation

**Opened:** 2026-09-06 · **Status:** preparation. No pitch submitted, no proposal drafted for submission.

One sharp technical problem, not four. The SBIR-ready framing:

> **A human-approved, sensor-and-vision system that captures physical shipment evidence, detects
> documentation and handling exceptions, and produces an auditable compliance record.**

## The three tracks, kept apart

| Track | Vehicle | Status |
|---|---|---|
| **1. Human-in-the-loop physical-AI compliance for regulated logistics** | SBIR Phase I | **Near-term. This is the proposal.** |
| **2. Autonomous multifamily building operations** | Separate future proposal or commercial pilot | Design only — `../ops-hardening/06-rnd-multifamily-sandbox-concept.md` |
| **3. Six-to-eight-unit property acquisition** | Conventional real-estate capital | **Not an SBIR activity.** Later, once track 1 has traction |

Track separation is the point. `00-track-separation.md` has the reasoning and the firewall.

## Read in this order

| File | |
|---|---|
| `00-track-separation.md` | The three tracks, why they cannot share a proposal, and what SBIR money may not buy |
| `01-technical-risk-register.md` | **Read this first if you read only one.** What is genuinely research here versus integration, and what would prove or disprove each risk |
| `02-nsf-project-pitch-draft.md` | Draft against the four prompts, within the character limits |
| `03-phase1-prototype-spec.md` | The simulated physical-AI prototype — 30–60 day scope |
| `04-customer-discovery-plan.md` | Who to interview, what to ask, what counts as evidence |
| `05-eligibility-and-registrations.md` | Eligibility, and the registration lead time that quietly controls the schedule |

---

## Two corrections to the working timeline

Both matter for scheduling and neither is a small adjustment.

**1. Project Pitch feedback is fast; the full-proposal deadlines are fixed.** The working plan assumed
a pitch "anytime" with a decision roughly six months after a full proposal. The pitch part appears
right — submissions are continuous under the current solicitation (**NSF 26-510**), reopened
2026-06-02. But full proposals go in on **fixed dates**, reported as **2026-11-04**, then
**2027-03-04**, then a recurring pattern of the first Wednesday in July, first Wednesday in November,
and first Thursday in March.

Today is 2026-09-06. That gives two realistic targets:

| Target | Requires | Assessment |
|---|---|---|
| **2026-11-04** | Pitch submitted within days; invitation returned in ~4 weeks; full proposal written in ~4 weeks | Aggressive. Only viable if the technical risk framing in `01` is already sharp |
| **2027-03-04** | Pitch by roughly December; proposal over January–February | **Realistic.** Leaves room for the prototype and the customer interviews to actually inform the proposal |

**Recommendation: target 2027-03-04 and treat 2026-11-04 as upside.** A proposal written before the
prototype exists and before anyone has been interviewed will read like one.

**2. Project Pitches are rationed.** Reported caps are **two per company per 12 months**, and **no
more than three for the same project or technology** regardless of topic or timing. This is the
constraint that should govern behaviour between now and submission: **a weak pitch is not a free
attempt at feedback — it spends half your annual allocation.** Get `01` right first.

## Sourcing caveat — read before relying on any figure above

`seedfund.nsf.gov` and `www.nsf.gov` are both blocked by this environment's network egress proxy, so
**every NSF figure in this folder comes from secondary sources, not from NSF directly.** They are
consistent across several sources but are not authoritative.

**Verify all of it against solicitation NSF 26-510 itself before acting**, in particular: the
Phase I ceiling and duration (reported ~$305,000, 6–18 months), the pitch caps, the deadline dates,
and the cost rules in `00` §4. Where this folder states a number, treat it as a prompt to check, not
as a finding.

## The next 30–60 days

1. Sharpen the technical risk framing — `01`. Everything else depends on it.
2. Build the simulated prototype — `03`.
3. Interview 8–12 potential users — `04`.
4. Start registrations — `05`. **Begin this in week one**; it has the longest lead time and no
   amount of good writing shortens it.
5. Finish the workflow hardening — `../ops-hardening/`. It is the credibility evidence underneath
   the whole pitch.
