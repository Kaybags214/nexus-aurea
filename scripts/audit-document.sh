#!/usr/bin/env bash
#
# audit-document.sh — run a compliance audit on a document using this repo's skills.
#
#   ./scripts/audit-document.sh <image-or-pdf> ["doc type hint"]
#
# Called by the n8n Execute Command node, or by hand from a terminal.
# Runs Claude Code headlessly so the skills in .claude/skills/ actually load —
# which an API call cannot do, because an API call cannot read this repository.
#
# Writes the report + sidecar into compliance-auditor/audit-reports/ and prints
# the report path on the last line of stdout. Commits and pushes.

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"

DOC="${1:-}"
HINT="${2:-}"

if [ -z "$DOC" ]; then
  echo "usage: $0 <image-or-pdf> [doc type hint]" >&2
  exit 64
fi
if [ ! -f "$DOC" ]; then
  echo "error: no such file: $DOC" >&2
  exit 66
fi
if ! command -v claude >/dev/null 2>&1; then
  echo "error: 'claude' is not on PATH. Install Claude Code, or run this with the full path." >&2
  exit 69
fi

DOC="$(cd "$(dirname "$DOC")" && pwd)/$(basename "$DOC")"   # absolute
STAMP="$(date +%Y-%m-%d_%H%M%S)"
LOG="$REPO/compliance-auditor/intake/runs.log"
mkdir -p "$(dirname "$LOG")" "$REPO/compliance-auditor/audit-reports"

# Permission flag for unattended runs. Headless mode cannot show a prompt, so a
# run that needs approval will hang. Verify the exact flag on your machine with
#   claude --help | grep -i permission
# and override here if it differs:
#   export CLAUDE_AUDIT_FLAGS="--permission-mode acceptEdits"
FLAGS="${CLAUDE_AUDIT_FLAGS:---permission-mode acceptEdits}"
MODEL="${CLAUDE_AUDIT_MODEL:-claude-opus-5}"

PROMPT="Audit the compliance document at ${DOC}.
${HINT:+Document type hint from the submitter: ${HINT}}

Follow CLAUDE.md, compliance-auditor/skill-contract.md and
compliance-auditor/standards-of-precedence.md.

1. Identify the document type.
2. Choose the matching skill in .claude/skills/ and run it IN FULL — read its
   SKILL.md router, then each file in its checks/ folder, in order. Do not
   shortcut by working from the router alone.
3. If more than one document is submitted for the same shipment, run the
   cross-document check and report repeating defects as one pattern finding.
4. Write the report to
   compliance-auditor/audit-reports/audit_${STAMP}_<doctype>.md
   in the shape of compliance-auditor/audit-report-template.md.
5. Write the sidecar JSON beside it, same basename with .json, per
   skill-contract.md — including the unverified array.
6. Redact any telephone number or personal contact detail in the report.
7. Write ONLY those two files. Do not edit CLAUDE.md, any area index, any skill, or any
   other file in the repository. The router rule in CLAUDE.md does not apply here: a report
   landing in an existing folder changes no structure. This run stages only
   compliance-auditor/audit-reports/, so an edit anywhere else is left dangling and uncommitted.

Rules: never state a regulatory limit from memory — verify or record it as
unverified. Unreadable is 'cannot verify from image', never a guess. Never issue
PASS with an open Critical.

Print ONLY the path of the report file you wrote as the final line of output."

echo "[$STAMP] START  doc=$DOC hint=${HINT:-none}" >> "$LOG"

set +e
OUT="$(claude -p "$PROMPT" --model "$MODEL" $FLAGS 2>&1)"
RC=$?
set -e

if [ $RC -ne 0 ]; then
  echo "[$STAMP] FAIL   rc=$RC" >> "$LOG"
  echo "$OUT" >&2
  exit $RC
fi

REPORT="$(printf '%s\n' "$OUT" | tr -d '\r' | grep -E 'audit-reports/.*\.md' | tail -1 || true)"

if [ -z "$REPORT" ] || [ ! -f "$REPORT" ]; then
  echo "[$STAMP] FAIL   no report file produced" >> "$LOG"
  echo "$OUT" >&2
  echo "error: the run finished but no report file was found." >&2
  exit 70
fi

git add compliance-auditor/audit-reports/ >/dev/null
if git diff --cached --quiet; then
  echo "[$STAMP] NOOP   nothing to commit" >> "$LOG"
else
  git -c user.name="Nexus Aurea Auditor" -c user.email="noreply@anthropic.com" \
      commit -q -m "audit: $(basename "$REPORT")"
  git push -q origin HEAD 2>>"$LOG" || echo "[$STAMP] WARN   push failed" >> "$LOG"
fi

echo "[$STAMP] OK     $REPORT" >> "$LOG"
printf '%s\n' "$REPORT"
