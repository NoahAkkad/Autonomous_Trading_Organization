"""Organization command request models."""

from typing import Literal

from .base_command import CommandType, OrganizationCommand


class CreateOrganizationCommand(OrganizationCommand):
    command_type: Literal["organization.create"] = "organization.create"
    organization_name: str
    short_name: str
    constitution_version: str
    governance_version: str


class UpdateOrganizationCommand(OrganizationCommand):
    command_type: Literal["organization.update"] = "organization.update"
    organization_name: str | None = None
    short_name: str | None = None
    status: str | None = None
    constitution_version: str | None = None
    governance_version: str | None = None


class ArchiveOrganizationCommand(OrganizationCommand):
    command_type: Literal["organization.archive"] = "organization.archive"
