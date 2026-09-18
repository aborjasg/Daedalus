from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class Permission:
    permission_id: UUID | None = None
    code: str = ""
    description: str = ""
