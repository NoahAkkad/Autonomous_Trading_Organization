"""Rank command request models."""

from typing import Literal, NewType

from .base_command import OrganizationCommand

AgentId = NewType("AgentId", str)
RankId = NewType("RankId", str)


class PromoteAgentCommand(OrganizationCommand):
    command_type: Literal["rank.promote_agent"] = "rank.promote_agent"
    agent_id: AgentId
    target_rank_id: RankId


class DemoteAgentCommand(OrganizationCommand):
    command_type: Literal["rank.demote_agent"] = "rank.demote_agent"
    agent_id: AgentId
    target_rank_id: RankId
