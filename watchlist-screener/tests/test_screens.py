"""Screen logic tests using synthetic OHLCV (no network calls)."""

import numpy as np
import pandas as pd

from watchlist_screener import screens


def make_synthetic_ohlcv(n=300, seed=0, vol_regime=None) -> pd.DataFrame:
    """Random-walk close series with optional per-day volatility regime, plus
    open/high/low/volume derived from it. vol_regime defaults to constant 2%
    daily stdev; pass an array of length n to vary volatility over time.
    """
    rng = np.random.default_rng(seed)
    if vol_regime is None:
        vol_regime = np.full(n, 0.02)
    daily_returns = rng.normal(loc=0.0, scale=vol_regime)
    close = 100 * np.exp(np.cumsum(daily_returns))
    open_ = np.roll(close, 1)
    open_[0] = 100
    high = np.maximum(open_, close) * (1 + rng.uniform(0, 0.01, n))
    low = np.minimum(open_, close) * (1 - rng.uniform(0, 0.01, n))
    volume = rng.integers(1_000_000, 5_000_000, n)
    idx = pd.date_range("2024-01-01", periods=n, freq="B")
    return pd.DataFrame(
        {"Open": open_, "High": high, "Low": low, "Close": close, "Volume": volume}, index=idx
    )


def test_volatility_screen_flags_elevated_regime():
    n = 300
    vol_regime = np.full(n, 0.015)
    vol_regime[-20:] = 0.06  # recent volatility spike
    df = make_synthetic_ohlcv(n=n, seed=1, vol_regime=vol_regime)

    result = screens.volatility_screen(df)

    assert result["flag"] == "elevated"
    assert result["vol_20d_annualized"] > result["vol_1y_avg_annualized"]
    assert result["ratio_20d_vs_1y_avg"] > 1.3


def test_volatility_screen_normal_regime():
    df = make_synthetic_ohlcv(n=300, seed=2, vol_regime=np.full(300, 0.02))

    result = screens.volatility_screen(df)

    assert result["flag"] == "normal"
    assert 0.7 <= result["ratio_20d_vs_1y_avg"] <= 1.3


def test_volatility_screen_handles_short_history():
    df = make_synthetic_ohlcv(n=25, seed=3)
    result = screens.volatility_screen(df)
    # 60d vol undefined with only 25 rows
    assert result["vol_60d_annualized"] is None
    assert result["vol_20d_annualized"] is not None
