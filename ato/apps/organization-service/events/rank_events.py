"""Rank event models."""

from typing import Literal, NewType

from .base_event import AggregateType, BaseEvent

AgentId = NewType("AgentId", str)
RankId = NewType("RankId", str)


class AgentPromoted(BaseEvent):
    event_type: Literal["agent.promoted"] = "agent.promoted"
    aggregate_type: AggregateType = AggregateType("agent")
    agent_id: AgentId
    previous_rank_id: RankId
    new_rank_id: RankId


class AgentDemoted(BaseEvent):
    event_type: Literal["agent.demoted"] = "agent.demoted"
    aggregate_type: AggregateType = AggregateType("agent")
    agent_id: AgentId
    previous_rank_id: RankId
    new_rank_id: RankId
