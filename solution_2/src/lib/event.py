from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Event:
    id: UUID = field(default_factory=uuid4)
    aggregate_id: str = field(default="")
    name: str = field(default="")
    data: dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
