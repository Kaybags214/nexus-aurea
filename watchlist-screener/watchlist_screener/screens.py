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


def volume_zscore_screen(df: pd.DataFrame, lookback: int = 20, z_threshold: float = 2.0,
                          recent_days: int = 20) -> dict:
    """Volume z-score vs. the prior 20-day average volume.

    z on a given day = (volume - mean of the preceding `lookback` days) / stdev
    of the preceding `lookback` days. Using the *preceding* window (not
    including the day itself) avoids a big print inflating its own baseline.
    Flags any day within the last `recent_days` where |z| > z_threshold.
    """
    volume = df["Volume"]
    prior_mean = volume.shift(1).rolling(lookback).mean()
    prior_std = volume.shift(1).rolling(lookback).std()
    zscore = (volume - prior_mean) / prior_std

    flagged_dates = []
    for date, z in zscore.tail(recent_days).items():
        if pd.notna(z) and abs(z) > z_threshold:
            flagged_dates.append({
                "date": date.strftime("%Y-%m-%d"),
                "volume": int(volume.loc[date]),
                "zscore": _round(z, 2),
            })

    last_z = zscore.iloc[-1]
    return {
        "last_volume": int(volume.iloc[-1]),
        "avg_volume_20d": _round(prior_mean.iloc[-1], 0),
        "zscore": _round(last_z, 2),
        "flag": bool(pd.notna(last_z) and abs(last_z) > z_threshold),
        "flagged_dates": flagged_dates,
    }


def gap_screen(df: pd.DataFrame, threshold_pct: float = 3.0, recent_days: int = 20) -> dict:
    """Overnight gap detection: open vs. prior close, flagged when |gap| > threshold_pct.

    Purely descriptive - flags the days it happened, no directional call on
    what happens next.
    """
    prior_close = df["Close"].shift(1)
    gap_pct = (df["Open"] - prior_close) / prior_close * 100

    flagged_dates = []
    for date, gap in gap_pct.tail(recent_days).items():
        if pd.notna(gap) and abs(gap) > threshold_pct:
            flagged_dates.append({
                "date": date.strftime("%Y-%m-%d"),
                "gap_pct": _round(gap, 2),
                "direction": "up" if gap > 0 else "down",
            })

    last_gap = gap_pct.iloc[-1]
    return {
        "threshold_pct": threshold_pct,
        "last_gap_pct": _round(last_gap, 2),
        "flagged_dates": flagged_dates,
    }


def correlation_matrix(price_data: dict[str, pd.DataFrame], window: int = 60) -> dict:
    """Rolling correlation matrix of daily log returns over the trailing `window`
    days, across every ticker/proxy passed in. Symbols with fewer than `window`
    overlapping days of history are dropped from the matrix rather than
    producing a misleading partial-window correlation.
    """
    returns = {}
    for symbol, df in price_data.items():
        close = df["Close"]
        returns[symbol] = np.log(close / close.shift(1))

    returns_df = pd.DataFrame(returns).dropna(how="all")
    windowed = returns_df.tail(window).dropna(axis=1, thresh=window)

    if windowed.shape[1] < 2:
        return {"window": window, "symbols": list(windowed.columns), "matrix": {}}

    corr = windowed.corr()
    matrix = {
        row: {col: _round(corr.loc[row, col], 3) for col in corr.columns}
        for row in corr.index
    }
    return {"window": window, "symbols": list(corr.columns), "matrix": matrix}


def _round(value: float, ndigits: int = 4) -> float | None:
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return None
    return round(float(value), ndigits)
