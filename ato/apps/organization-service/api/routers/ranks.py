"""Rank management routes."""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from api.dependencies import CommandDispatcher, get_command_dispatcher
from api.schemas.requests import DemoteAgentRequest, PromoteAgentRequest
from api.schemas.responses import CommandAcceptedResponse
from application.commands import DemoteAgentCommand, PromoteAgentCommand

router = APIRouter(prefix="/ranks", tags=["ranks"])


@router.post("/promote", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def promote_agent(
    request: PromoteAgentRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = PromoteAgentCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        agent_id=request.agent_id,
        target_rank_id=request.target_rank_id,
    )
    return dispatcher.dispatch(command)


@router.post("/demote", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def demote_agent(
    request: DemoteAgentRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = DemoteAgentCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        agent_id=request.agent_id,
        target_rank_id=request.target_rank_id,
    )
    return dispatcher.dispatch(command)
