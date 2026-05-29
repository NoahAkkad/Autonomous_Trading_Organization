"""Domain exceptions for organization service."""

from .agent_already_exists import AgentAlreadyExists
from .department_already_exists import DepartmentAlreadyExists
from .invalid_rank import InvalidRank
from .invalid_relationship import InvalidRelationship
from .organization_already_exists import OrganizationAlreadyExists

__all__ = [
    "AgentAlreadyExists",
    "DepartmentAlreadyExists",
    "InvalidRank",
    "InvalidRelationship",
    "OrganizationAlreadyExists",
]
