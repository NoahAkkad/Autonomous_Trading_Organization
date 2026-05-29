"""Permission event models."""

from typing import Literal, NewType

from .base_event import AggregateType, BaseEvent

AgentId = NewType("AgentId", str)
PermissionId = NewType("PermissionId", str)


class PermissionGranted(BaseEvent):
    event_type: Literal["permission.granted"] = "permission.granted"
    aggregate_type: AggregateType = AggregateType("agent")
    agent_id: AgentId
    permission_id: PermissionId


class PermissionRevoked(BaseEvent):
    event_type: Literal["permission.revoked"] = "permission.revoked"
    aggregate_type: AggregateType = AggregateType("agent")
    agent_id: AgentId
    permission_id: PermissionId
