from datetime import datetime, timezone
import logging
import uuid
from app.agents.data_fetcher import DataFetcherAgent
from app.agents.analyzer import AnalyzerAgent
from app.memory.conversation_store import ConversationStore
from app.models.schemas import AdvisorSummary

logger = logging.getLogger(__name__)


class OrchestratorAgent:
    def __init__(self, fetcher=None, analyzer=None, memory=None):
        self.fetcher = fetcher or DataFetcherAgent()
        self.analyzer = analyzer or AnalyzerAgent()
        self.memory = memory or ConversationStore()

    def run(self, customer_id: str, session_id: str | None = None) -> dict:
        session_id = session_id or str(uuid.uuid4())
        logger.info("Orchestrator started for %s", customer_id)
        data = self.fetcher.fetch(customer_id)
        analysis = self.analyzer.analyze(data)
        profile = data["customer"]
        recommendations = [
            "Review the allocation and concentration figures with a qualified financial advisor.",
            "Confirm current goals, time horizon, tax situation, and liquidity needs before considering changes.",
        ]
        if analysis["top_concentrations_pct"][0][1] >= 35:
            recommendations.insert(0, "Discuss single-holding concentration risk during the advisor review.")

        summary = AdvisorSummary(
            customer_id=customer_id,
            timestamp=datetime.now(timezone.utc).isoformat(),
            executive_summary=(
                f"{profile.name}'s illustrative portfolio is valued at ${analysis['total_value']:,.2f}, "
                f"with an unrealized gain/loss of ${analysis['unrealized_pnl']:,.2f}. "
                f"The stated goal is: {profile.primary_goal}."
            ),
            facts=[
                f"Risk tolerance on file: {profile.risk_tolerance}.",
                f"Investment horizon on file: {profile.investment_horizon_years} years.",
                *analysis["observations"],
                "Market context is mock data and is not a live market feed.",
            ],
            assumptions=["Holdings and prices are fictional demo inputs.", "Taxes, fees, outside assets, and personal circumstances have not been assessed."],
            recommendations=recommendations,
        )
        self.memory.record_message(session_id, customer_id, "user", f"Generate advisor summary for {customer_id}")
        self.memory.record_message(session_id, customer_id, "assistant", summary.executive_summary)
        self.memory.save_summary(summary)
        return {"customer": profile, "analysis": analysis, "summary": summary.to_dict(), "human_review_required": True}
