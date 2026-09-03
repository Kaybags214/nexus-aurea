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

**CRITICAL - validate freshness on every quote.** `GLOBAL_QUOTE` can silently return a stale
cached row. Observed on 2026-08-27: CJMB first returned `latest trading day: 2026-08-24` at
$2.27 / -8.84%, then minutes later returned `2026-08-27` at $2.20 / +4.76% - same endpoint, same
ticker, no error either time. Check the `07. latest trading day` field on EVERY response. If it does
not match today's session date, re-request once; if it still disagrees, print the figure with its
actual as-of date and mark it STALE rather than presenting it as today's close.

**Confirm today's date from the data, not the system clock.** This environment's clock has been
observed running days behind. Take the session date from the `latest trading day` returned by a
liquid ticker (IBM, INTC), and use that date for the report filename and headers.

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

**SEC filings - link construction (do not skip this).** Only ever emit the `browse-edgar` CIK link
form above, using the real CIK from `COMPANY_OVERVIEW`. Never construct a direct
`/Archives/edgar/data/<CIK>/<accession>/<file>` URL unless all three values are real and in hand -
if CIK, accession number, or filename is unknown, drop the filing rather than emit a link containing
the literal string `None`. Confirm every filing you cite carries *this* company's own CIK, not a
same-day filing from an unrelated issuer that surfaced in a generic search. (On 2026-09-02, H's card
cited 93 filings and LIFE's cited 90 in one 48-hour window, every link broken as
`data/None/.../None` - neither company plausibly files that volume in two days; that pattern means
the filing list was never scoped to the company at all. Re-derive it from the CIK, not a keyword
search.)

**News - avoid name collisions.** Search using the company's full legal name and ticker together
(e.g. `"Ethos Technologies" LIFE`, not a bare `LIFE` keyword search), and discard results that are
about a different, similarly-named company. (On 2026-09-02, LIFE's news section returned Swiss Life,
Globe Life, NobleOak Life, and an unrelated baseball headline - none about Ethos Technologies.)

**Crypto - Crypto.com connector** if available: `get_tickers` for price and 24h data,
`get_candlestick` for 7-day change, `get_book` for spread. Instruments are `<TOKEN>_USD`. The
`change` field is a fraction, not a percent (0.0152 means +1.52%). If unavailable, use Alpha Vantage
`DIGITAL_CURRENCY_DAILY` or web research, and say which source was used. Market cap, circulating
supply, unlock schedules, and on-chain activity come from web research either way.

**Private signals:** Sygaldry Technologies and Solidigm - funding, partnerships, hiring, product,
customer validation, IPO signals.

Label every figure with its source and as-of date. Never carry a stale price forward. Keep reported
facts separate from interpretation.

## Step 3.5 - Self-audit before writing (mandatory, do not skip)

Before writing the report file, build two lists and diff them:

1. Every ticker read from the `watchlist.md` Active Watchlist table, plus every token from
   `blockchain-pharma-watchlist.md`. (Shenzhen-listed and private-signal rows are separate sections -
   audit those against their own tables the same way.)
2. Every ticker that will actually get a card in the report you are about to write.

If anything in (1) is missing from (2), you may not silently omit it - either fetch its data now, or
give it a card with a `DATA UNAVAILABLE: <specific reason>` badge, per Step 1's rule. Do not proceed
to Step 4 until the two lists match exactly. State the count explicitly in the section header, e.g.
`Stocks Watchlist (31/31 covered)` - the denominator is always the full watchlist count, never just
however many cards happened to get written.

This has failed silently for three sessions running (2026-08-31, 09-01, 09-02): MU, NVDA, AVGO,
MRVL, COHR, LITE, QBTS, SOXX, SSNLF, SKHY, and DRAM all vanished from the report with no
`DATA UNAVAILABLE` note and no visible count discrepancy - the header just said "18 Assets" as if
that were the whole watchlist. DRAM is the one held position in the account and MU is its named
bellwether in the watchlist notes, so this is the single highest-value check in the whole run.

## Step 4 - Write the report

Write `market-watch/screener-reports/report_YYYY-MM-DD.html` for today's date.

Self-contained HTML, inline CSS only, dark theme (#0f172a background, #f8fafc text), card grid,
priority badges, green #22c55e for gains and red #ef4444 for losses. Footer with the ET timestamp
and: "For research/tracking purposes only. Not financial advice."

**Template stability.** Reuse the same HTML structure, CSS, and class names
(`card`, `ticker`, `price`, `change pos/neg`, `section-title`, etc.) across runs - copy the skeleton
from the most recent `report_*.html` rather than regenerating markup from scratch each session. The
last four sessions (08-29, 08-31, 09-01, 09-02) each used a structurally different template, which
breaks any downstream tooling that parses the report and is a sign the run isn't actually following
"match the most recent report format" from Step 1.

Append new filings and insider activity to `market-watch/filing-tracker.md`.

## Step 5 - Commit and push

Create a branch `market-report-YYYY-MM-DD`, commit as `Add market watch report for YYYY-MM-DD`, and
push with `git push -u origin market-report-YYYY-MM-DD`. Retry up to 4 times with exponential
backoff on network errors.

Do not push directly to `main` - scheduled sessions are branch-scoped and the push will fail.
Do not open a pull request.

Then reply with a short summary: biggest movers, insider transactions worth noting, and anything
that changes a watchlist thesis.
