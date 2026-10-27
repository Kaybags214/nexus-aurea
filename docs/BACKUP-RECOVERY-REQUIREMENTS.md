# Nexus Aurea — Backup and Recovery Requirements
Status: Requirements only; scripts NOT production validated
Captured: 2026-10-27

## Environment and discovery
- Chromebook Linux was the working environment in this discussion.
- Previously assumed local paths: `~/nexus-aurea` and `~/nexus-backups`. Confirm that they actually exist before any write.
- ChromeOS removable storage may be under `/mnt/chromeos/removable/<device>/`; mount/sharing can change. Never assume the removable root is a verified external drive. Require an explicitly selected, writable, mounted destination.
- Archived July 2026 filenames looked like `nexus-aurea-backup-20260705-172301.tar.gz`; this is historical evidence, **not verification that backups still exist**.

## Backup interface
- Desired modes: `github`, `drive`, `both`, plus read-only `status`.
- GitHub: verify repository, branch, remote, authentication; do not auto-stage sensitive files or unverified regulated content. A Git push is version control, not a full independent disaster-recovery backup.
- Local/external: backup complete intended project scope, including history if required; use dated archives, SHA-256 manifest, archive integrity test, post-copy checksum verification, logs, explicit failure status.
- Fail visibly if the required external destination is missing, rather than reporting a successful dual backup with only a local file.
- Keep at least one independently recoverable copy away from the active working directory. Define retention, access control and encryption for any sensitive data.

## Restore safety (mandatory)
1. Default to `help`, `list` and `verify` read-only commands. Restoration must be deliberate.
2. Authenticate/validate selected source. Check checksum, archive readability, archive paths (no traversal, absolute paths, links escaping target), and expected project structure.
3. Extract into a *new temporary directory* on the same filesystem. Never first `rm -rf` the live project.
4. Create and verify a complete independent safety copy, with available disk space checked.
5. Show source, target, differences, and exact files/operations; require explicit confirmation.
6. Swap/recover only after successful validation; preserve previous tree for rollback.
7. Verify Git state, file inventory, and sample content after restore; document a recovery drill in a disposable directory.
- The July 2026 restore drafts used risky delete-before-extract approaches and partial `.md` copies. Do not use those scripts in production without redesign and testing.
- Never run `git reset --hard`, force push, or destructive checkout as a casual restore test.

## Status
These are design requirements saved from the conversation, not proof that Chromebook paths, scripts, backups, or Git sync currently work.
