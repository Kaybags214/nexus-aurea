# Daily Market Watch Update Playbook

Purpose: Define exactly what the automated weekday market-watch update produces, so every run is
consistent, reproducible, and complete.

**Schedule:** Monday through Friday, 4:30 PM Eastern (30 minutes after the U.S. equity close).
**Output:** `market-watch/screener-reports/report_YYYY-MM-DD.html`
**Companion updates:** `market-watch/filing-tracker.md` (append any new filings found)

This folder is for research and education. It is not a trading journal and not financial advice.

---

## 1. Coverage

Every run must cover **every** entry in these files. Do not silently drop a name — if data cannot be
retrieved, print the entry with an explicit `DATA UNAVAILABLE` note and the reason.

| Source file | What it contains |
|---|---|
| `market-watch/watchlist.md` | U.S. equities, ETFs, Shenzhen-listed optical names, private-company signals |
| `market-watch/blockchain-pharma-watchlist.md` | Crypto tokens / networks |

Re-read both files at the start of every run. The watchlist changes over time; never work from a
hardcoded ticker list.

---

## 2. Report sections (in order)

### 2.1 Header + market bar

- Report date and generation timestamp in ET.
- Index bar: S&P 500, Nasdaq Composite, Dow Jones, VIX — closing level and percent change.
- One-line market tone summary (what drove the session).

### 2.2 Equity watchlist

One card per ticker. Include as much of the following as is retrievable:

**Price and session data**
- Last / closing price, absolute and percent change
- Day range, volume vs. average volume
- 52-week high / low and distance from each
- Market capitalization

**Fundamentals**
- P/E (trailing and forward), P/S, EV/EBITDA where meaningful
- Revenue (latest quarter and TTM), revenue growth YoY
- Net income / EPS, gross and operating margin
- Cash, total debt, free cash flow, and cash runway for pre-revenue names
- Shares outstanding and change vs. prior period (dilution watch)
- Dividend and yield where applicable

**Analyst and positioning**
- Consensus rating, price target, recent upgrades/downgrades
- Short interest and days-to-cover where available
- Institutional / insider ownership percentage

**News**
- Material headlines from the last 24 hours (or since the prior trading day) with source links
- Skip aggregator noise; prefer primary sources and major financial press

**Thesis check**
- One or two lines: does anything today change the reason this name is on the watchlist?

### 2.3 SEC filings — required every run

For each U.S.-listed watchlist company, check for filings made since the previous report and
report **what the filing actually says**, not just that it exists.

| Form | What to extract |
|---|---|
| **10-K** (annual) | Business model, revenue and margin trend, risk-factor changes vs. prior year, debt and liquidity, MD&A takeaways, ownership structure, going-concern language |
| **10-Q** (quarterly) | Revenue trend, net income/loss, cash position, debt, share count and dilution, segment performance, risk-factor changes |
| **8-K** (material event) | What happened, whether it is material, and whether it touches management, debt, acquisitions, financing, resignations, litigation, delisting risk, or capital structure |
| **DEF 14A** (proxy) | Board structure, executive compensation, shareholder proposals, insider ownership, voting control |
| **Form 4** (insider) | Insider buying vs. selling, option grants, size relative to holdings, pattern over time |
| **Form 144** | Proposed insider sales |
| **S-1 / S-3 / 424B** | Registration and shelf capacity, offering size and pricing, use of proceeds, dilution impact |
| **SC 13D / 13G / 13F** | Activist or large-holder position changes |

Primary source: SEC EDGAR full-text and company filing indexes
(`https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&ticker=<TICKER>&type=&dateb=&owner=include&count=40`).
Link every filing directly to its EDGAR document URL.

For non-U.S. names (Samsung, Novo Nordisk ADR context, Shenzhen-listed optical companies), use the
equivalent local disclosure — exchange filings, annual and interim reports, 20-F where applicable —
and label the source clearly.

**ETFs file differently.** WQTM and IYW are registered investment companies, not operating
companies - they file no 10-K, 10-Q, or 8-K. For these, check N-PORT and N-CSR for holdings and
index changes and 485BPOS for prospectus changes, and report holdings, concentration, and expense
ratio rather than company fundamentals.

Append every newly discovered filing as a row in `market-watch/filing-tracker.md`.

### 2.4 Crypto / blockchain watchlist

One card per token in `blockchain-pharma-watchlist.md`:

- Price, 24h change, 7-day change
- Market capitalization and 24h volume
- Circulating vs. total/max supply; note upcoming unlocks
- Network activity where retrievable (transactions, active addresses, TVL, staking)
- Protocol, partnership, or regulatory news from the last 24 hours
- Adoption check: any movement on real pharma / supply-chain / logistics use cases

Keep the study framing from the crypto watchlist file — real adoption over price action.

**Data sources.** Use the Crypto.com connector for market data - it is an exchange feed and is
authoritative for price and volume. All nine watchlist tokens trade there against USD:

| Tool | Use for | Instrument format |
|---|---|---|
| `get_tickers` | Last price, 24h high/low, 24h change, volume, best bid/ask | `BTC_USD`, `TRAC_USD`, `VET_USD` |
| `get_candlestick` | 7-day change and trend from daily candles | same |
| `get_book` | Order book depth and spread on thin names | same |
| `get_trades` | Recent trade flow | same |

Verified working for BTC, ETH, LINK, HBAR, VET, TRAC, XLM, XRP, and FIL as `<TOKEN>_USD`.

The exchange feed does not carry market capitalization, circulating or total supply, unlock
schedules, or on-chain network activity. Get those from web research and label the source
separately - do not present them as exchange data.

Note that `change` from `get_tickers` is a fractional 24h change (0.0152 means +1.52%), not a
percentage. Convert before display.

### 2.5 Private company signals

For each private entry (Sygaldry Technologies, Solidigm, and any added later):

- Funding, partnership, hiring, product, or customer-validation news
- IPO or listing signals
- Why it matters to the adjacent public lane

### 2.6 Sector and cross-cutting notes

Short synthesis across the watchlist themes:

- AI infrastructure / optical photonics
- Semiconductors and memory
- Quantum computing
- Advanced nuclear and power
- Biotech and GLP-1 / pharma
- Cold chain and logistics
- Defense
- Stablecoins and crypto regulation

### 2.7 Footer

Generation timestamp in ET and the standing disclaimer:
"For research/tracking purposes only. Not financial advice."

---

## 3. Formatting

Match the existing report style in `market-watch/screener-reports/`:

- Self-contained HTML, dark theme (`#0f172a` background, `#f8fafc` text)
- Card grid layout, priority badges (`high`, `med-high`, `med`, `hold`, `high-risk`)
- Green `#22c55e` for gains, red `#ef4444` for losses
- No external assets — inline CSS only, so the file renders offline from the repo

---

## 4. Data integrity rules

- Label every figure with its source and as-of time.
- Never estimate, interpolate, or carry forward a stale price as if it were current.
- If a data source fails, say so in the report rather than omitting the entry.
- Distinguish reported facts from interpretation; keep speculation clearly marked as such.
- Follow the review rules in `watchlist.md` and `blockchain-pharma-watchlist.md` — filings outrank
  price movement.

---

## 5. Run steps

1. Read `watchlist.md` and `blockchain-pharma-watchlist.md` for the current universe.
2. Pull index levels and per-ticker market data.
3. Check SEC EDGAR (and non-U.S. equivalents) for filings since the previous report.
4. Pull crypto market and network data.
5. Search news for each equity, token, and private-company signal.
6. Write `market-watch/screener-reports/report_YYYY-MM-DD.html`.
7. Append new filings to `market-watch/filing-tracker.md`.
8. Commit as `Add market watch report for YYYY-MM-DD` and push.

## 6. Holidays

U.S. markets are closed on NYSE holidays. On a closed day, either skip the run or generate a short
note stating the market was closed and covering crypto only — crypto trades continuously.

## 7. Schedule mechanics

Driven by a Claude Routine, trigger ID `trig_01VpM5waKPTsMgEciRdHi4Pd`, on cron `32 20 * * 1-5`.

Cron is evaluated in UTC and does not follow daylight saving, so the schedule has to be shifted by
hand twice a year to stay at 4:32 PM Eastern:

| Period | Cron (UTC) | Eastern |
|---|---|---|
| EDT (Mar-Nov) | `32 20 * * 1-5` | 4:32 PM |
| EST (Nov-Mar) | `32 21 * * 1-5` | 4:32 PM |

Left unchanged over the winter the run fires at 3:32 PM ET, while the market is still open, and
every report would capture mid-session prices instead of the close.

One-shot reminder routines are scheduled to make each switch:

| Fires | Trigger ID | Action |
|---|---|---|
| 2026-11-01 | `trig_0199DnhhGkehVQtbvkpNB66d` | EDT to EST, set cron to `32 21 * * 1-5` |
| 2027-03-14 | `trig_01YZAKT22UXzFfaSH82ZodKY` | EST to EDT, set cron to `32 20 * * 1-5`, and schedule the next pair |

Each reminder fires on the Sunday of the change, before the following Monday's run, and sends a push
and email notification. The March reminder also re-arms the next two, so the chain sustains itself.
Both reminders fall back to looking the routine up by name if the trigger ID has changed.

Notification channels cannot be edited via `update_trigger`; changing them means recreating the
routine, which issues a new trigger ID. If that happens, update the ID in this table and in both
reminder prompts.

## 8. Connector availability

The Crypto.com connector is authenticated on the account, but connectors cannot be attached to
routines created through the API - the organization blocks that parameter. Scheduled runs therefore
may or may not have `mcp__Crypto_com__*` tools available.

The run prompt handles both cases: it checks for the connector tools first and uses them when
present, otherwise falls back to web research and records which source was used in the report.

To attach the connector permanently, recreate the routine from the Routines UI on claude.ai, where
connector grants can be selected.
