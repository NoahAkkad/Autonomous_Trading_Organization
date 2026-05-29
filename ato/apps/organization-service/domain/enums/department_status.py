"""Department lifecycle states."""

from enum import StrEnum


class DepartmentStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"
