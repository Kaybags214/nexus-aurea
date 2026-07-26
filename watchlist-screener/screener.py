#!/usr/bin/env python3
"""Run on demand: python screener.py [--tickers ...] [--format markdown|json]"""

from watchlist_screener.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
