## Exercise 2 — Aggregate Identity & Event Streams

**Goal:** Extend your solution with proper aggregate identity, per-stream event storage, and rehydration from history.

Build on top of your Exercise 1 code. The changes span both the library and the domain classes:

- **`Event`** (`lib/event.py`): Add an `aggregate_id` field so each event is linked to the aggregate that produced it.
- **`Aggregate`** (`lib/aggregate.py`): The constructor now accepts an `aggregate_id`. Add a `load_from_history(events)` method that replays a list of events to reconstruct state without adding them to the pending list.
- **`EventStore`** (`lib/event_store.py`): Store events in per-aggregate streams. Add `get_events(aggregate_id)` to retrieve one aggregate's history, and `get_all_events()` to retrieve every event across all streams (sorted by timestamp).
- **`BankAccount`** (`src/bank_account.py`): Move out of `main.py` into its own module. The constructor now takes an `aggregate_id` and passes it to the base `Aggregate`.
- **`BalanceProjection`** (`src/balance_projection.py`): Move out of `main.py` into its own module. Balances are now keyed by `aggregate_id` instead of owner name, using `event.aggregate_id`.

In `main.py`, demonstrate:
1. Creating accounts with explicit aggregate IDs.
2. Persisting pending events to the store stream-by-stream.
3. **Rehydration** — creating a fresh aggregate instance and calling `load_from_history` with events fetched from the store.
4. **Projection** — building a global balance view by iterating over `get_all_events()`.

See `solution_2/` for the reference implementation.