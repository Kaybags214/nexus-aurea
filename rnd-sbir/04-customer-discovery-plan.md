# 04 — Customer Discovery Plan

**Target: 8–12 interviews in the next 30–60 days.** NSF weighs commercial evidence heavily, and
interviews are the cheapest, fastest way to produce it.

**Two jobs at once.** These conversations are also where corpus partners come from (`01` §6). Every
interview is a chance to ask about historical documents — do not run them separately.

---

## 1. Who

| Segment | Role to reach | Why | Target |
|---|---|---|---|
| **Freight forwarders / consolidators** | DG compliance manager, station manager | Accountable at tender. Highest exposure | 4–5 |
| **Cargo handling agents** | Acceptance supervisor, DG acceptance staff | Where errors are caught today, under time pressure | 2–3 |
| **Pharma shippers / 3PLs** | QA or logistics compliance lead | Cold chain adds GDP/GMP documentation on top | 2–3 |
| **DG trainers / consultants** | Instructor, independent auditor | See error patterns across many companies. Often the easiest first interviews | 1–2 |

**Reach the person who signs, not the person who buys.** The DG-certified individual whose name goes
on the declaration knows what actually goes wrong. Procurement does not, and will describe a system
nobody uses.

Sourcing: existing industry contacts; IATA DGR training cohorts and instructors; local forwarders
and handling agents at nearby airports; professional associations; LinkedIn, with a specific,
non-salesy approach.

## 2. Ground rules

- **This is not a sales call, and it should not sound like one.** Do not describe the system before
  they describe their process. Once you have pitched, everything after is politeness, not data.
- **Ask about the last time, not the general case.** "Walk me through the last declaration you sent
  back" beats "what problems do you have." Specific memories are reliable; generalisations are
  self-flattering.
- **Ask what they do, not what they would buy.** Stated purchase intent is close to worthless.
  Current behaviour and current spend are not.
- **Write it down within the hour.** Verbatim quotes where possible — quotes are what make a
  market section credible.
- **No confidential documents.** If someone offers a real declaration, stop and route it through the
  consent and redaction path (`../ops-hardening/07-client-document-custody.md` §5).

## 3. Interview guide (~30 minutes)

**Their process — 10 min**
1. Walk me through what happens when a DG shipment's paperwork arrives for acceptance.
2. Who physically checks it against the package? What do they compare?
3. How long does one check take? How many a day?
4. What happens when the paperwork and the package disagree?

**Errors — 10 min**
5. Tell me about the last declaration you rejected or sent back. What was wrong with it?
6. Which errors do you see repeatedly?
7. Has an error ever got through? What happened downstream? *(May not get a straight answer. Ask
   anyway — the hesitation is itself informative.)*
8. What does one rejected or held shipment cost you — direct cost, and the rest?

**Current tooling — 5 min**
9. What software touches this today? Does anything check the document, or just move it?
10. Has anything automated been tried here? What happened?

**The uncertainty question — 5 min** *(the one that tests the core thesis)*
11. If a system told you "I read this field but I am not confident," would that be useful, or just
    noise?
12. How many false alarms a day before your team stops reading the alerts?
13. What would a system have to show you for you to trust that it had actually checked something?

**Then, and only then**
14. Describe the concept in two sentences. Ask what is wrong with it.
15. Would you be willing to share historical, redacted declarations to help build a test set?
16. Who else should I talk to?

Questions 12 and 13 are the highest-value in the guide. **12 measures R5 directly** — the alert
volume at which the human gate stops being a control. **13 tells you what the evidence record must
contain** to be believed, which is the entire product.

## 4. What counts as evidence

For the pitch and the eventual proposal:

| Strong | Weak |
|---|---|
| "We reject about one in eight declarations; each costs roughly X in re-work and delay" | "Compliance is a big pain point" |
| "Three alerts a day is fine. Ten and we stop looking." | "We would definitely be interested" |
| "I would need to see the actual box on the form it flagged" | "Sounds useful" |
| A named contact willing to provide redacted documents | A LinkedIn like |

Quantified frequency, quantified cost, and stated tolerance thresholds. Everything else is warmth.

## 5. Recording

One file per interview in `rnd-sbir/interviews/`, redacted:

```
Date · Segment · Role (not name) · Company type (not name)
Their process, in their words
Errors described — with frequency and cost where given
Current tooling
Responses to Q11–13, verbatim where possible
Corpus willingness: yes / no / maybe — follow-up
Referrals
What surprised me
```

**"What surprised me" is the most valuable line in the template.** It is where an assumption breaks,
and a broken assumption found now is worth more than a confirmed one.

Keep company and individual names out of the committed record — segment and role are enough for the
pitch, and `../ops-hardening/07-client-document-custody.md` applies to interview notes as much as to
shipping documents.

## 6. Synthesis

After 8–12 interviews, produce a two-page memo:

- Error frequency and cost, ranged across interviews.
- Alert-tolerance threshold, ranged — the R5 design constraint, from the field.
- What must be shown for a finding to be believed — the evidence-record requirement.
- Which assumptions in `02-nsf-project-pitch-draft.md` §3 survived, and which did not.
- Corpus partners identified.

**Then revise the pitch's Market Opportunity section against it.** The draft in `02` §3 is a set of
hypotheses written before anyone was asked. Some of them are wrong. Finding out which, before
submitting, is the entire point of doing this now rather than after.
