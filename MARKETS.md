# Markets — index

Public-company research and the screener. Separate from the compliance lanes; shares the
discipline of citing sources and separating research from speculation.

## Start here

| File | What it is |
|---|---|
| `market-watch/README.md` | What this lane is and how it runs |
| `market-watch/daily-update-playbook.md` | The daily procedure |
| `market-watch/ROUTINE-PROMPT.md` | The scheduled routine's prompt — **4:32 PM ET weekdays** |
| `market-watch/n8n-analysis-prompt.md` | Analysis system prompt. The market twin of `AUDIT-ENGINE-PROMPT.md` |
| `market-watch/SETUP-WALKTHROUGH.md` | Setup |

## Tracking

- `market-watch/watchlist.md` — the watchlist
- `market-watch/blockchain-pharma-watchlist.md` — pharma / blockchain names
- `market-watch/filing-tracker.md` — filings
- `market-watch/adoption-tracker.md` — adoption signals
- `market-watch/flow-brief-routine.md` — flow brief procedure

## Output

- `market-watch/flow-briefs/` — dated briefs, most recent `2026-09-02.md`
- `market-watch/screener-reports/` — dated screener output, most recent `2026-08-04.md`
- `market-watch/company-notes/` — per-company notes; currently `RGTI.md` only
- `market-watch/analysis/` — **empty**

## The screener — `watchlist-screener/`

A real Python package, not notes.

- `watchlist-screener/README.md` — setup and the cron / Task Scheduler section
- `watchlist-screener/run_daily.sh` — daily wrapper; commits its report via a dedicated git worktree
- `watchlist-screener/screener.py` and `watchlist-screener/watchlist_screener/` — `cli.py`, `data.py`, `screens.py`
- `watchlist-screener/tests/` — `test_cli.py`, `test_data.py`, `test_screens.py`
