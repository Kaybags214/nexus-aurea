# Documentation and Backup Workflow

## Source of truth
- The `nexus-aurea` GitHub repository is the version-controlled source for Nexus Aurea technical documentation.
- Work locally in `~/nexus-aurea`; commit and push reviewed changes to `main`.
- The initial cloud architecture document is `docs/cloud-architecture.md`, confirmed pushed as commit `b981504` (at the time of the conversation).

## Document boundaries
- Keep architecture content separate from prompts used to generate or revise it.
- If a reusable architecture prompt is needed, store it separately as `docs/cloud-architecture-prompt.md`.
- Create distinct security, backup, disaster recovery, and business continuity policies as they are developed. These are proposed documents, not evidence that policies already exist.

## AI collaboration
- ChatGPT and Claude may assist with drafting, explanation, and independent review.
- Verify AI-generated changes before committing.
- AI chat histories are references, **not reliable backups or the authoritative document store**.

## Backup approach
- The laptop is the working copy; GitHub supplies a remote copy and version history.
- GitHub alone is not a complete backup strategy. Maintain an independent backup of the repository, ideally automated with retention and periodic restore testing.
- Google Drive or another cloud provider may be used as an additional archive, but no such backup is confirmed configured.

## Historical clarification
- `Nexus-Core` was the source location used to copy the initial architecture file, not the final destination repository.
- Early terminal navigation errors and Git setup troubleshooting were resolved and do not need preservation here.
