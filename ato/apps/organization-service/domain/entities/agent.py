"""Agent domain entity."""

from dataclasses import dataclass

from ..enums import AgentStatus
from ..value_objects import AgentId, DepartmentId, DomainName, OrganizationId, RankId, RoleId
from ..value_objects.validation import require_present


@dataclass(frozen=True, slots=True, kw_only=True)
class Agent:
    agent_id: AgentId
    organization_id: OrganizationId
    department_id: DepartmentId
    agent_name: DomainName
    role_id: RoleId
    rank_id: RankId
    authority_level: int
    version: int
    status: AgentStatus

    def __post_init__(self) -> None:
        require_present(self.agent_id, "agent_id")
        require_present(self.organization_id, "organization_id")
        require_present(self.department_id, "department_id")
        require_present(self.agent_name, "agent_name")
        require_present(self.role_id, "role_id")
        require_present(self.rank_id, "rank_id")
        if self.authority_level < 0:
            raise ValueError("authority_level must be non-negative")
        if self.version < 1:
            raise ValueError("version must be greater than zero")
