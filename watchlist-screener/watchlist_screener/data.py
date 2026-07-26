"""Daily OHLCV data pull via yfinance."""

from __future__ import annotations

import pandas as pd
import yfinance as yf

REQUIRED_COLUMNS = ["Open", "High", "Low", "Close", "Volume"]


def fetch_history(ticker: str, period: str = "1y") -> pd.DataFrame:
    """Fetch daily OHLCV for a single ticker.

    Returns a DataFrame indexed by date with columns Open, High, Low, Close, Volume.
    Raises ValueError if no data comes back (bad ticker, delisted, etc.).
    """
    df = yf.Ticker(ticker).history(period=period, interval="1d", auto_adjust=False)
    if df.empty:
        raise ValueError(f"No data returned for ticker '{ticker}'")
    df = df[REQUIRED_COLUMNS].dropna(how="all")
    df.index.name = "Date"
    return df


def fetch_all(
    tickers: list[str], period: str = "1y"
) -> tuple[dict[str, pd.DataFrame], dict[str, str]]:
    """Fetch daily OHLCV for a list of tickers, skipping any that fail.

    Returns ({ticker: DataFrame}, {ticker: error_message}) so one bad ticker
    doesn't take down the rest of the screen.
    """
    data: dict[str, pd.DataFrame] = {}
    errors: dict[str, str] = {}
    for ticker in tickers:
        try:
            data[ticker] = fetch_history(ticker, period=period)
        except Exception as exc:  # noqa: BLE001 - surface any fetch failure per-ticker
            errors[ticker] = str(exc)
    return data, errors
