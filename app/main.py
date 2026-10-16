import argparse
import json
import logging
from app.orchestrator import OrchestratorAgent


def main() -> None:
    parser = argparse.ArgumentParser(description="Local demo of a multi-agent Wealth Advisor Assistant")
    parser.add_argument("--customer", default="CUST-101", help="Demo customer ID (CUST-101 or CUST-202)")
    parser.add_argument("--db", default="wealth_advisor_memory.db", help="SQLite database path")
    parser.add_argument("--history", action="store_true", help="Show saved summary count for the customer")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    advisor = OrchestratorAgent()
    # Keep the database path configurable for reproducible local runs.
    if args.db != "wealth_advisor_memory.db":
        from app.memory.conversation_store import ConversationStore
        advisor.memory = ConversationStore(args.db)
    if args.history:
        print(json.dumps({"history": advisor.memory.get_history(args.customer)}, indent=2))
        return
    result = advisor.run(args.customer)
    print(json.dumps(result, indent=2, default=lambda value: value.__dict__))


if __name__ == "__main__":
    main()
