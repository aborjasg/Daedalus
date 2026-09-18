from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class Integration:
    integration_id: UUID | None = None
    code: str = ""
    name: str = ""
