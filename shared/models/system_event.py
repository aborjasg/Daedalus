from dataclasses import dataclass
from datetime import datetime
from typing import Any
from uuid import UUID


@dataclass(slots=True)
class SystemEvent:
    event_id: UUID | None = None
    tenant_id: UUID | None = None
    module_id: UUID | None = None
    event_type: str = ""
    payload: dict[str, Any] | None = None
    created_at: datetime | None = None
