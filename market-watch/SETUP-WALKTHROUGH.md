# Setup Walkthrough - Plain Language

For getting the daily market watch report to include real financial data and SEC filings.

No coding. Nothing to install. About 10 minutes.

---

## First, the words

| Word | What it actually means |
|---|---|
| **Connector** | A switch you flip on the Claude website to let Claude use another service. You already have several: Gmail, Google Drive, Crypto.com. |
| **UI** | Just the claude.ai website. |
| **API key** | A password issued by a data company. **We are probably not using one.** |
| **Routine** | The scheduled job that writes the report every weekday at 4:32 PM. |
| **Egress proxy** | The thing blocking Claude from reaching outside websites. This is the actual problem. |

---

## The problem in one paragraph

This workspace blocks Claude from reaching almost every outside website, including sec.gov and
every stock-data site. But it does *not* block connectors, because those travel a different route.
That is why crypto prices work (Crypto.com is a connector) and stock filings do not (those need
sec.gov, which is blocked). The fix is to add a connector for financial data, rather than buying a
data subscription that Claude still would not be able to reach.

---

## Step 1 - Turn on a financial data connector

1. Go to **claude.ai** and sign in.
2. Open **Settings**, then **Connectors**.
3. Search for **Alpha Vantage**.
4. Click **Connect** and follow the sign-in prompts.

Alpha Vantage has a free tier and covers stock prices, fundamentals, earnings, news, and some SEC
filing data.

If you would rather have deeper filing coverage and do not mind paying, **Bigdata.com** is built
specifically for SEC filings and earnings calls and returns cited source documents. Either one
works with these instructions.

## Step 2 - Rebuild the daily routine so it can use the connector

This step is necessary because a routine only gets the connectors that were selected when it was
created. The existing one was created without any.

1. On claude.ai, go to **Routines**.
2. Open **Daily Market Watch Report (Mon-Fri, 4:30 PM ET)**.
3. Copy its prompt text somewhere safe, then **delete** the routine.
4. Create a new routine:
   - **Name:** Daily Market Watch Report (Mon-Fri, 4:30 PM ET)
   - **Schedule:** 4:32 PM Eastern, Monday through Friday
   - **Connectors:** tick **Alpha Vantage** and **Crypto.com**
   - **Notifications:** push and email
   - **Prompt:** paste the text you copied
5. Save.

## Step 3 - Test it

Ask Claude to run the routine once immediately, before waiting for 4:32. Check that the report
actually contains fundamentals and filing data rather than DATA UNAVAILABLE.

---

## Optional - the cleaner fix for filings

Alpha Vantage gives *some* filing data. To get the full "read the 10-K and tell me what changed"
version, sec.gov needs to be unblocked for this workspace. EDGAR is free and authoritative, so this
is better than paying a vendor to resell it.

That is an environment network setting, not a connector. It is documented at
https://code.claude.com/docs/en/claude-code-on-the-web

Claude cannot change this from inside a session - it has to be set on the environment.

---

## What is already working, with no action needed

- The routine runs Monday to Friday at 4:32 PM ET and commits to `main`
- Push and email notifications are on
- Daylight saving reminders are scheduled for 2026-11-01 and 2027-03-14, and re-arm themselves
- Crypto prices, index levels, news, and sector notes all work today
- Watchlist entries are read from the watchlist files on every run, so adding a ticker there is
  enough to get it covered

## What does not work yet

- SEC filing contents (10-K, 10-Q, 8-K) - discoverable by search, not readable
- Deep fundamentals for most names - P/E, EV/EBITDA, free cash flow, short interest, ownership
- Reliable closing prices for roughly half the watchlist

See `screener-reports/sample_2026-08-21.html` for exactly what this looks like in practice.
