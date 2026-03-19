from .event import Event


class EventStore:
    """
    Simple in memory event store.

    It allows adding and retrieving events.
    """

    def __init__(self) -> None:
        self._events: list[Event] = []

    def append(self, event: Event) -> Event:
        """Append an event to the store."""

        self._events.append(event)
        return event

    def get_events(self) -> list[Event]:
        """Get all events from the store."""

        return self._events
