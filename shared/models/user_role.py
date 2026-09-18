from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class UserRole:
    user_id: UUID | None = None
    role_id: UUID | None = None
