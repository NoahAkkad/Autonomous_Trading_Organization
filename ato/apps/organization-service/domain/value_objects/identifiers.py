"""Strongly typed identifiers for organization domain entities."""

from typing import NewType

AgentId = NewType("AgentId", str)
DepartmentId = NewType("DepartmentId", str)
OrganizationId = NewType("OrganizationId", str)
PermissionId = NewType("PermissionId", str)
RankId = NewType("RankId", str)
RelationshipId = NewType("RelationshipId", str)
RoleId = NewType("RoleId", str)
