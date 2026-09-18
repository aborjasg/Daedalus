from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True)
class User:
    user_id: UUID | None = None
    tenant_id: UUID | None = None
    email: str = ""
    password_hash: str = ""
    status: str = ""
    last_login: datetime | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by: UUID | None = None
    updated_by: UUID | None = None
