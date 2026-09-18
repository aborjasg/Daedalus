from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class TenantModule:
    tenant_id: UUID | None = None
    module_id: UUID | None = None
    status: str = ""
    billing_plan_id: UUID | None = None
