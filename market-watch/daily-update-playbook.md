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

The run is driven by a Claude Routine on cron `32 20 * * 1-5` (UTC), which is 4:32 PM Eastern while
U.S. Eastern Daylight Time is in effect.

Cron is evaluated in UTC and does not follow daylight saving. When the U.S. returns to Eastern
Standard Time in early November, the schedule must move to `32 21 * * 1-5` to stay at 4:32 PM ET,
and back to `32 20 * * 1-5` when EDT resumes in March. Left unchanged over the winter, the run would
fire at 3:32 PM ET — while the market is still open.
