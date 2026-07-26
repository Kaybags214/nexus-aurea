# Watchlist Screener

A descriptive, on-demand screener for a fixed watchlist plus sector-proxy
tickers. It pulls daily OHLCV and computes rolling statistics (volatility,
volume anomalies, gaps, correlation). It does **not** generate trade signals,
place orders, or run as a scheduled job — run it manually whenever you want a
fresh read.

## Watchlist

`RGTI, INFQ, UONEK, CARV, NVDA, QBTS`

Sector proxies (default): `SMH` (semiconductors, relevant to NVDA), `QTUM`
(Defiance Quantum ETF, relevant to RGTI/QBTS/INFQ).

## Setup

```bash
cd watchlist-screener
pip install -r requirements.txt
```

## Usage

```bash
python screener.py                              # default watchlist, markdown to stdout
python screener.py --format json                # JSON to stdout
python screener.py --output report.md           # write to a file
python screener.py --tickers NVDA,RGTI --proxies SMH
python screener.py --fetch-timeout 20           # lower the per-ticker network ceiling
```

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

## Status

Implemented so far: data pull (yfinance) + rolling 20/60-day volatility vs.
each ticker's own trailing 1-year average. Volume z-score, gap detection, and
the rolling correlation matrix are being added next.

## Note on testing in this environment

This was built in a sandboxed session whose network egress is restricted to
an allowlist (PyPI, npm, GitHub, Anthropic) — general internet hosts,
including Yahoo Finance, are blocked by the environment's egress policy. The
screen logic and the CLI/report pipeline were validated end-to-end against
synthetic OHLCV data (see `tests/`), but the actual `yfinance` data pull has
not been exercised against live Yahoo Finance data. Run `python screener.py`
locally to confirm the live pull and inspect real output before relying on
it.
