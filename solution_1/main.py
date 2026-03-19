from typing import override

from lib import Aggregate, Event, Projection


class BankAccount(Aggregate):
    def __init__(self) -> None:
        super().__init__()
        self._owner: str = ""
        self._balance: float = 0.0
        self._is_open: bool = False

    # Commands
    # Commands enforce business rules and raise events. They should not contain any state mutation logic.
    def open(self, owner: str) -> None:
        if self._is_open:
            raise RuntimeError("Account is already open")
        self.publish_event(Event(name="AccountOpened", data={"owner": owner}))

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.publish_event(
            Event(name="MoneyDeposited", data={"owner": self._owner, "amount": amount})
        )

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds: balance is {self._balance}")
        self.publish_event(
            Event(name="MoneyWithdrawn", data={"owner": self._owner, "amount": amount})
        )

    # State reconstruction
    # The apply method is responsible for mutating the aggregate's state based on an event.
    # It should not contain any business logic or validation.
    @override
    def apply(self, event: Event) -> None:
        match event.name:
            case "AccountOpened":
                self._owner = event.data["owner"]
                self._balance = 0.0
                self._is_open = True
            case "MoneyDeposited":
                self._balance += event.data["amount"]
            case "MoneyWithdrawn":
                self._balance -= event.data["amount"]
            case _:
                raise ValueError(f"Unknown event type: {event.name}")


class BalanceProjection(Projection):
    def __init__(self) -> None:
        self.balances: dict[str, float] = {}

    @override
    def reset(self) -> None:
        self.balances.clear()

    @override
    def handle(self, event: Event) -> None:
        match event.name:
            case "AccountOpened":
                owner: str = event.data["owner"]
                self.balances[owner] = 0.0
            case "MoneyDeposited":
                owner: str = event.data["owner"]
                amount: float = event.data["amount"]
                self.balances[owner] += amount
            case "MoneyWithdrawn":
                owner: str = event.data["owner"]
                amount: float = event.data["amount"]
                self.balances[owner] -= amount
            case _:
                pass


def main():
    bank_account = BankAccount()
    bank_account.open("Alice")
    bank_account.deposit(100.0)
    bank_account.deposit(50.0)
    bank_account.withdraw(30.0)

    projection = BalanceProjection()
    for event in bank_account.get_pending_events():
        projection.handle(event)

    print(projection.balances)


if __name__ == "__main__":
    main()
