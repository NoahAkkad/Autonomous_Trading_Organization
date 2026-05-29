"""Relationship management routes."""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from api.dependencies import CommandDispatcher, OrganizationQueryService, get_command_dispatcher, get_query_service
from api.schemas.requests import CreateRelationshipRequest, RemoveRelationshipRequest
from api.schemas.responses import CommandAcceptedResponse, RelationshipResponse
from application.commands import CreateRelationshipCommand, RemoveRelationshipCommand

router = APIRouter(prefix="/relationships", tags=["relationships"])


@router.post("", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def create_relationship(
    request: CreateRelationshipRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = CreateRelationshipCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        relationship_id=request.relationship_id,
        source_agent_id=request.source_agent_id,
        target_agent_id=request.target_agent_id,
        relationship_type=request.relationship_type,
    )
    return dispatcher.dispatch(command)


@router.delete("/{relationship_id}", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def remove_relationship(
    relationship_id: str,
    request: RemoveRelationshipRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = RemoveRelationshipCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        relationship_id=relationship_id,
    )
    return dispatcher.dispatch(command)


@router.get("", response_model=list[RelationshipResponse], status_code=status.HTTP_200_OK)
def list_relationships(
    query_service: Annotated[OrganizationQueryService, Depends(get_query_service)],
) -> list[RelationshipResponse]:
    return query_service.list_relationships()
