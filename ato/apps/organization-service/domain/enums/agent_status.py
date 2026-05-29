"""Agent lifecycle states."""

from enum import StrEnum


class AgentStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    RETIRED = "retired"
