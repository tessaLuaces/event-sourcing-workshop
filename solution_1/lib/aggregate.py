from abc import ABC, abstractmethod

from .event import Event


class Aggregate(ABC):
    """
    Base class for aggregates.

    The apply method is used to mutate the state of the aggregate based on an event. Should be implemented by subclasses.
    Contains a list of pending events that have been applied but not persisted.

    Class methods:
    - publish_event: Apply an event to the aggregate's state and add it to pending events.
    - get_pending_events: Return and clear the list of pending events.
    - apply: Abstract method to apply an event to the aggregate's state.
    """

    def __init__(self) -> None:
        self._pending_events: list[Event] = []

    def publish_event(self, event: Event) -> None:
        """Apply an event to the aggregate's state and add it to pending events."""
        self.apply(event)
        self._pending_events.append(event)

    def get_pending_events(self) -> list[Event]:
        """Return and clear the list of pending events."""
        pending = list(self._pending_events)
        self._pending_events.clear()
        return pending

    @abstractmethod
    def apply(self, event: Event) -> None:
        """Apply an event to the aggregate's state."""
        pass
