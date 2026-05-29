"""Organization domain entity."""

from dataclasses import dataclass

from ..enums import OrganizationStatus
from ..value_objects import DomainName, OrganizationId
from ..value_objects.validation import require_present


@dataclass(frozen=True, slots=True, kw_only=True)
class Organization:
    organization_id: OrganizationId
    organization_name: DomainName
    short_name: DomainName
    status: OrganizationStatus
    constitution_version: str
    governance_version: str

    def __post_init__(self) -> None:
        require_present(self.organization_id, "organization_id")
        require_present(self.organization_name, "organization_name")
        require_present(self.short_name, "short_name")
        require_present(self.constitution_version, "constitution_version")
        require_present(self.governance_version, "governance_version")
