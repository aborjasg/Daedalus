from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class TenantIntegration:
    tenant_integration_id: UUID | None = None
    tenant_id: UUID | None = None
    integration_id: UUID | None = None
    status: str = ""
    created_at: datetime | None = None
