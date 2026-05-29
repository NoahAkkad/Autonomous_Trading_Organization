"""Relationship command request models."""

from typing import Literal, NewType

from .base_command import OrganizationCommand

AgentId = NewType("AgentId", str)
RelationshipId = NewType("RelationshipId", str)


class CreateRelationshipCommand(OrganizationCommand):
    command_type: Literal["relationship.create"] = "relationship.create"
    relationship_id: RelationshipId
    source_agent_id: AgentId
    target_agent_id: AgentId
    relationship_type: str


class RemoveRelationshipCommand(OrganizationCommand):
    command_type: Literal["relationship.remove"] = "relationship.remove"
    relationship_id: RelationshipId
