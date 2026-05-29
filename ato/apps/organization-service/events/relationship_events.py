"""Relationship event models."""

from typing import Literal, NewType

from .base_event import AggregateType, BaseEvent

AgentId = NewType("AgentId", str)
RelationshipId = NewType("RelationshipId", str)


class RelationshipCreated(BaseEvent):
    event_type: Literal["relationship.created"] = "relationship.created"
    aggregate_type: AggregateType = AggregateType("relationship")
    relationship_id: RelationshipId
    source_agent_id: AgentId
    target_agent_id: AgentId
    relationship_type: str


class RelationshipRemoved(BaseEvent):
    event_type: Literal["relationship.removed"] = "relationship.removed"
    aggregate_type: AggregateType = AggregateType("relationship")
    relationship_id: RelationshipId
