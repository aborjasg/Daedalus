from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass(slots=True)
class TenantSubscription:
    subscription_id: UUID | None = None
    tenant_id: UUID | None = None
    plan_id: UUID | None = None
    status: str = ""
    renewal_date: date | None = None
