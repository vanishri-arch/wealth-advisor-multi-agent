# Wealth Advisor Assistant — Multi-Agent AI

A Python-based demonstration of a multi-agent AI workflow for wealth-advisor support. The project combines customer data retrieval, portfolio analysis, orchestration, persistent conversation memory, and human-in-the-loop review.

> **Disclaimer:** This is an educational demo using fictional customer data and mock market context. It does not connect to a brokerage, execute trades, or provide personalized financial advice.

## Project Overview

The application coordinates specialized components to produce a portfolio summary for advisor review.

### Architecture

- **Orchestrator Agent:** Coordinates data retrieval, analysis, summary generation, memory updates, and the human-review gate.
- **Data Fetcher Agent:** Retrieves fictional customer profiles and holdings through mock CRM tools and illustrative market context.
- **Analyzer Agent:** Calculates portfolio value, cost basis, unrealized gain or loss, asset-class allocation, and holding concentrations.
- **SQLite Conversation Memory:** Persists session messages and historical advisor summaries locally.
- **Human-in-the-Loop Review:** Keeps advisor review in the workflow. Generated summaries are not treated as approved financial recommendations.
- **Mock Tools:** Allow the application to run without paid API keys or external service connections.

## Key Features

- Multiple specialized components coordinated through an orchestrator.
- Portfolio calculations and asset-allocation analysis.
- Customer-specific demo scenarios.
- Persistent SQLite storage for conversation history and summaries.
- Human-review status included in generated summaries.
- Automated tests for core calculations, customer retrieval, history persistence, and error handling.
- Local execution without external API credentials.

## Technology Stack

- Python
- SQLite
- Standard-library database and data-handling tools
- `unittest` for automated testing
- `pytest` (optional)

## Project Structure

```text
wealth-advisor-multi-agent/
├── app/
│   ├── agents/
│   │   ├── analyzer.py
│   │   └── data_fetcher.py
│   ├── memory/
│   │   └── conversation_store.py
│   ├── models/
│   │   └── schemas.py
│   ├── tools/
│   │   ├── crm_tools.py
│   │   └── market_tools.py
│   ├── main.py
│   └── orchestrator.py
├── data/
├── tests/
│   └── test_wealth_advisor.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- No paid API key required
- No external network connection required for the demo

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/vanishri-arch/wealth-advisor-multi-agent.git
cd wealth-advisor-multi-agent
```

### 2. Run the application

Run the default demo customer:

```bash
python -m app.main
```

Run a specific demo customer:

```bash
python -m app.main --customer CUST-101
```

```bash
python -m app.main --customer CUST-202
```

### 3. View saved history

```bash
python -m app.main --history --customer CUST-101
```

The application stores local conversation and summary history in SQLite. The default database file is excluded from Git through `.gitignore`.

## Running Tests

Run the test suite using Python's built-in test runner:

```bash
python -m unittest discover -s tests -v
```

Alternatively, install the optional test dependency and use `pytest`:

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

## Current Limitations

- Customer profiles, holdings, and market context are illustrative and use mock data.
- The application is a demonstration, not a production financial-advisory system.
- No live brokerage, market-data provider, CRM, or external AI API is connected.
- Portfolio outputs require human review and should not be interpreted as personalized financial advice.
- Production deployment would require authorized data integrations, security controls, audit logging, monitoring, and additional validation.

## Future Improvements

- Add an authorized live market-data integration.
- Integrate a real CRM through approved APIs.
- Add configurable risk and portfolio-analysis rules.
- Expand automated tests and evaluation scenarios.
- Introduce authentication, access controls, and audit trails for production readiness.

## Author

**Vanishri**

GitHub: [@vanishri-arch](https://github.com/vanishri-arch)

---

*Built as a practical demonstration of multi-agent orchestration, portfolio analysis, persistent memory, and human-in-the-loop workflow design.*
