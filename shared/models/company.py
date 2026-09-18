from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class Company:
    company_id: UUID | None = None
    tenant_id: UUID | None = None
    legal_name: str = ""
    domain: str = ""
    timezone: str = ""
    created_at: datetime | None = None
