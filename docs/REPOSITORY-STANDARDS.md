# Nexus Aurea — Repository and Evidence Standards
Status: Internal operating standard (documentation workflow only)
Captured: 2026-10-27

## Source and release control
- Treat Claude, ChatGPT and other AI-generated research/code as **unverified intake**, not binding regulation or tested software.
- Classify material as RAW, REVIEWED, VERIFIED REFERENCE, or APPROVED OPERATIONAL. Do not imply approval from the filename alone.
- Preserve the original raw source where useful. Maintain corrected versions separately with dated source links, applicable edition, reviewer, and change history.
- For IATA DGR / ICAO / 49 CFR / GDP / CBP / HTSUS, cite the actual governing edition, section, conditions, and operator/customer variations. Check primary sources; do not promote a vendor marketing claim to a regulatory rule.
- Dangerous goods shipment acceptance, customs filing, and pharmaceutical excursion release/disposition require an authorized human decision. AI checklists are screening aids only.
- Reject invented shortcuts, blanket approval rules, assumed exam frequencies, speculative pass probabilities, and absolute temperature-based product rejection thresholds.

## Repository organization
- Keep existing live folders rather than recreating a second repository or blindly renaming paths.
- Proposed areas: `compliance/`, `dgr/`, `cold-chain/`, `customs/`, `scripts/`, `docs/`; use `research-drafts/` only when needed.
- CBLE work can use `customs/cble/{cfr-19,exams,study-guides,reference-materials,error-logs}/` when those folders are intentionally added.
- Earlier scripts assumed a local `~/nexus-aurea` checkout, while older drafts assumed `~/nexus-core`. Verify actual working directories and Git remotes before running commands.
- Both `Kaybags214/nexus-aurea` and `Kaybags214/nexus-aurea-core` exist. Do not infer that one supersedes the other; verify intended scope.
- Never commit secrets, credentials, private shipment records, personal data, or customer files to a public repository.

## Changes and review
1. Inspect source, intended destination, and existing files.
2. Identify duplicates, unsupported citations, dangerous instructions, and needed updates.
3. For scripts, run shell syntax checks and safe/read-only tests before any production action.
4. Inspect `git status` and `git diff --cached` before committing.
5. Commit specifically reviewed files, not indiscriminate `git add .` for compliance research.
6. Confirm remote/branch and verify any successful push.
7. No unattended publishing of raw compliance output.

## Superseded historical draft warnings
July 2026 materials repeatedly mislocated post-summary corrections under Part 145, described Part 152 as seizures/penalties, mislabeled Part 159, and gave unsupported CBLE weights/pass forecasts. Lithium battery, UN3373, cold-chain excursion and approval statements also needed correction. They are **not approved field guidance**.
