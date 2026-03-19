from abc import ABC, abstractmethod

from .event import Event


class Projection(ABC):
    """Base class for projections.
    Projections are read models that can be rebuilt by replaying events.
    They have a reset method to clear their state and a handle method to process individual events.
    Both reset and handle will be implemented by subclasses.
    """

    @abstractmethod
    def reset(self) -> None:
        """Reset the projection to an empty state."""
        pass

    @abstractmethod
    def handle(self, event: Event) -> None:
        """Handle an event to update the projection's state."""
        pass
