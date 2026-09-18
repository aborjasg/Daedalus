from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID


@dataclass(slots=True)
class UsageMetric:
    metric_id: UUID | None = None
    tenant_id: UUID | None = None
    module_id: UUID | None = None
    metric_code: str = ""
    value: Decimal | None = None
    timestamp: datetime | None = None
