from abc import ABC

class Projection(ABC):
    """Base class for projections.
    Projections are read models that can be rebuilt by replaying events.
    They have a reset method to clear their state and a handle method to process individual events.
    The rebuild method can be used to reset and replay a sequence of events to reconstruct the projection's state.
    Both reset and handle will be implemented by subclasses.
    """
