from collections import defaultdict


class AnalyzerAgent:
    """Calculate transparent portfolio metrics from the supplied mock holdings."""

    def analyze(self, data: dict) -> dict:
        holdings = data["holdings"]
        if not holdings:
            raise ValueError("No holdings are available for analysis.")

        total_value = sum(item.current_value for item in holdings)
        total_cost = sum(item.cost_value for item in holdings)
        if total_value <= 0:
            raise ValueError("Portfolio value must be positive.")

        allocation_values: dict[str, float] = defaultdict(float)
        for item in holdings:
            allocation_values[item.asset_class] += item.current_value
        allocation = {
            asset: round(value / total_value * 100, 2)
            for asset, value in allocation_values.items()
        }
        concentrations = sorted(
            ((item.symbol, round(item.current_value / total_value * 100, 2)) for item in holdings),
            key=lambda pair: pair[1], reverse=True,
        )
        pnl = round(total_value - total_cost, 2)
        profile = data["customer"]
        observations = [f"Portfolio value is ${total_value:,.2f}.", f"Unrealized gain/loss is ${pnl:,.2f}."]
        if concentrations[0][1] >= 35:
            observations.append(f"{concentrations[0][0]} is {concentrations[0][1]:.1f}% of the portfolio, indicating concentration risk.")
        if allocation.get("Equity", 0) >= 80 and profile.risk_tolerance != "aggressive":
            observations.append("Equity exposure is high relative to the stated risk tolerance; consider a professional review.")

        return {
            "total_value": round(total_value, 2),
            "total_cost": round(total_cost, 2),
            "unrealized_pnl": pnl,
            "asset_allocation_pct": allocation,
            "top_concentrations_pct": concentrations[:3],
            "observations": observations,
            "market_context": data["market_context"],
        }
