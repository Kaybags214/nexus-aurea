#!/usr/bin/env bash
# Daily wrapper for cron/Task Scheduler: activates the venv, runs the
# screener, and writes a dated report + log under reports/. Meant to be
# invoked with an absolute path, since cron runs with a minimal environment
# (no shell profile, no activated venv, often no useful PATH).
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [ ! -f ".venv/bin/activate" ]; then
    echo "error: .venv not found in $SCRIPT_DIR - run the Setup steps in README.md first" >&2
    exit 1
fi
# shellcheck disable=SC1091
source .venv/bin/activate

mkdir -p reports
DATE_STAMP="$(date +%F)"
REPORT_FILE="reports/${DATE_STAMP}.md"
LOG_FILE="reports/${DATE_STAMP}.log"

python screener.py --output "$REPORT_FILE" "$@" 2>"$LOG_FILE"
STATUS=$?

if [ $STATUS -ne 0 ]; then
    echo "watchlist screener failed (exit $STATUS) - see $LOG_FILE" >&2
fi
exit $STATUS
