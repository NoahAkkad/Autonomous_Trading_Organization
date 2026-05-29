"""FastAPI response schemas for organization-service management APIs."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ApiResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")


class CommandAcceptedResponse(ApiResponse):
    command_id: str
    command_type: str
    status: str


class OrganizationResponse(ApiResponse):
    organization_id: str
    organization_name: str
    short_name: str
    status: str
    constitution_version: str
    governance_version: str
    created_at: datetime
    updated_at: datetime
    department_count: int
    agent_count: int


class DepartmentResponse(ApiResponse):
    department_id: str
    organization_id: str
    department_name: str
    department_code: str
    status: str
    department_head_id: str | None
    agent_count: int
    created_at: datetime
    updated_at: datetime


class AgentResponse(ApiResponse):
    agent_id: str
    organization_id: str
    department_id: str
    agent_name: str
    role: str | None
    rank: str | None
    authority_level: int
    status: str
    version: int
    created_at: datetime
    updated_at: datetime


class RelationshipResponse(ApiResponse):
    relationship_id: str
    source_agent_id: str
    target_agent_id: str
    relationship_type: str
    status: str
    created_at: datetime
