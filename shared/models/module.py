from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class Module:
    module_id: UUID | None = None
    code: str = ""
    name: str = ""
    is_system_module: bool = False
    status: str = ""
    created_at: datetime | None = None
