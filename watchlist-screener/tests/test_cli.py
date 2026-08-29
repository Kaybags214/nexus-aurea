"""CLI-level tests: exit codes matter for cron monitoring, so cover them directly."""

from unittest import mock

from tests.test_screens import make_synthetic_ohlcv
from watchlist_screener import cli, data


def test_main_returns_zero_when_watchlist_data_available(capsys):
    fake = {"NVDA": make_synthetic_ohlcv(n=300, seed=1)}
    with mock.patch.object(data, "fetch_all", return_value=(fake, {})):
        code = cli.main(["--tickers", "NVDA", "--proxies", ""])
    assert code == 0


def test_main_returns_nonzero_when_every_watchlist_ticker_fails(capsys):
    with mock.patch.object(data, "fetch_all", return_value=({}, {"NVDA": "boom"})):
        code = cli.main(["--tickers", "NVDA", "--proxies", ""])
    assert code == 1
    assert "every watchlist ticker failed" in capsys.readouterr().err


def test_main_returns_zero_when_only_a_proxy_fails(capsys):
    fake = {"NVDA": make_synthetic_ohlcv(n=300, seed=1)}
    with mock.patch.object(data, "fetch_all", return_value=(fake, {"SMH": "boom"})):
        code = cli.main(["--tickers", "NVDA", "--proxies", "SMH"])
    assert code == 0
