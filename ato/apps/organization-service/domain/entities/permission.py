"""Permission domain entity."""

from dataclasses import dataclass

from ..value_objects import DomainName, PermissionId
from ..value_objects.validation import require_present


@dataclass(frozen=True, slots=True, kw_only=True)
class Permission:
    permission_id: PermissionId
    permission_name: DomainName

    def __post_init__(self) -> None:
        require_present(self.permission_id, "permission_id")
        require_present(self.permission_name, "permission_name")
