# SEC Filing Tracker

Purpose: Track SEC filings and extract business-relevant findings.

| Date Reviewed | Ticker | Company | Filing Type | Filing Date | Key Finding | Action |
|---|---|---|---|---|---|---|
| 2026-07-05 | CARV | Carver Bancorp, Inc. | Watchlist Start |  | Community bank / ownership watch | Pull latest 10-Q, 10-K, 8-Ks |
| 2026-07-05 | INFQ | Infleqtion Inc. | Watchlist Start |  | Quantum technology / public-company watch | Pull latest 8-K and public filings |
| 2026-07-05 | LIFE | Ethos Technologies | Watchlist Start |  | Insurtech / public-company watch | Pull IPO filing and public reports |
| 2026-08-24 | WQTM | WisdomTree Quantum Computing Fund | ETF (N-CEN / N-CSR / N-PORT / 485BPOS) | Inception 2025-10-09 | Verified. US-listed ETF on Cboe BATS tracking the WisdomTree Classiq Quantum Computing Index; 53 holdings, 0.45% expense ratio, ~31% foreign issues, growth rather than income. A registered investment company, not an operating company, so it files no 10-K, 10-Q, or 8-K. | Track holdings, concentration, and index changes via N-PORT and N-CSR, plus 485BPOS for prospectus changes. Do not look for company filings. |


### Note on WQTM

Two different funds use the WQTM ticker. The watchlist entry is the **US** fund, the WisdomTree
Quantum Computing Fund on Cboe BATS. WisdomTree also runs a European namesake, the WisdomTree
Quantum Computing UCITS ETF (WQTM/QWTM), which is a separate vehicle with its own disclosure regime.
Confirm which one a data source is quoting before recording anything here.

Sources: [Morningstar](https://www.morningstar.com/etfs/bats/wqtm/quote),
[ETF Database](https://etfdb.com/etf/WQTM/),
[WisdomTree Europe (UCITS namesake)](https://www.wisdomtree.eu/en-gb/etfs/thematic/wqtm---wisdomtree-quantum-computing-ucits-etf---usd-acc)

## Filing Review Checklist

### 8-K

- What happened?
- Is it material?
- Does it involve management, debt, acquisition, financing, resignation, litigation, delisting risk, or capital structure?
- Does it change the thesis?

### 10-Q

- Revenue trend
- Net income or loss
- Cash position
- Debt
- Dilution or share count
- Segment performance
- Risk factor changes

### 10-K

- Business model
- Major risks
- Regulatory exposure
- Debt and liquidity
- Management discussion
- Ownership structure
- Long-term strategic position

### DEF 14A

- Board structure
- Executive compensation
- Shareholder proposals
- Insider ownership
- Voting control

### Form 4

- Insider buying
- Insider selling
- Option grants
- Pattern of transactions
