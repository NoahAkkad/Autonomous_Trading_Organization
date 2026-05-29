"""Department management routes."""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from api.dependencies import CommandDispatcher, OrganizationQueryService, get_command_dispatcher, get_query_service
from api.schemas.requests import (
    ArchiveDepartmentRequest,
    CreateDepartmentRequest,
    UpdateDepartmentRequest,
)
from api.schemas.responses import CommandAcceptedResponse, DepartmentResponse
from application.commands import (
    ArchiveDepartmentCommand,
    CreateDepartmentCommand,
    UpdateDepartmentCommand,
)

router = APIRouter(prefix="/departments", tags=["departments"])


@router.post("", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def create_department(
    request: CreateDepartmentRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = CreateDepartmentCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        department_id=request.department_id,
        department_name=request.department_name,
        department_code=request.department_code,
    )
    return dispatcher.dispatch(command)


@router.get("/{department_id}", response_model=DepartmentResponse, status_code=status.HTTP_200_OK)
def get_department(
    department_id: str,
    query_service: Annotated[OrganizationQueryService, Depends(get_query_service)],
) -> DepartmentResponse:
    return query_service.get_department(department_id)


@router.get("", response_model=list[DepartmentResponse], status_code=status.HTTP_200_OK)
def list_departments(
    query_service: Annotated[OrganizationQueryService, Depends(get_query_service)],
) -> list[DepartmentResponse]:
    return query_service.list_departments()


@router.patch("/{department_id}", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def update_department(
    department_id: str,
    request: UpdateDepartmentRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = UpdateDepartmentCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        department_id=department_id,
        department_name=request.department_name,
        department_code=request.department_code,
        status=request.status,
    )
    return dispatcher.dispatch(command)


@router.delete("/{department_id}", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def archive_department(
    department_id: str,
    request: ArchiveDepartmentRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = ArchiveDepartmentCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        department_id=department_id,
    )
    return dispatcher.dispatch(command)
