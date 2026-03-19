from .lib import Aggregate, Event
from typing import override


class BankAccount(Aggregate):
    def __init__(self, aggregate_id: str):
        super().__init__(aggregate_id)
        self._owner: str = ""
        self._balance: float = 0.0
        self._open: bool = False

    # commands
    def open(self, owner: str) -> None:
        if self._open:
            raise Exception("Account already open")
        self.publish_event(type="account_opened", payload={"owner": owner})

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.publish_event(type="money_deposited", payload={"amount": amount})

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds: balance is {self._balance}")
        self.publish_event(type="money_withdrawn", payload={"amount": amount})

    # state reconstruction
    @override
    def _apply(self, event: Event):
        match event.name:
            case "account_opened":
                self._owner = event.data["owner"]
                self._balance = 0.0
                self._open = True
            case "money_deposited":
                self._balance += event.data["amount"]
            case "money_withdrawn":
                self._balance -= event.data["amount"]
            case _:
                raise ValueError(f"Unknown event type: {event.name}")
