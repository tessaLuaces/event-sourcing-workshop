from abc import ABC

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