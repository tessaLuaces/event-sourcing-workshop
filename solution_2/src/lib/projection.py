from abc import ABC, abstractmethod

from .event import Event


class Projection(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def handle(self, event: Event) -> None:
        pass
