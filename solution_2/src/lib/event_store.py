from .event import Event


class EventStore:
    def __init__(self):
        self._streams: dict[str, list[Event]] = {}

    def append(self, aggregate_id: str, event: Event) -> Event:
        if aggregate_id not in self._streams:
            self._streams[aggregate_id] = []
        self._streams[aggregate_id].append(event)
        return event

    def get_events(self, aggregate_id: str) -> list[Event]:
        return self._streams.get(aggregate_id, [])

    def get_all_events(self) -> list[Event]:
        all_events = []
        for events in self._streams.values():
            all_events.extend(events)
        return sorted(all_events, key=lambda e: e.timestamp)
