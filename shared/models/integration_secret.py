from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class IntegrationSecret:
    secret_id: UUID | None = None
    tenant_integration_id: UUID | None = None
    key: str = ""
    value_reference: str = ""
