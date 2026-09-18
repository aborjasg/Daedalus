from dataclasses import dataclass
from datetime import datetime
from typing import Any
from uuid import UUID


@dataclass(slots=True)
class AuditLog:
    audit_id: UUID | None = None
    tenant_id: UUID | None = None
    user_id: UUID | None = None
    action: str = ""
    entity: str = ""
    entity_id: UUID | None = None
    timestamp: datetime | None = None
    metadata: dict[str, Any] | None = None
