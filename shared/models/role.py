from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class Role:
    role_id: UUID | None = None
    tenant_id: UUID | None = None
    name: str = ""
    description: str = ""
    status: str = ""
    created_at: datetime | None = None
    updated_at: datetime | None = None
