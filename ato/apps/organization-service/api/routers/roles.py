"""Role management routes."""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from api.dependencies import CommandDispatcher, get_command_dispatcher
from api.schemas.requests import AssignRoleRequest, RevokeRoleRequest
from api.schemas.responses import CommandAcceptedResponse
from application.commands import AssignRoleCommand, RevokeRoleCommand

router = APIRouter(prefix="/roles", tags=["roles"])


@router.post("/assign", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def assign_role(
    request: AssignRoleRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = AssignRoleCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        agent_id=request.agent_id,
        role_id=request.role_id,
    )
    return dispatcher.dispatch(command)


@router.post("/revoke", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def revoke_role(
    request: RevokeRoleRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = RevokeRoleCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        agent_id=request.agent_id,
        role_id=request.role_id,
    )
    return dispatcher.dispatch(command)
