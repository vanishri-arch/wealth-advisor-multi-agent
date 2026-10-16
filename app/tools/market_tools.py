"""Deterministic market context for demos; values are illustrative, not live data."""


class MockMarketTool:
    def get_market_context(self) -> dict[str, str | float]:
        return {
            "source": "mock market feed",
            "market_volatility": "normal (illustrative value)",
            "benchmark_ytd_return_pct": 8.0,
        }
