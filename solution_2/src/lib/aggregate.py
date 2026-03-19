from abc import ABC, abstractmethod
from typing import Any

from .event import Event


class Aggregate(ABC):
    def __init__(self, aggregate_id: str):
        self.id = aggregate_id
        self._pending_events = []

    def publish_event(self, type: str, payload: dict[str, Any]) -> None:
        event = Event(name=type, data=payload, aggregate_id=self.id)
        self._apply(event)
        self._pending_events.append(event)

    def get_pending_events(self) -> list[Event]:
        pending = list(self._pending_events)
        self._pending_events.clear()
        return pending

    def load_from_history(self, events: list[Event]) -> None:
        for event in events:
            self._apply(event)
        self._pending_events.clear()

    @abstractmethod
    def _apply(self, event: Event):
        pass
