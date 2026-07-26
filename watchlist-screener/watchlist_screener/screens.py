"""Descriptive screens computed from OHLCV data. No trading signals, no orders."""

from __future__ import annotations

import numpy as np
import pandas as pd

TRADING_DAYS_PER_YEAR = 252
ELEVATED_RATIO = 1.3
COMPRESSED_RATIO = 0.7


def volatility_screen(df: pd.DataFrame) -> dict:
    """Rolling 20/60-day annualized volatility vs. the name's own trailing 1yr average.

    - vol_20d / vol_60d: annualized stdev of daily log returns over the last N days.
    - vol_1y_avg: mean of the 20-day rolling annualized vol series over the
      available history (up to 1yr), i.e. the name's typical volatility level.
    - flag: "elevated" if current 20d vol is >30% above the 1yr average,
      "compressed" if >30% below, else "normal".
    """
    close = df["Close"]
    log_returns = np.log(close / close.shift(1))

    rolling_20 = log_returns.rolling(20).std() * np.sqrt(TRADING_DAYS_PER_YEAR)
    rolling_60 = log_returns.rolling(60).std() * np.sqrt(TRADING_DAYS_PER_YEAR)

    vol_20d = rolling_20.iloc[-1]
    vol_60d = rolling_60.iloc[-1] if not rolling_60.dropna().empty else float("nan")
    vol_1y_avg = rolling_20.mean()

    ratio_20d = vol_20d / vol_1y_avg if vol_1y_avg else float("nan")
    ratio_60d = vol_60d / vol_1y_avg if vol_1y_avg else float("nan")

    if ratio_20d > ELEVATED_RATIO:
        flag = "elevated"
    elif ratio_20d < COMPRESSED_RATIO:
        flag = "compressed"
    else:
        flag = "normal"

    return {
        "vol_20d_annualized": _round(vol_20d),
        "vol_60d_annualized": _round(vol_60d),
        "vol_1y_avg_annualized": _round(vol_1y_avg),
        "ratio_20d_vs_1y_avg": _round(ratio_20d),
        "ratio_60d_vs_1y_avg": _round(ratio_60d),
        "flag": flag,
    }


def _round(value: float, ndigits: int = 4) -> float | None:
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return None
    return round(float(value), ndigits)
