"""Role domain entity."""

from dataclasses import dataclass

from ..value_objects import DomainName, RoleId
from ..value_objects.validation import require_present


@dataclass(frozen=True, slots=True, kw_only=True)
class Role:
    role_id: RoleId
    role_name: DomainName
    description: str

    def __post_init__(self) -> None:
        require_present(self.role_id, "role_id")
        require_present(self.role_name, "role_name")
