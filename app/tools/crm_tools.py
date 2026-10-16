"""Fictional CRM data used for local demos; replace with an approved CRM adapter."""
from app.models.schemas import CustomerProfile, Holding

CUSTOMERS = {
    "CUST-101": CustomerProfile(
        customer_id="CUST-101", name="Eleanor Vance", risk_tolerance="moderate",
        investment_horizon_years=12, primary_goal="Retirement and moderate growth",
        notes="Prefers a diversified portfolio and is concerned about volatility.",
    ),
    "CUST-202": CustomerProfile(
        customer_id="CUST-202", name="Marcus Chen", risk_tolerance="aggressive",
        investment_horizon_years=25, primary_goal="Long-term wealth accumulation",
        notes="Interested in technology and semiconductor trends.",
    ),
}

HOLDINGS = {
    "CUST-101": [
        Holding("VTI", "Total US Stock Market ETF", "Equity", 80, 210, 262.5),
        Holding("BND", "Total Bond Market ETF", "Fixed Income", 150, 74, 72.1),
        Holding("VXUS", "Total International Stock ETF", "Equity", 60, 55, 59.4),
        Holding("SHV", "Short Treasury ETF", "Cash & Equivalents", 40, 110, 110.2),
        Holding("AAPL", "Apple Inc.", "Equity", 35, 140, 225),
    ],
    "CUST-202": [
        Holding("NVDA", "NVIDIA Corporation", "Equity", 90, 45, 135),
        Holding("MSFT", "Microsoft Corporation", "Equity", 25, 310, 430),
        Holding("QQQ", "Nasdaq-100 ETF", "Equity", 30, 360, 480),
        Holding("CASH", "USD Cash Reserve", "Cash & Equivalents", 15000, 1, 1),
    ],
}


class MockCRMTool:
    def get_customer(self, customer_id: str) -> CustomerProfile:
        try:
            return CUSTOMERS[customer_id]
        except KeyError as exc:
            raise ValueError(f"Unknown customer ID: {customer_id}") from exc

    def get_holdings(self, customer_id: str) -> list[Holding]:
        self.get_customer(customer_id)  # Validate customer before returning holdings.
        return list(HOLDINGS.get(customer_id, []))
