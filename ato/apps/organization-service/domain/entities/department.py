"""Department domain entity."""

from dataclasses import dataclass

from ..enums import DepartmentStatus
from ..value_objects import DepartmentCode, DepartmentId, DomainName, OrganizationId
from ..value_objects.validation import require_present


@dataclass(frozen=True, slots=True, kw_only=True)
class Department:
    department_id: DepartmentId
    organization_id: OrganizationId
    department_name: DomainName
    department_code: DepartmentCode
    status: DepartmentStatus

    def __post_init__(self) -> None:
        require_present(self.department_id, "department_id")
        require_present(self.organization_id, "organization_id")
        require_present(self.department_name, "department_name")
        require_present(self.department_code, "department_code")
