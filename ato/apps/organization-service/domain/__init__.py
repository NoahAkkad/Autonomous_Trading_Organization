"""Pure domain layer for the organization service."""

from .entities import Agent, Department, Organization, Permission, Rank, Relationship, Role
from .enums import AgentStatus, DepartmentStatus, OrganizationStatus, RelationshipType
from .exceptions import (
    AgentAlreadyExists,
    DepartmentAlreadyExists,
    InvalidRank,
    InvalidRelationship,
    OrganizationAlreadyExists,
)

__all__ = [
    "Agent",
    "AgentAlreadyExists",
    "AgentStatus",
    "Department",
    "DepartmentAlreadyExists",
    "DepartmentStatus",
    "InvalidRank",
    "InvalidRelationship",
    "Organization",
    "OrganizationAlreadyExists",
    "OrganizationStatus",
    "Permission",
    "Rank",
    "Relationship",
    "RelationshipType",
    "Role",
]
