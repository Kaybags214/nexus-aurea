#!/usr/bin/env bash
#
# audit-document.sh — run a compliance audit on a document using this repo's skills.
#
#   ./scripts/audit-document.sh <image-or-pdf> ["doc type hint"]          practice
#   ./scripts/audit-document.sh --client <image-or-pdf> ["doc type hint"]  real client
#
# PRACTICE mode writes the report into the repo and commits it. Use only for invented
# parties — Apex Inc., ABC Flyers, fixtures.
#
# CLIENT mode writes to $NA_CLIENT_DIR (default ~/nexus-aurea-client), commits nothing,
# and touches git not at all. Use for every real client document.
# See compliance/02-sops/data-handling.md — the report is as sensitive as the document.
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

CLIENT_MODE=0
if [ "${1:-}" = "--client" ]; then
  CLIENT_MODE=1
  shift
fi

DOC="${1:-}"
HINT="${2:-}"

if [ -z "$DOC" ]; then
  echo "usage: $0 [--client] <image-or-pdf> [doc type hint]" >&2
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
mkdir -p "$(dirname "$LOG")"

# Resolve a path to its canonical form — symlinks and .. segments removed. The
# containment check below is the confidentiality boundary, so it must compare where
# a path actually lands, not how it was spelled.
canon() {
  if command -v realpath >/dev/null 2>&1; then
    realpath "$1"
  else
    ( cd "$1" >/dev/null 2>&1 && pwd -P )
  fi
}

if [ "$CLIENT_MODE" = "1" ]; then
  OUTDIR="${NA_CLIENT_DIR:-$HOME/nexus-aurea-client}/reports"
  if ! mkdir -p "$OUTDIR" 2>/dev/null; then
    echo "error: cannot create the client output directory ($OUTDIR)." >&2
    echo "       Check NA_CLIENT_DIR — a dangling symlink or an unwritable parent" >&2
    echo "       will do this. Refusing to continue." >&2
    exit 78
  fi

  # Canonicalise BOTH sides before comparing. "/tmp/../repo/x" and a symlink pointing
  # into the repository both spell as outside while landing inside.
  OUTDIR_REAL="$(canon "$OUTDIR")"
  REPO_REAL="$(canon "$REPO")"
  if [ -z "$OUTDIR_REAL" ] || [ -z "$REPO_REAL" ]; then
    echo "error: could not resolve the client output directory ($OUTDIR)." >&2
    echo "       Refusing to write a client report to an unresolved path." >&2
    exit 78
  fi
  case "$OUTDIR_REAL" in
    "$REPO_REAL"|"$REPO_REAL"/*)
      echo "error: client output directory resolves inside the repository." >&2
      echo "         given: $OUTDIR" >&2
      echo "       resolves: $OUTDIR_REAL" >&2
      echo "       Client reports must never enter git. Set NA_CLIENT_DIR elsewhere." >&2
      exit 78 ;;
  esac
  OUTDIR="$OUTDIR_REAL"
  chmod 700 "$OUTDIR" 2>/dev/null || true
else
  OUTDIR="$REPO/compliance-auditor/audit-reports"
  mkdir -p "$OUTDIR"
fi

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
   ${OUTDIR}/audit_${STAMP}_<doctype>.md
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

if [ "$CLIENT_MODE" = "1" ]; then
  echo "[$STAMP] START  mode=CLIENT out=$OUTDIR" >> "$LOG"
else
  echo "[$STAMP] START  mode=practice doc=$DOC hint=${HINT:-none}" >> "$LOG"
fi

set +e
OUT="$(claude -p "$PROMPT" --model "$MODEL" $FLAGS 2>&1)"
RC=$?
set -e

if [ $RC -ne 0 ]; then
  echo "[$STAMP] FAIL   rc=$RC" >> "$LOG"
  echo "$OUT" >&2
  exit $RC
fi

REPORT="$(printf '%s\n' "$OUT" | tr -d '\r' | grep -oE '[^[:space:]]*audit_[0-9_-]+_[^[:space:]]*\.md' | tail -1 || true)"
[ -n "$REPORT" ] && [ ! -f "$REPORT" ] && [ -f "$OUTDIR/$(basename "$REPORT")" ] && REPORT="$OUTDIR/$(basename "$REPORT")"

if [ -z "$REPORT" ] || [ ! -f "$REPORT" ]; then
  echo "[$STAMP] FAIL   no report file produced" >> "$LOG"
  echo "$OUT" >&2
  echo "error: the run finished but no report file was found." >&2
  exit 70
fi

# The sidecar is the audit trail — how a finding gets defended months later.
# skill-contract.md makes it mandatory, and makes its "unverified" array mandatory.
# A report without one is an incomplete run, not a successful one.
SIDECAR="${REPORT%.md}.json"
if [ ! -f "$SIDECAR" ]; then
  echo "[$STAMP] FAIL   report written but no sidecar: $SIDECAR" >> "$LOG"
  echo "error: the run wrote $REPORT but no sidecar JSON beside it." >&2
  echo "       skill-contract.md requires one. Treating the run as incomplete." >&2
  exit 71
fi
if command -v python3 >/dev/null 2>&1; then
  if ! python3 - "$SIDECAR" <<'PYEOF'
import json, sys
with open(sys.argv[1]) as fh:
    doc = json.load(fh)
if "unverified" not in doc:
    sys.exit("sidecar has no 'unverified' array")
PYEOF
  then
    echo "[$STAMP] FAIL   sidecar invalid: $SIDECAR" >> "$LOG"
    echo "error: $SIDECAR is not valid JSON, or is missing the required" >&2
    echo "       'unverified' array. Treating the run as incomplete." >&2
    exit 71
  fi
fi

if [ "$CLIENT_MODE" = "1" ]; then
  # Deliberately no git. The report names the client's shipper, consignee, commodity and
  # value; committing it is the same disclosure as committing the document itself.
  chmod 600 "$REPORT" "$SIDECAR" 2>/dev/null || true
  echo "[$STAMP] OK     mode=CLIENT (not committed)" >> "$LOG"
else
  git add compliance-auditor/audit-reports/ >/dev/null
  if git diff --cached --quiet; then
    echo "[$STAMP] NOOP   nothing to commit" >> "$LOG"
  else
    git -c user.name="Nexus Aurea Auditor" -c user.email="noreply@anthropic.com" \
        commit -q -m "audit: $(basename "$REPORT")"
    git push -q origin HEAD 2>>"$LOG" || echo "[$STAMP] WARN   push failed" >> "$LOG"
  fi
  echo "[$STAMP] OK     $REPORT" >> "$LOG"
fi
printf '%s\n' "$REPORT"
