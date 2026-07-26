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
