import tempfile
import unittest
from pathlib import Path
from app.agents.analyzer import AnalyzerAgent
from app.agents.data_fetcher import DataFetcherAgent
from app.memory.conversation_store import ConversationStore
from app.orchestrator import OrchestratorAgent


class WealthAdvisorTests(unittest.TestCase):
    def test_fetcher_returns_demo_customer_and_holdings(self):
        result = DataFetcherAgent().fetch("CUST-101")
        self.assertEqual(result["customer"].customer_id, "CUST-101")
        self.assertGreater(len(result["holdings"]), 0)

    def test_unknown_customer_fails_clearly(self):
        with self.assertRaisesRegex(ValueError, "Unknown customer ID"):
            DataFetcherAgent().fetch("NO-SUCH-CUSTOMER")

    def test_analyzer_allocation_adds_to_approximately_100(self):
        data = DataFetcherAgent().fetch("CUST-101")
        result = AnalyzerAgent().analyze(data)
        self.assertAlmostEqual(sum(result["asset_allocation_pct"].values()), 100, delta=0.1)
        self.assertGreater(result["total_value"], 0)

    def test_end_to_end_saves_history_and_requires_review(self):
        with tempfile.TemporaryDirectory() as folder:
            store = ConversationStore(str(Path(folder) / "test.db"))
            result = OrchestratorAgent(memory=store).run("CUST-202", "test-session")
            self.assertTrue(result["human_review_required"])
            self.assertEqual(result["summary"]["customer_id"], "CUST-202")
            self.assertEqual(len(store.get_history("CUST-202")), 1)


if __name__ == "__main__":
    unittest.main()
