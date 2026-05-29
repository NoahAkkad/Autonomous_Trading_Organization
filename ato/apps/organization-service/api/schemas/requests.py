"""FastAPI request schemas for organization-service management APIs."""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

JsonObject = dict[str, Any]


class ApiRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)


class CommandRequest(ApiRequest):
    actor_id: str
    reason: str
    metadata: JsonObject = Field(default_factory=dict)


class OrganizationCommandRequest(CommandRequest):
    organization_id: str


class CreateOrganizationRequest(OrganizationCommandRequest):
    organization_name: str
    short_name: str
    constitution_version: str
    governance_version: str


class UpdateOrganizationRequest(CommandRequest):
    organization_name: str | None = None
    short_name: str | None = None
    status: str | None = None
    constitution_version: str | None = None
    governance_version: str | None = None


class ArchiveOrganizationRequest(CommandRequest):
    pass


class CreateDepartmentRequest(OrganizationCommandRequest):
    department_id: str
    department_name: str
    department_code: str


class UpdateDepartmentRequest(CommandRequest):
    organization_id: str
    department_name: str | None = None
    department_code: str | None = None
    status: str | None = None


class ArchiveDepartmentRequest(CommandRequest):
    organization_id: str


class CreateAgentRequest(OrganizationCommandRequest):
    agent_id: str
    department_id: str
    agent_name: str
    role_id: str
    rank_id: str
    authority_level: int


class UpdateAgentRequest(CommandRequest):
    organization_id: str
    department_id: str | None = None
    agent_name: str | None = None
    role_id: str | None = None
    rank_id: str | None = None
    authority_level: int | None = None
    status: str | None = None


class ArchiveAgentRequest(CommandRequest):
    organization_id: str


class CreateRelationshipRequest(OrganizationCommandRequest):
    relationship_id: str
    source_agent_id: str
    target_agent_id: str
    relationship_type: str


class RemoveRelationshipRequest(CommandRequest):
    organization_id: str


class AssignRoleRequest(OrganizationCommandRequest):
    agent_id: str
    role_id: str


class RevokeRoleRequest(OrganizationCommandRequest):
    agent_id: str
    role_id: str


class PromoteAgentRequest(OrganizationCommandRequest):
    agent_id: str
    target_rank_id: str


class DemoteAgentRequest(OrganizationCommandRequest):
    agent_id: str
    target_rank_id: str


class GrantPermissionRequest(OrganizationCommandRequest):
    agent_id: str
    permission_id: str


class RevokePermissionRequest(OrganizationCommandRequest):
    agent_id: str
    permission_id: str
