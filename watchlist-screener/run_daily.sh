#!/usr/bin/env bash
# Daily wrapper for cron/Task Scheduler:
#   1. Activates the venv and runs the screener, writing a local dated
#      report + log under reports/ (gitignored - debug copy only).
#   2. On success, commits that same report into market-watch/screener-reports/
#      on `main` and pushes it - via a dedicated git worktree, never by
#      switching branches in this checkout, so it can't collide with
#      whatever branch/uncommitted work you're using this clone for.
#
# Meant to be invoked with an absolute path (see README's cron/Task
# Scheduler section): cron runs with a minimal environment, no shell
# profile, no activated venv, often no useful PATH.
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
SCREENER_STATUS=$?

if [ $SCREENER_STATUS -ne 0 ]; then
    echo "watchlist screener failed (exit $SCREENER_STATUS) - see $LOG_FILE - skipping commit" >&2
    exit $SCREENER_STATUS
fi

# --- Commit + push the report to main, via a dedicated worktree ---------
REPO_ROOT="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel)"
WORKTREE_DIR="$REPO_ROOT/.report-worktree"
REPORT_SUBDIR="market-watch/screener-reports"
COMMIT_MSG="Add watchlist screener report for ${DATE_STAMP}"

git -C "$REPO_ROOT" fetch origin main 2>>"$LOG_FILE"
if [ $? -ne 0 ]; then
    echo "error: git fetch origin main failed - see $LOG_FILE - report saved locally at $REPORT_FILE but not committed" >&2
    exit 2
fi

if [ ! -d "$WORKTREE_DIR" ]; then
    if git -C "$REPO_ROOT" show-ref --verify --quiet refs/heads/main; then
        git -C "$REPO_ROOT" worktree add "$WORKTREE_DIR" main >>"$LOG_FILE" 2>&1
    else
        git -C "$REPO_ROOT" worktree add -b main "$WORKTREE_DIR" origin/main >>"$LOG_FILE" 2>&1
    fi
    if [ $? -ne 0 ]; then
        echo "error: failed to set up $WORKTREE_DIR - see $LOG_FILE - report saved locally at $REPORT_FILE but not committed" >&2
        exit 2
    fi
fi

# This worktree is bot-managed only; hard-reset to origin/main every run so
# it can never drift or carry a half-finished merge into a commit.
git -C "$WORKTREE_DIR" checkout main >>"$LOG_FILE" 2>&1
git -C "$WORKTREE_DIR" reset --hard origin/main >>"$LOG_FILE" 2>&1
if [ $? -ne 0 ]; then
    echo "error: failed to sync $WORKTREE_DIR to origin/main - see $LOG_FILE - report saved locally at $REPORT_FILE but not committed" >&2
    exit 2
fi

mkdir -p "$WORKTREE_DIR/$REPORT_SUBDIR"
cp "$REPORT_FILE" "$WORKTREE_DIR/$REPORT_SUBDIR/${DATE_STAMP}.md"

git -C "$WORKTREE_DIR" add "$REPORT_SUBDIR/${DATE_STAMP}.md"
if git -C "$WORKTREE_DIR" diff --cached --quiet; then
    echo "no change vs. already-committed report for $DATE_STAMP - nothing to push" >>"$LOG_FILE"
    exit 0
fi

git -C "$WORKTREE_DIR" commit -m "$COMMIT_MSG" >>"$LOG_FILE" 2>&1
if [ $? -ne 0 ]; then
    echo "error: git commit failed - see $LOG_FILE - report saved locally at $REPORT_FILE but not committed" >&2
    exit 2
fi

PUSH_OK=1
for delay in 0 2 4 8 16; do
    [ "$delay" -ne 0 ] && sleep "$delay"
    if git -C "$WORKTREE_DIR" push origin main >>"$LOG_FILE" 2>&1; then
        PUSH_OK=0
        break
    fi
    git -C "$WORKTREE_DIR" fetch origin main >>"$LOG_FILE" 2>&1
    git -C "$WORKTREE_DIR" rebase origin/main >>"$LOG_FILE" 2>&1 || break
done

if [ $PUSH_OK -ne 0 ]; then
    echo "error: git push to origin main failed after retries - see $LOG_FILE - commit exists locally in $WORKTREE_DIR" >&2
    exit 2
fi

echo "committed and pushed $REPORT_SUBDIR/${DATE_STAMP}.md to main" >>"$LOG_FILE"
exit 0
