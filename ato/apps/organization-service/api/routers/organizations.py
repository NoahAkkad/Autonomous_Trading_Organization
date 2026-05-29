"""Organization management routes."""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from api.dependencies import CommandDispatcher, OrganizationQueryService, get_command_dispatcher, get_query_service
from api.schemas.requests import (
    ArchiveOrganizationRequest,
    CreateOrganizationRequest,
    UpdateOrganizationRequest,
)
from api.schemas.responses import CommandAcceptedResponse, OrganizationResponse
from application.commands import (
    ArchiveOrganizationCommand,
    CreateOrganizationCommand,
    UpdateOrganizationCommand,
)

router = APIRouter(prefix="/organizations", tags=["organizations"])


@router.post("", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def create_organization(
    request: CreateOrganizationRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = CreateOrganizationCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        organization_name=request.organization_name,
        short_name=request.short_name,
        constitution_version=request.constitution_version,
        governance_version=request.governance_version,
    )
    return dispatcher.dispatch(command)


@router.get("/{organization_id}", response_model=OrganizationResponse, status_code=status.HTTP_200_OK)
def get_organization(
    organization_id: str,
    query_service: Annotated[OrganizationQueryService, Depends(get_query_service)],
) -> OrganizationResponse:
    return query_service.get_organization(organization_id)


@router.patch("/{organization_id}", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def update_organization(
    organization_id: str,
    request: UpdateOrganizationRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = UpdateOrganizationCommand(
        organization_id=organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        organization_name=request.organization_name,
        short_name=request.short_name,
        status=request.status,
        constitution_version=request.constitution_version,
        governance_version=request.governance_version,
    )
    return dispatcher.dispatch(command)


@router.delete("/{organization_id}", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def archive_organization(
    organization_id: str,
    request: ArchiveOrganizationRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = ArchiveOrganizationCommand(
        organization_id=organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
    )
    return dispatcher.dispatch(command)
