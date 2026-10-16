from app.tools.crm_tools import MockCRMTool
from app.tools.market_tools import MockMarketTool


class DataFetcherAgent:
    def __init__(self, crm: MockCRMTool | None = None, market: MockMarketTool | None = None):
        self.crm = crm or MockCRMTool()
        self.market = market or MockMarketTool()

    def fetch(self, customer_id: str) -> dict:
        customer = self.crm.get_customer(customer_id)
        holdings = self.crm.get_holdings(customer_id)
        return {
            "customer": customer,
            "holdings": holdings,
            "market_context": self.market.get_market_context(),
        }
