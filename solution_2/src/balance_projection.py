from typing import override
from .lib import Projection, Event


class BalanceProjection(Projection):
    def __init__(self):
        self.balances: dict[str, float] = {}

    @override
    def reset(self) -> None:
        self.balances.clear()

    @override
    def handle(self, event: Event) -> None:
        match event.name:
            case "account_opened":
                self.balances[event.aggregate_id] = 0.0
            case "money_deposited":
                self.balances[event.aggregate_id] += event.data["amount"]
            case "money_withdrawn":
                self.balances[event.aggregate_id] -= event.data["amount"]
            case _:
                raise ValueError(f"Unknown event type: {event.name}")