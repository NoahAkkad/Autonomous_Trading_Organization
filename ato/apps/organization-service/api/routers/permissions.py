"""Permission management routes."""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from api.dependencies import CommandDispatcher, get_command_dispatcher
from api.schemas.requests import GrantPermissionRequest, RevokePermissionRequest
from api.schemas.responses import CommandAcceptedResponse
from application.commands import GrantPermissionCommand, RevokePermissionCommand

router = APIRouter(prefix="/permissions", tags=["permissions"])


@router.post("/grant", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def grant_permission(
    request: GrantPermissionRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = GrantPermissionCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        agent_id=request.agent_id,
        permission_id=request.permission_id,
    )
    return dispatcher.dispatch(command)


@router.post("/revoke", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def revoke_permission(
    request: RevokePermissionRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = RevokePermissionCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        agent_id=request.agent_id,
        permission_id=request.permission_id,
    )
    return dispatcher.dispatch(command)
