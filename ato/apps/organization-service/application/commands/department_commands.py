"""Department command request models."""

from typing import Literal, NewType

from .base_command import OrganizationCommand

DepartmentId = NewType("DepartmentId", str)


class CreateDepartmentCommand(OrganizationCommand):
    command_type: Literal["department.create"] = "department.create"
    department_id: DepartmentId
    department_name: str
    department_code: str


class UpdateDepartmentCommand(OrganizationCommand):
    command_type: Literal["department.update"] = "department.update"
    department_id: DepartmentId
    department_name: str | None = None
    department_code: str | None = None
    status: str | None = None


class ArchiveDepartmentCommand(OrganizationCommand):
    command_type: Literal["department.archive"] = "department.archive"
    department_id: DepartmentId
