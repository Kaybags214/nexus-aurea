# Daily Routine Prompt

Paste this as the prompt when recreating the routine in claude.ai > Routines.

**Schedule:** 4:32 PM Eastern, Monday-Friday
**Connectors:** Alpha Vantage, Crypto.com
**Notifications:** push and email

---

Generate today's post-close market watch report for the kaybags214/nexus-aurea repository.

The U.S. equity market closed about 30 minutes ago.

## Step 1 - Read the spec

- `market-watch/daily-update-playbook.md` - the authoritative spec. Follow it.
- `market-watch/watchlist.md` - equities, ETFs, Shenzhen names, private signals
- `market-watch/blockchain-pharma-watchlist.md` - crypto tokens
- `market-watch/screener-reports/` - match the most recent `report_*.html` format

Build the ticker universe by reading those files every run. Never work from a hardcoded list, and
never drop an entry - if data cannot be retrieved, print DATA UNAVAILABLE with the reason.

## Step 2 - Check the market was open

Use Alpha Vantage `MARKET_STATUS`. If closed, write a short report noting the closure, cover crypto
only, and skip to step 5.

## Step 3 - Gather data

**Prices - Alpha Vantage `GLOBAL_QUOTE`, one call per US ticker.** Gives open, high, low, price,
volume, previous close, change, change percent, and trading day. Do NOT use `REALTIME_BULK_QUOTES` -
it is a premium endpoint and returns fabricated sample data (MSFT/AAPL/IBM) on this plan. If you
ever see those three tickers unrequested, discard the response.

**Fundamentals - Alpha Vantage `COMPANY_OVERVIEW`, one call per US ticker.** Gives market cap,
EBITDA, P/E, PEG, book value, EPS, revenue TTM, margins, ROA/ROE, analyst target price and the full
strong-buy/buy/hold/sell/strong-sell breakdown, 52-week range, 50/200-day moving averages, shares
outstanding and float, percent insiders, percent institutions, and the company's SEC CIK number.

**Insider activity - Alpha Vantage `INSIDER_TRANSACTIONS`.** This is Form 4 data: transaction date,
executive name and title, security type, acquisition or disposal (A/D), shares, and share price.
Pass `from_date` to limit to the period since the last report. Responses can be large - use
`return_full_data: true` when the preview truncates. Flag every disposal by an officer or director,
and say plainly when insiders are net sellers.

**ETFs - Alpha Vantage `ETF_PROFILE`** for WQTM and IYW. Net assets, expense ratio, turnover, and
holdings with sector allocation. ETFs file no 10-K, 10-Q, or 8-K - report holdings and concentration
rather than company fundamentals.

**News - Alpha Vantage `NEWS_SENTIMENT`**, plus web search for anything it misses.

**Other useful endpoints:** `EARNINGS` and `EARNINGS_CALENDAR` for upcoming reports,
`EARNINGS_CALL_TRANSCRIPT` for what management actually said, `INSTITUTIONAL_HOLDINGS` for 13F-style
position changes, `DIVIDENDS` and `SPLITS` for corporate actions, `LISTING_STATUS` for delisting
risk (relevant to CJMB), `IPO_CALENDAR` for the Solidigm listing watch, and `TREASURY_YIELD`, `CPI`,
`FEDERAL_FUNDS_RATE` for macro context.

**SEC filings.** Alpha Vantage does not serve 10-K, 10-Q, or 8-K full text, and sec.gov is blocked
by this environment's network policy. So: report insider activity from `INSIDER_TRANSACTIONS`,
financials from `COMPANY_OVERVIEW` and the statement endpoints, and use web search to find filings
that exist. Link them by CIK using
`https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<CIK>&type=&dateb=&owner=include&count=40`
and state clearly that the filing was located but its contents were not read. Never summarize a
filing you have not actually read.

**Crypto - Crypto.com connector** if available: `get_tickers` for price and 24h data,
`get_candlestick` for 7-day change, `get_book` for spread. Instruments are `<TOKEN>_USD`. The
`change` field is a fraction, not a percent (0.0152 means +1.52%). If unavailable, use Alpha Vantage
`DIGITAL_CURRENCY_DAILY` or web research, and say which source was used. Market cap, circulating
supply, unlock schedules, and on-chain activity come from web research either way.

**Private signals:** Sygaldry Technologies and Solidigm - funding, partnerships, hiring, product,
customer validation, IPO signals.

Label every figure with its source and as-of date. Never carry a stale price forward. Keep reported
facts separate from interpretation.

## Step 4 - Write the report

Write `market-watch/screener-reports/report_YYYY-MM-DD.html` for today's date.

Self-contained HTML, inline CSS only, dark theme (#0f172a background, #f8fafc text), card grid,
priority badges, green #22c55e for gains and red #ef4444 for losses. Footer with the ET timestamp
and: "For research/tracking purposes only. Not financial advice."

Append new filings and insider activity to `market-watch/filing-tracker.md`.

## Step 5 - Commit and push

Create a branch `market-report-YYYY-MM-DD`, commit as `Add market watch report for YYYY-MM-DD`, and
push with `git push -u origin market-report-YYYY-MM-DD`. Retry up to 4 times with exponential
backoff on network errors.

Do not push directly to `main` - scheduled sessions are branch-scoped and the push will fail.
Do not open a pull request.

Then reply with a short summary: biggest movers, insider transactions worth noting, and anything
that changes a watchlist thesis.
