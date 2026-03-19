## Exercise 1 — Core Event Sourcing Primitives

**Goal:** Implement the foundational building blocks and wire up a working bank account.

Work in `lib/` and `main.py`. You need to implement:

- **`Event`** (`lib/event.py`): A simple immutable domain event with an `id`, `name`, `data` payload, and `timestamp`.
- **`EventStore`** (`lib/event_store.py`): An in-memory store that can append and retrieve events.
- **`Aggregate`** (`lib/aggregate.py`): The base class that tracks pending (uncommitted) events. It exposes `publish_event` to raise an event and apply it to the aggregate's state, and `get_pending_events` to flush them.
- **`Projection`** (`lib/projection.py`): A read model base class with a `reset` method and a `handle` method that processes one event at a time.

Once the library is in place, implement a `BankAccount` aggregate and a `BalanceProjection` in `main.py`:

- `BankAccount` should support `open(owner)`, `deposit(amount)`, and `withdraw(amount)` commands, each enforcing basic business rules and raising the appropriate event.
- `BalanceProjection` should rebuild the balance for each owner by replaying events.

See `solution_1/` for the reference implementation.
