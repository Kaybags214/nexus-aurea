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


def test_volume_zscore_flags_spike_on_last_day():
    df = make_synthetic_ohlcv(n=100, seed=4)
    # Baseline volume was 1-5M; blow the last day out to 50M.
    df.loc[df.index[-1], "Volume"] = 50_000_000

    result = screens.volume_zscore_screen(df)

    assert result["flag"] is True
    assert result["zscore"] > 2.0
    assert result["flagged_dates"][-1]["date"] == df.index[-1].strftime("%Y-%m-%d")


def test_volume_zscore_normal_volume_not_flagged():
    df = make_synthetic_ohlcv(n=100, seed=5)
    # Replace the random volume draws with a low-variance series so this
    # assertion isn't at the mercy of an occasional random tail event.
    df["Volume"] = 2_000_000 + np.linspace(-10_000, 10_000, len(df))

    result = screens.volume_zscore_screen(df)

    assert result["flag"] is False
    assert result["flagged_dates"] == []


def test_gap_screen_flags_large_open_gap():
    df = make_synthetic_ohlcv(n=50, seed=6)
    prior_close = df["Close"].iloc[-2]
    df.loc[df.index[-1], "Open"] = prior_close * 1.10  # +10% gap up

    result = screens.gap_screen(df, threshold_pct=3.0)

    assert result["last_gap_pct"] > 3.0
    assert result["flagged_dates"][-1]["direction"] == "up"
    assert result["flagged_dates"][-1]["date"] == df.index[-1].strftime("%Y-%m-%d")


def test_gap_screen_no_flags_below_threshold():
    df = make_synthetic_ohlcv(n=50, seed=7)
    # Force every open to equal the prior close: zero gaps.
    df["Open"] = df["Close"].shift(1).fillna(df["Close"].iloc[0])

    result = screens.gap_screen(df, threshold_pct=3.0)

    assert result["flagged_dates"] == []


def test_correlation_matrix_identical_series_are_perfectly_correlated():
    base = make_synthetic_ohlcv(n=200, seed=8)
    price_data = {"A": base, "B": base.copy()}

    result = screens.correlation_matrix(price_data, window=60)

    assert result["matrix"]["A"]["B"] == 1.0
    assert result["matrix"]["A"]["A"] == 1.0


def test_correlation_matrix_drops_symbols_with_insufficient_history():
    long_history = make_synthetic_ohlcv(n=200, seed=9)
    short_history = make_synthetic_ohlcv(n=10, seed=10)
    price_data = {"LONG": long_history, "SHORT": short_history}

    result = screens.correlation_matrix(price_data, window=60)

    assert "SHORT" not in result["symbols"]
    assert result["matrix"] == {}
