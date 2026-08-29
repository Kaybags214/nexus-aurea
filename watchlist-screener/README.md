# Watchlist Screener

A descriptive screener for a fixed watchlist plus sector-proxy tickers. It
pulls daily OHLCV and computes rolling statistics (volatility, volume
anomalies, gaps, correlation). It does **not** generate trade signals or
place orders. Run it on demand, or optionally on a daily schedule (see
"Daily automation" below) — either way it only ever produces a descriptive
report, never an action.

## Watchlist

`RGTI, INFQ, UONEK, CARV, NVDA, QBTS`

Sector proxies (default): `SMH` (semiconductors, relevant to NVDA), `QTUM`
(Defiance Quantum ETF, relevant to RGTI/QBTS/INFQ).

## Setup

```bash
cd watchlist-screener
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

(A venv isn't strictly required for manual runs, but `run_daily.sh` below
expects one at `.venv/` so cron doesn't need your shell profile.)

## Usage

```bash
python screener.py                              # default watchlist, markdown to stdout
python screener.py --format json                # JSON to stdout
python screener.py --output report.md           # write to a file
python screener.py --tickers NVDA,RGTI --proxies SMH
python screener.py --fetch-timeout 20           # lower the per-ticker network ceiling
python screener.py --z-threshold 2.5 --gap-threshold 5 --corr-window 90
```

## Screens

- **Volatility**: rolling 20-day and 60-day annualized volatility (stdev of
  daily log returns) vs. each ticker's own trailing 1yr average of the 20-day
  series. Flags `elevated` (>30% above average) or `compressed` (>30% below).
- **Volume z-score**: each day's volume vs. the mean/stdev of the *preceding*
  20 days. Flags any of the last 20 trading days where `|z| > 2` (tunable via
  `--z-threshold`).
- **Gap detection**: open vs. prior close, flagged when the move exceeds
  `--gap-threshold` percent (default 3%), over the last 20 trading days.
- **Correlation matrix**: pairwise correlation of daily log returns across the
  full watchlist + sector proxies, over the trailing `--corr-window` days
  (default 60). Symbols without enough overlapping history (e.g. a recent
  listing) are dropped from the matrix rather than shown with a misleading
  partial-window number.

All four are descriptive only — flags mark days/conditions worth a human
look, not buy/sell signals.

Progress ("Fetching NVDA...", row counts, per-ticker errors) prints to stderr as it
runs, so you can see what's happening rather than staring at a blank terminal.

## If it seems to hang

yfinance makes several sequential HTTP calls per ticker (cookie, crumb, chart
data) with no retries but generous per-call timeouts, so a stalled connection
(rate limiting, a flaky network, a corporate proxy) can make a single ticker
take a long time. This screener fetches all tickers in parallel and enforces
a hard `--fetch-timeout` per ticker (default 45s) — a stuck ticker is recorded
as an error and the run continues, and the process force-exits once the
report is built even if a stalled background thread is still alive. If a run
is slow, watch the stderr progress lines to see which ticker is stuck, and
try `--fetch-timeout 15` to fail faster. If every ticker times out, first
sanity-check plain connectivity to Yahoo Finance from your machine/network
(`python -c "import yfinance as yf; print(yf.Ticker('NVDA').history(period='5d'))"`).

## Daily automation

`run_daily.sh` wraps the screener for cron/Task Scheduler:

1. Activates `.venv`, runs the screener, and writes a dated report to
   `reports/YYYY-MM-DD.md` with stderr captured to `reports/YYYY-MM-DD.log`
   (both gitignored — local debug copies).
2. On success, commits that report to `market-watch/screener-reports/YYYY-MM-DD.md`
   on `main` and pushes it.

```bash
chmod +x run_daily.sh
./run_daily.sh                 # sanity-check it manually first
```

Extra arguments pass straight through to `screener.py`, e.g.
`./run_daily.sh --gap-threshold 5`.

### How the auto-commit stays out of your way

The commit happens in a dedicated git worktree at `.report-worktree/`, not
in your working checkout. That means the job **never** switches your branch,
stashes your edits, or touches uncommitted work — you can be mid-change on a
feature branch while the 7am job commits to `main`. The worktree is
bot-managed: it's hard-reset to `origin/main` on every run, so it can't
drift or carry stale state into a commit.

Behavior in the cases that matter:

- **Screener fails** (every watchlist ticker unfetchable) → exits non-zero,
  commits nothing. A proxy alone failing still counts as success.
- **Report unchanged** from one already committed today → no duplicate
  commit, exits 0.
- **Someone else pushed to `main`** in the meantime → fetches and rebases
  onto their work before pushing, with retries. Their commits are never
  overwritten (no force-push anywhere in this script).
- **Push fails** after retries → exits non-zero; the commit still exists in
  `.report-worktree/` so nothing is lost.

All four paths were tested end-to-end against a throwaway local repo.

Add `.report-worktree/` to your global gitignore if you don't want to see it
in `git status` (it's already listed in this repo's `.gitignore`).

### Linux/macOS: cron

Use the absolute path (cron's environment has no shell profile or PATH to
speak of):

```bash
crontab -e
```

Add a line like this (7:00am on weekdays; cron uses the system's local
time, adjust the hour for yours):

```
0 7 * * 1-5 /absolute/path/to/nexus-aurea/watchlist-screener/run_daily.sh
```

Check it's registered with `crontab -l`. The next morning, confirm it ran:
`ls -la reports/` and read the newest `.md`/`.log` pair.

### macOS alternative: launchd

cron works fine on macOS, but if you'd rather use a launchd plist (survives
sleep/wake more reliably), ask and I can add one.

### Windows: Task Scheduler

```powershell
schtasks /create /tn "WatchlistScreener" /tr "C:\path\to\watchlist-screener\run_daily.sh" /sc daily /st 07:00
```

(Requires Git Bash/WSL for the `.sh` wrapper, or ask and I can add a native
`.ps1` equivalent instead.)

### What automation does *not* do here

The cron job commits and pushes the daily report to `main` and nothing else.
It does not email, Slack, or otherwise notify you, and it does not act on
the report's contents in any way. If you want notifications, that's a
separate addition — say so explicitly.

To stop the auto-commit and go back to local-files-only, remove the commit
block at the bottom of `run_daily.sh` (everything below the
`--- Commit + push ---` comment) and delete `.report-worktree/` with
`git worktree remove .report-worktree`.

## Status

All four screens (volatility, volume z-score, gap detection, correlation
matrix) are implemented, tested against synthetic data, and confirmed
against live Yahoo Finance data for the default watchlist.

## Testing

`tests/` covers the screen math and the fetch-timeout watchdog against
synthetic/mocked data (`python -m pytest tests/`, no network required). This
was originally built in a sandboxed session whose network egress is
restricted to an allowlist (PyPI, npm, GitHub, Anthropic) — general internet
hosts, including Yahoo Finance, are blocked there — so the live data pull
could only be exercised by running `python screener.py` in a normal
environment, which has since been done successfully.
