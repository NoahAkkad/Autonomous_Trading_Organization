"""Role event models."""

from typing import Literal, NewType

from .base_event import AggregateType, BaseEvent

AgentId = NewType("AgentId", str)
RoleId = NewType("RoleId", str)


class RoleAssigned(BaseEvent):
    event_type: Literal["role.assigned"] = "role.assigned"
    aggregate_type: AggregateType = AggregateType("agent")
    agent_id: AgentId
    role_id: RoleId


class RoleRevoked(BaseEvent):
    event_type: Literal["role.revoked"] = "role.revoked"
    aggregate_type: AggregateType = AggregateType("agent")
    agent_id: AgentId
    role_id: RoleId
