# Wealth Advisor Assistant — Multi-Agent Demo

A small, local Python demonstration of a multi-agent workflow for wealth-advisor support. It uses fictional customer and holding data, deterministic mock market context, and SQLite memory. It does not connect to a brokerage, execute trades, or provide personalized regulated financial advice.

## Architecture

- **Orchestrator Agent** coordinates retrieval, analysis, summary generation, memory writes, and the human-review gate.
- **Data Fetcher Agent** retrieves a fictional customer profile and holdings from the mock CRM and gets illustrative market context.
- **Analyzer Agent** calculates portfolio value, cost, unrealized gain/loss, asset-class allocation, and largest holding concentrations.
- **Mock tools** keep the demo runnable without API keys. Replace these adapters only after selecting and authorizing real data sources.
- **SQLite memory** stores session messages and historical summaries locally.
- **Human review** is always required. The output is for advisor discussion; the application never trades or performs external actions.

## Requirements

- Python 3.10 or newer
- No paid API key or network access required
- Optional: `pytest` for test execution

## Run

From this project directory:

```bash
python -m app.main
python -m app.main --customer CUST-202
python -m app.main --db ./data/demo.db --customer CUST-101
python -m app.main --history --customer CUST-101
```

The first run creates a local SQLite database. The default database is `wealth_advisor_memory.db` and is ignored by Git.

## Tests

```bash
python -m unittest discover -s tests -v
```

Or install the optional test dependency and run:

```bash
python -m pip install -r requirements.txt
pytest -q
```

## Example workflow

1. The orchestrator receives a demo customer ID.
2. The data-fetcher retrieves the profile, holdings, and mock market context.
3. The analyzer calculates metrics and flags large concentrations for review.
4. The orchestrator builds a summary, labels demo assumptions, and saves the interaction and summary in SQLite.
5. The result clearly states that human review is required.

## Sample customers

- `CUST-101`: moderate risk tolerance, retirement and moderate growth goal.
- `CUST-202`: aggressive risk tolerance, long-term accumulation goal.

All names, prices, quantities, and market values are fictional illustrative data. Metrics are arithmetic summaries of the supplied sample holdings, not verified live valuations.

## Limitations and next steps

- Market data and CRM records are mock implementations.
- No LLM is required; agent behavior is deterministic so tests are reproducible.
- Before real use, add authentication, authorization, consent, audit controls, data-quality checks, secure secret handling, and compliance review. Integrate only approved APIs and have a qualified advisor review any client-facing output.
- Consider adding schema-based API adapters, portfolio benchmark comparison, richer risk metrics, and a UI after the core workflow is reviewed.

## GitHub preparation

```bash
git init
git add .
git commit -m "Build wealth advisor multi-agent demo"
```

Review the files before pushing. Never commit credentials, real client information, or local database files.
