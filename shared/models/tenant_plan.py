from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID


@dataclass(slots=True)
class TenantPlan:
    plan_id: UUID | None = None
    code: str = ""
    name: str = ""
    price_monthly: Decimal | None = None
    price_yearly: Decimal | None = None
    status: str = ""
    created_at: datetime | None = None
