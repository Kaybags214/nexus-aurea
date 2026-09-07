# Agentic OS — Idea Capture

Status: captured, not yet built. Saved so the idea does not get lost.

## Source

- Video: **"The NEW Agentic OS standard for Claude 5 Models is here (Full Breakdown)"**
- Channel: **RoboNuggets** (Jay E)
- URL: https://www.youtube.com/watch?v=8NSyI-npJCU
- Site / newsletter: https://www.robonuggets.blog
- Community: https://robonuggets.us (Skool)

## PDF status — retrieved

**"ARMS — The Agentic OS Guide (Deep Edition)", a RoboNuggets guide by Jay E, 17 pages.**
Obtained 2026-09-07 via Google Drive after the direct Skool link expired and both
`skool.com` and `files.skool.com` proved blocked by this environment's network policy.

The framework below is now taken from the guide itself, not reconstructed.

## The framework — ARMS

**Not four layers. Four parts, three levels each — a 4 × 3 grid.** Level 1 works today,
level 3 is where the system runs without you.

Build order is bottom-up and **starts with Skills**, in the guide's words *"because they
compound into everything else."*

| # | Part | What it is | L1 | L2 | L3 |
|---|------|-----------|----|----|----|
| 1 | **Skills** | Your SOPs as commands | Pre-built, then your own | Skills with their own file sets (router + sub-files) | Triggered outside chat, headless |
| 2 | **Memory** | Your workspace and context | A folder | Router files, not neat folders | A visual second brain |
| 3 | **Routines** | Scheduled work | Local | Always-on, own machine + Syncthing | Whole agent in the cloud |
| 4 | **Applications** | What the agent can reach | Browse the catalog | Agent searches for connectors | Build your own connectors and micro-apps |

The **command centre is a bonus layer, not part of ARMS.** The guide puts it at 20–30% of
the value: *"The look is a skin; ARMS underneath is the product."*

## Corrections to the first version of this file

The original reconstruction got several things wrong. Recorded here so the error does not
get re-introduced:

- **Order.** Memory was placed at the foundation. Skills comes first.
- **Shape.** Four flat layers; the three-levels-per-part structure was missed entirely.
- **Applications.** Defined as the dashboard for non-technical users. It actually means
  connectors — CLI, API or MCP — plus micro-apps built where none exists.
- **The command centre** was treated as part of the framework. It is the bonus layer.
- **`learnings.md` per skill is ours, not the guide's.** It appears nowhere in the PDF.
  Kept because it earns its place, but it is a Nexus Aurea convention.

## Where Nexus Aurea stands

Level 1 complete across all four parts, with one level 3 partly built.

| Part | L1 | L2 | L3 |
|------|----|----|----|
| Skills | ✅ six skills in `.claude/skills/` | ✅ skill trees — routers 40–43 lines | ⬜ needs the laptop |
| Memory | ✅ eleven lanes + precedence standard | ✅ `CLAUDE.md` + six area indexes | ⬜ visual second brain |
| Routines | ✅ market watch, 4:32 PM ET weekdays | ⬜ | ⬜ |
| Applications | ✅ six connectors live | ⬜ | 🟦 `compliance-auditor` n8n webhook |

## Visuals

Two pages, two different jobs.

**`command-center.html`** — the control surface. Modelled on RUBRIC, the dashboard
shown in the RoboNuggets video: panel columns around a rotating node ring with a
particle memory core. Micro apps, live transit clocks (FRA / SIN / MEM), intake
queue with severity flags, skills deck with a model x effort matrix, and a routine
schedule that marks NEXT against real local time.

Published Artifact: https://claude.ai/code/artifact/f685bfab-eefc-4962-97bb-42940af9fe13

Interface mockup, not a live system. Clocks, week tracker and routine status run on
real time; intake counts, findings and review totals are sample data. Model x effort
picks persist in browser localStorage only.

### The refresh routine

`Refresh Nexus Aurea Command Center` — trigger `trig_0184ine4nbSXR5ZDmJbKCZAg`.
Fires **daily at 11:00 UTC (7:00 AM Eastern)** in a fresh session. It re-reads this repository,
recounts findings, verdicts, skills and memory, rewrites the figures in `command-center.html`,
republishes to the same Artifact URL, and pushes the change.

A run that finds nothing changed makes no edit and does not republish — a no-op is the correct
outcome, not a failure. Notifications are off.

It only touches figures. It is instructed not to change layout, not to alter skills or audit
reports, and not to mark anything live or built that is not.

To pause or change it, use the Routines list in claude.ai, or ask in a session.

---

**`nexus-agentic-os.html`** — the architecture reference. The ARMS stack drawn as
four layers with the repo mapping and a build order. Explains what to build;
`command-center.html` shows what it looks like when built.

Published Artifact: https://claude.ai/code/artifact/50370611-d383-4c04-9451-8a0ee603bce6

## Operating rule (unchanged)

Build the system before chasing the opportunity.
