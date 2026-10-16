from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class CustomerProfile:
    customer_id: str
    name: str
    risk_tolerance: str
    investment_horizon_years: int
    primary_goal: str
    notes: str = ""


@dataclass
class Holding:
    symbol: str
    asset_name: str
    asset_class: str
    quantity: float
    cost_basis: float
    current_price: float

    @property
    def current_value(self) -> float:
        return round(self.quantity * self.current_price, 2)

    @property
    def cost_value(self) -> float:
        return round(self.quantity * self.cost_basis, 2)

    @property
    def unrealized_gain_loss(self) -> float:
        return round(self.current_value - self.cost_value, 2)


@dataclass
class AdvisorSummary:
    customer_id: str
    timestamp: str
    executive_summary: str
    facts: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)
    human_review_required: bool = True
    human_signoff_completed: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
