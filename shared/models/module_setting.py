from dataclasses import dataclass
from datetime import datetime
from typing import Any
from uuid import UUID


@dataclass(slots=True)
class ModuleSetting:
    setting_id: UUID | None = None
    tenant_id: UUID | None = None
    module_id: UUID | None = None
    key: str = ""
    value: dict[str, Any] | None = None
    updated_at: datetime | None = None
    updated_by: UUID | None = None
