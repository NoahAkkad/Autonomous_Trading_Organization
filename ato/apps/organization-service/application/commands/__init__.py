"""Command request models for the organization service."""

from .agent_commands import ArchiveAgentCommand, CreateAgentCommand, UpdateAgentCommand
from .base_command import (
    ActorId,
    CommandId,
    CommandMetadata,
    CommandType,
    OrganizationCommand,
    OrganizationId,
)
from .department_commands import (
    ArchiveDepartmentCommand,
    CreateDepartmentCommand,
    UpdateDepartmentCommand,
)
from .organization_commands import (
    ArchiveOrganizationCommand,
    CreateOrganizationCommand,
    UpdateOrganizationCommand,
)
from .permission_commands import GrantPermissionCommand, RevokePermissionCommand
from .rank_commands import DemoteAgentCommand, PromoteAgentCommand
from .relationship_commands import CreateRelationshipCommand, RemoveRelationshipCommand
from .role_commands import AssignRoleCommand, RevokeRoleCommand

__all__ = [
    "ActorId",
    "ArchiveAgentCommand",
    "ArchiveDepartmentCommand",
    "ArchiveOrganizationCommand",
    "AssignRoleCommand",
    "CommandId",
    "CommandMetadata",
    "CommandType",
    "CreateAgentCommand",
    "CreateDepartmentCommand",
    "CreateOrganizationCommand",
    "CreateRelationshipCommand",
    "DemoteAgentCommand",
    "GrantPermissionCommand",
    "OrganizationCommand",
    "OrganizationId",
    "PromoteAgentCommand",
    "RemoveRelationshipCommand",
    "RevokePermissionCommand",
    "RevokeRoleCommand",
    "UpdateAgentCommand",
    "UpdateDepartmentCommand",
    "UpdateOrganizationCommand",
]
