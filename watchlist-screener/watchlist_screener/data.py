"""Daily OHLCV data pull via yfinance."""

from __future__ import annotations

import sys
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeoutError

import pandas as pd
import yfinance as yf

REQUIRED_COLUMNS = ["Open", "High", "Low", "Close", "Volume"]

# yfinance issues a handful of sequential HTTP calls per ticker (cookie, crumb,
# chart data), each with its own ~10-30s default timeout and no retries. A
# stalled connection (rate limiting, a flaky network) can therefore make a
# single ticker take minutes. REQUEST_TIMEOUT bounds each individual yfinance
# HTTP call; FETCH_TIMEOUT is a hard per-ticker wall-clock ceiling enforced by
# a worker thread, so one bad ticker can never block the whole run.
REQUEST_TIMEOUT = 15
FETCH_TIMEOUT = 45


def fetch_history(ticker: str, period: str = "1y", timeout: int = REQUEST_TIMEOUT) -> pd.DataFrame:
    """Fetch daily OHLCV for a single ticker.

    Returns a DataFrame indexed by date with columns Open, High, Low, Close, Volume.
    Raises ValueError if no data comes back (bad ticker, delisted, etc.).
    """
    df = yf.Ticker(ticker).history(
        period=period, interval="1d", auto_adjust=False, timeout=timeout
    )
    if df.empty:
        raise ValueError(f"No data returned for ticker '{ticker}'")
    df = df[REQUIRED_COLUMNS].dropna(how="all")
    df.index.name = "Date"
    return df


def fetch_all(
    tickers: list[str], period: str = "1y", fetch_timeout: int = FETCH_TIMEOUT
) -> tuple[dict[str, pd.DataFrame], dict[str, str]]:
    """Fetch daily OHLCV for a list of tickers in parallel, skipping any that fail.

    Each ticker gets at most `fetch_timeout` seconds; a ticker that blows past
    it is recorded as an error and the run continues rather than hanging.
    Returns ({ticker: DataFrame}, {ticker: error_message}).
    """
    data: dict[str, pd.DataFrame] = {}
    errors: dict[str, str] = {}

    # Not using `with ThreadPoolExecutor(...)`: its __exit__ calls
    # shutdown(wait=True), which would block on exactly the stuck worker
    # threads this function exists to time out on. shutdown(wait=False)
    # below lets the process move on and abandons any still-blocked workers
    # as daemon-like leftovers (the CLI force-exits at the end regardless).
    pool = ThreadPoolExecutor(max_workers=min(8, len(tickers)) or 1)
    futures = {pool.submit(fetch_history, ticker, period): ticker for ticker in tickers}
    for future, ticker in futures.items():
        print(f"Fetching {ticker}...", file=sys.stderr, flush=True)
        try:
            data[ticker] = future.result(timeout=fetch_timeout)
            print(f"  {ticker}: {len(data[ticker])} rows", file=sys.stderr, flush=True)
        except FutureTimeoutError:
            errors[ticker] = f"timed out after {fetch_timeout}s"
            print(f"  {ticker}: timed out after {fetch_timeout}s", file=sys.stderr, flush=True)
        except Exception as exc:  # noqa: BLE001 - surface any fetch failure per-ticker
            errors[ticker] = str(exc)
            print(f"  {ticker}: {exc}", file=sys.stderr, flush=True)
    pool.shutdown(wait=False)

    return data, errors
