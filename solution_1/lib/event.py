from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Event:
    """
    Representation of a domain event.
    An event is a fact that happened in the past, relevant to the domain. It's immutable.
    """

    id: UUID = field(default_factory=uuid4)
    name: str = field(default="")
    data: dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
