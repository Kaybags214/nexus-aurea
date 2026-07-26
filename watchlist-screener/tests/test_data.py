"""Tests for the fetch watchdog: a stuck ticker must not hang the whole run."""

import time
from unittest import mock

from watchlist_screener import data
from tests.test_screens import make_synthetic_ohlcv


def test_fetch_all_times_out_stuck_ticker_without_hanging():
    def fake_fetch_history(ticker, period="1y", timeout=data.REQUEST_TIMEOUT):
        if ticker == "STUCK":
            time.sleep(5)  # simulates a stalled network call
            return make_synthetic_ohlcv(n=300, seed=0)
        return make_synthetic_ohlcv(n=300, seed=1)

    with mock.patch.object(data, "fetch_history", side_effect=fake_fetch_history):
        started = time.monotonic()
        result_data, errors = data.fetch_all(["OK", "STUCK"], fetch_timeout=0.5)
        elapsed = time.monotonic() - started

    assert elapsed < 3, "fetch_all should return promptly once the watchdog fires"
    assert "OK" in result_data
    assert "STUCK" in errors
    assert "timed out" in errors["STUCK"]


def test_fetch_all_reports_exceptions_per_ticker():
    def fake_fetch_history(ticker, period="1y", timeout=data.REQUEST_TIMEOUT):
        if ticker == "BAD":
            raise ValueError("No data returned for ticker 'BAD'")
        return make_synthetic_ohlcv(n=300, seed=2)

    with mock.patch.object(data, "fetch_history", side_effect=fake_fetch_history):
        result_data, errors = data.fetch_all(["GOOD", "BAD"])

    assert "GOOD" in result_data
    assert errors["BAD"] == "No data returned for ticker 'BAD'"
