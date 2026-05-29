"""Role command request models."""

from typing import Literal, NewType

from .base_command import OrganizationCommand

AgentId = NewType("AgentId", str)
RoleId = NewType("RoleId", str)


class AssignRoleCommand(OrganizationCommand):
    command_type: Literal["role.assign"] = "role.assign"
    agent_id: AgentId
    role_id: RoleId


class RevokeRoleCommand(OrganizationCommand):
    command_type: Literal["role.revoke"] = "role.revoke"
    agent_id: AgentId
    role_id: RoleId
