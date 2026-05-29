"""Agent event models."""

from typing import Literal, NewType

from .base_event import AggregateType, BaseEvent

AgentId = NewType("AgentId", str)
DepartmentId = NewType("DepartmentId", str)
RankId = NewType("RankId", str)
RoleId = NewType("RoleId", str)


class AgentCreated(BaseEvent):
    event_type: Literal["agent.created"] = "agent.created"
    aggregate_type: AggregateType = AggregateType("agent")
    agent_id: AgentId
    department_id: DepartmentId
    agent_name: str
    role_id: RoleId
    rank_id: RankId
    authority_level: int = 0
    status: str


class AgentUpdated(BaseEvent):
    event_type: Literal["agent.updated"] = "agent.updated"
    aggregate_type: AggregateType = AggregateType("agent")
    agent_id: AgentId
    department_id: DepartmentId | None = None
    agent_name: str | None = None
    role_id: RoleId | None = None
    rank_id: RankId | None = None
    authority_level: int | None = None
    status: str | None = None


class AgentArchived(BaseEvent):
    event_type: Literal["agent.archived"] = "agent.archived"
    aggregate_type: AggregateType = AggregateType("agent")
    agent_id: AgentId
