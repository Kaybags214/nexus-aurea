# Flow Brief Routine — setup

An alerts-only daily brief built on the **Webull Prime** endpoints. It complements the
existing Abacus.AI "Nexus Aurea Daily Market Watch Report" rather than replacing it:
Abacus works from price and news, this works from large-order capital flow, analyst
consensus and earnings estimates — the data a price-only workflow cannot see.

## Why this is not created automatically

A scheduled routine created from inside a Claude Code session cannot carry MCP connectors
on this account — the `connectors` parameter is unavailable, and a routine without them
fires sessions with no `mcp__Webull__*` tools at all. Since the Webull data *is* the brief,
such a routine would fail every run.

**Create it from the claude.ai Routines UI instead**, where the Webull connector can be
attached to the routine.

## Settings

| Field | Value |
|---|---|
| Name | Nexus Aurea Flow Brief (weekdays, after close) |
| Schedule | Weekdays, 5:30pm ET — cron `30 21 * * 1-5` (UTC) |
| Session | Fresh session per run |
| Connectors | **Webull** (required), Alpha Vantage (optional, for FX conversion) |
| Notifications | Push on |

Note on daylight saving: `30 21 * * 1-5` is 5:30pm ET while EDT is in effect. When EST
begins in November it becomes 4:30pm ET — change the hour to `22` to hold 5:30pm ET.

## Prompt

Paste this verbatim as the routine's prompt.

```
Run the Nexus Aurea daily flow brief for the session that just closed. This is an alerts-only brief: it exists to surface divergences that a price-and-news workflow would miss, NOT to restate the day's prices. A quiet day should produce a short note, not a padded report.

REPO: Kaybags214/nexus-aurea (clone it if the session doesn't have it).

STEP 1 — Build the ticker list dynamically from the repo, so it always stays in sync:
- Equities/ETFs: every ticker in the Active Watchlist table of `market-watch/watchlist.md`.
- Crypto: every ticker in `market-watch/blockchain-pharma-watchlist.md`.
- Also pull the Webull "Prime" watchlist via mcp__Webull__get_watchlists + get_watchlist_instruments and note any Prime name that has no entry in watchlist.md.
Never hardcode tickers — read them from the files each run.

STEP 2 — Pull data via the Webull connector (these are paid Prime endpoints; use them, they are the point of this brief):
- get_stock_snapshot for the full list (US_STOCK and US_ETF separately, max 100 symbols per call).
- get_stock_capital_flow (count 3) for every name that moved more than 3% on the day, plus MU, NVDA and any name held in the account.
- get_account_list / get_account_balance / get_account_positions to check current holdings.
- get_analyst_target_price and get_analyst_rating for any name whose alert fires below.
- get_financial_alert for upcoming earnings estimates on watchlist names.

STEP 3 — Fire an alert ONLY when one of these concrete conditions is met. Report nothing else.
1. FLOW/PRICE DIVERGENCE: net large-order flow (large_in minus large_out) is opposite in sign to the day's price move, and is either >= $100M absolute or >= 2% of market cap. (This is the pattern that caught MU on 2026-08-28: -$1.22B net large outflow on a -0.27% close.)
2. DISTRIBUTION TO RETAIL: large orders net negative while small orders net positive.
3. ALL-TIER SELLING: large, medium and small order flow all net negative on the same day.
4. FLOW REVERSAL: net large-order flow flips sign versus the prior session by more than $100M.
5. BELOW THE FLOOR: close is below the single lowest analyst target price.
6. CONSENSUS CROSS: mean analyst target crosses through the current price, or the rating mix shifts materially (a new sell rating, or holds becoming a majority).
7. REVENUE GOING BACKWARDS: an upcoming earnings estimate shows revenue below the prior-year comparable.
8. NEW 52-WEEK LOW, or a close within 3% of one.
9. HOLDINGS CHECK: any alert on a name actually held in the Webull account is always reported and listed first.

STEP 4 — Write the brief to `market-watch/flow-briefs/YYYY-MM-DD.md` in the repo. Keep it tight: a one-line verdict at the top, then one short block per fired alert naming the ticker, which condition fired, the actual numbers, and what it would mean. If nothing fires, write a single line recording that the checks ran and nothing tripped. Commit directly to `main` (matching how the existing daily reports land) with a message summarising the alerts, and push.

RULES:
- Report only what the data shows. Derived figures must be labelled as derived, and net assets are never described as cash.
- One session of flow data is not a trend — say so when a signal rests on a single print.
- "Large order" is a proxy for institutional activity, not 13F data.
- Watch for currency mismatches: some analyst targets come back in a non-USD currency (Novo Nordisk's are in DKK). Convert before comparing to a USD price.
- This is research and education, not financial advice, and not a recommendation to trade. Never place, suggest placing, or size a trade.
- Hyatt (H) is the user's employer: public filings only, never non-public workplace information.
- If the market was closed that day (holiday), do nothing and exit without committing.
```

## Where the alert conditions came from

Each condition is derived from a pattern found in the 2026-08-28 session review
(`market-watch/analysis/2026-08-29-webull-portfolio-watchlist-review.html`), not invented:

- **Condition 1** — MU closed -0.27% on -$1.22B net large-order outflow. Invisible on price alone.
- **Condition 2** — OKLO showed large orders net out while small orders were net in.
- **Condition 3** — CRCL sold off across all three order-size tiers at once.
- **Condition 4** — MRVL flipped from -$472M to +$542M net large flow in one session.
- **Condition 5** — COHR closed below the lowest analyst target on the street.
- **Condition 7** — SMR's Q3 revenue estimate is $3.81M against $8.24M a year prior.

## Existing automation, for reference

The Abacus.AI task "Nexus Aurea Daily Market Watch Report" reads `market-watch/watchlist.md`
and `market-watch/blockchain-pharma-watchlist.md`, writes
`market-watch/screener-reports/report_YYYY-MM-DD.html`, commits it, then emails a completion
link. On 2026-08-28 the commit landed at 21:15:49 UTC and the email at 21:16:31 UTC.

Because `watchlist.md` is the source list for both workflows, adding a ticker there picks it
up in both — no separate registration needed.
