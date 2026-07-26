#!/usr/bin/env python3
"""Run on demand: python screener.py [--tickers ...] [--format markdown|json]"""

from watchlist_screener.cli import _run_as_script

if __name__ == "__main__":
    _run_as_script()
