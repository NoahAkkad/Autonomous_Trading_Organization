"""Agent command request models."""

from typing import Literal, NewType

from .base_command import OrganizationCommand

AgentId = NewType("AgentId", str)
DepartmentId = NewType("DepartmentId", str)
RankId = NewType("RankId", str)
RoleId = NewType("RoleId", str)


class CreateAgentCommand(OrganizationCommand):
    command_type: Literal["agent.create"] = "agent.create"
    agent_id: AgentId
    department_id: DepartmentId
    agent_name: str
    role_id: RoleId
    rank_id: RankId
    authority_level: int


class UpdateAgentCommand(OrganizationCommand):
    command_type: Literal["agent.update"] = "agent.update"
    agent_id: AgentId
    department_id: DepartmentId | None = None
    agent_name: str | None = None
    role_id: RoleId | None = None
    rank_id: RankId | None = None
    authority_level: int | None = None
    status: str | None = None


class ArchiveAgentCommand(OrganizationCommand):
    command_type: Literal["agent.archive"] = "agent.archive"
    agent_id: AgentId
