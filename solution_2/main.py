from src.lib import EventStore
from src.bank_account import BankAccount
from src.balance_projection import BalanceProjection

def main():
    # 1. Initialize Event Store
    event_store = EventStore()

    alice_aggregate_id = "alice-1"
    alice_account = BankAccount(alice_aggregate_id)
    alice_account.open("Alice")

    bob_aggregate_id = "bob-1"
    bob_account = BankAccount(bob_aggregate_id)
    bob_account.open("Bob")

    # 2. Perform Commands
    bob_account.deposit(200.0)
    bob_account.deposit(100.0)
    alice_account.deposit(100.0)
    bob_account.deposit(100.0)
    alice_account.withdraw(30.0)
    bob_account.deposit(200.0)
    bob_account.deposit(100.0)
    bob_account.withdraw(50.0)
    bob_account.withdraw(50.0)

    # 3. Persist events (Simulating saving to a database)
    print("--- Persisting Events ---")
    for event in alice_account.get_pending_events():
        event_store.append(alice_aggregate_id, event)

    for event in bob_account.get_pending_events():
        event_store.append(bob_aggregate_id, event)
    print("Events persisted to EventStore.\n")

    # 4. Rehydration Demonstration - reconstruct state purely from the event store
    print("--- Rehydration Demo ---")
    alice_rehydrated = BankAccount(alice_aggregate_id)
    print(f"New instance (before rehydration) balance: {alice_rehydrated._balance}")

    # Load history from store
    alice_history = event_store.get_events(alice_aggregate_id)
    alice_rehydrated.load_from_history(alice_history)

    print(f"Rehydrated instance balance: {alice_rehydrated._balance}")

    assert alice_account._balance == alice_rehydrated._balance
    print("Success: Rehydrated state matches original state.")
    print("------------------------\n")

    # 5. Projection Demonstration - should be built from the persistent store, not live objects
    print("--- Projection Demo ---")
    projection = BalanceProjection()

    # Retrieve ALL events from the store to build a global view
    all_events = event_store.get_all_events()
    for event in all_events:
        projection.handle(event)

    print(f"Total balances (from EventStore): {projection.balances}")
    print(f"Bob balance: ${projection.balances[bob_aggregate_id]}")
    print(f"Alice balance: ${projection.balances[alice_aggregate_id]}")
    print("-----------------------")


if __name__ == "__main__":
    main()
