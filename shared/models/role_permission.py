from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class RolePermission:
    role_id: UUID | None = None
    permission_id: UUID | None = None
