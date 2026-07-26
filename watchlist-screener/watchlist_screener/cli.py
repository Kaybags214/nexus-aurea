"""CLI entry point: on-demand watchlist screener. Not a scheduled job."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

from . import data, screens

DEFAULT_TICKERS = ["RGTI", "INFQ", "UONEK", "CARV", "NVDA", "QBTS"]
DEFAULT_PROXIES = ["SMH", "QTUM"]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Descriptive watchlist screener (volatility, volume, correlation, gaps). "
        "No trading signals or order execution."
    )
    parser.add_argument(
        "--tickers",
        default=",".join(DEFAULT_TICKERS),
        help=f"Comma-separated watchlist tickers (default: {','.join(DEFAULT_TICKERS)})",
    )
    parser.add_argument(
        "--proxies",
        default=",".join(DEFAULT_PROXIES),
        help=f"Comma-separated sector-proxy tickers (default: {','.join(DEFAULT_PROXIES)})",
    )
    parser.add_argument("--period", default="1y", help="yfinance history period (default: 1y)")
    parser.add_argument(
        "--format", choices=["markdown", "json"], default="markdown", help="Report output format"
    )
    parser.add_argument("--output", help="Write report to this file instead of stdout")
    parser.add_argument(
        "--fetch-timeout",
        type=int,
        default=data.FETCH_TIMEOUT,
        help=f"Max seconds to wait per ticker before giving up on it (default: {data.FETCH_TIMEOUT})",
    )
    parser.add_argument(
        "--z-threshold",
        type=float,
        default=2.0,
        help="Volume z-score magnitude that counts as a flagged day (default: 2.0)",
    )
    parser.add_argument(
        "--gap-threshold",
        type=float,
        default=3.0,
        help="Open-vs-prior-close gap %% that counts as a flagged day (default: 3.0)",
    )
    parser.add_argument(
        "--corr-window",
        type=int,
        default=60,
        help="Trailing days of returns used for the correlation matrix (default: 60)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    tickers = [t.strip().upper() for t in args.tickers.split(",") if t.strip()]
    proxies = [t.strip().upper() for t in args.proxies.split(",") if t.strip()]
    all_symbols = tickers + [p for p in proxies if p not in tickers]

    price_data, errors = data.fetch_all(
        all_symbols, period=args.period, fetch_timeout=args.fetch_timeout
    )
    for ticker, message in errors.items():
        print(f"warning: skipping {ticker}: {message}", file=sys.stderr)

    results = {}
    usable_price_data = {}
    for ticker, df in price_data.items():
        if len(df) < 20:
            errors.setdefault(ticker, "fewer than 20 trading days of history; skipping")
            continue
        usable_price_data[ticker] = df
        results[ticker] = {
            "last_date": df.index[-1].strftime("%Y-%m-%d"),
            "last_close": round(float(df["Close"].iloc[-1]), 4),
            "volatility": screens.volatility_screen(df),
            "volume": screens.volume_zscore_screen(df, z_threshold=args.z_threshold),
            "gaps": screens.gap_screen(df, threshold_pct=args.gap_threshold),
        }

    correlation = screens.correlation_matrix(usable_price_data, window=args.corr_window)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "period": args.period,
        "watchlist": tickers,
        "sector_proxies": proxies,
        "errors": errors,
        "tickers": results,
        "correlation": correlation,
    }

    if args.format == "json":
        output = json.dumps(report, indent=2)
    else:
        output = _render_markdown(report)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output + "\n")
    else:
        print(output)
    return 0


def _render_markdown(report: dict) -> str:
    lines = [
        "# Watchlist Screener Report",
        "",
        f"Generated: {report['generated_at']}",
        f"Period: {report['period']}",
        f"Watchlist: {', '.join(report['watchlist'])}",
        f"Sector proxies: {', '.join(report['sector_proxies'])}",
        "",
        "## Volatility (20/60-day vs. 1yr average)",
        "",
        "| Ticker | Last Close | Vol 20d | Vol 60d | Vol 1yr Avg | 20d/1yr Ratio | Flag |",
        "|---|---|---|---|---|---|---|",
    ]
    for ticker, info in report["tickers"].items():
        v = info["volatility"]
        lines.append(
            f"| {ticker} | {info['last_close']} | {v['vol_20d_annualized']} | "
            f"{v['vol_60d_annualized']} | {v['vol_1y_avg_annualized']} | "
            f"{v['ratio_20d_vs_1y_avg']} | {v['flag']} |"
        )

    lines += [
        "",
        "## Volume Z-Score (vs. prior 20-day average)",
        "",
        "| Ticker | Last Volume | Avg Vol 20d | Z-Score | Flag | Flagged Days (last 20) |",
        "|---|---|---|---|---|---|",
    ]
    for ticker, info in report["tickers"].items():
        vol = info["volume"]
        flagged = ", ".join(f"{d['date']} (z={d['zscore']})" for d in vol["flagged_dates"]) or "-"
        lines.append(
            f"| {ticker} | {vol['last_volume']:,} | {vol['avg_volume_20d']:,.0f} | "
            f"{vol['zscore']} | {vol['flag']} | {flagged} |"
        )

    lines += [
        "",
        "## Gap Detection (open vs. prior close)",
        "",
        "| Ticker | Threshold | Last Gap % | Flagged Days (last 20) |",
        "|---|---|---|---|",
    ]
    for ticker, info in report["tickers"].items():
        gaps = info["gaps"]
        flagged = (
            ", ".join(f"{d['date']} ({d['gap_pct']}%, {d['direction']})" for d in gaps["flagged_dates"])
            or "-"
        )
        lines.append(
            f"| {ticker} | {gaps['threshold_pct']}% | {gaps['last_gap_pct']}% | {flagged} |"
        )

    corr = report["correlation"]
    lines += [
        "",
        f"## Correlation Matrix (last {corr['window']} trading days, daily returns)",
        "",
    ]
    if corr["matrix"]:
        symbols = corr["symbols"]
        lines.append("| | " + " | ".join(symbols) + " |")
        lines.append("|---|" + "---|" * len(symbols))
        for row in symbols:
            values = " | ".join(str(corr["matrix"][row][col]) for col in symbols)
            lines.append(f"| {row} | {values} |")
    else:
        lines.append("Not enough overlapping history to compute a correlation matrix.")

    if report["errors"]:
        lines += ["", "## Errors", ""]
        lines += [f"- {ticker}: {msg}" for ticker, msg in report["errors"].items()]
    return "\n".join(lines)


def _run_as_script() -> None:
    """Run main() and force the process to exit even if a stalled network
    thread from yfinance is still alive in the background (see data.py)."""
    code = main()
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(code)


if __name__ == "__main__":
    _run_as_script()
