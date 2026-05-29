"""Permission command request models."""

from typing import Literal, NewType

from .base_command import OrganizationCommand

AgentId = NewType("AgentId", str)
PermissionId = NewType("PermissionId", str)


class GrantPermissionCommand(OrganizationCommand):
    command_type: Literal["permission.grant"] = "permission.grant"
    agent_id: AgentId
    permission_id: PermissionId


class RevokePermissionCommand(OrganizationCommand):
    command_type: Literal["permission.revoke"] = "permission.revoke"
    agent_id: AgentId
    permission_id: PermissionId
