"""Agent management routes."""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from api.dependencies import CommandDispatcher, OrganizationQueryService, get_command_dispatcher, get_query_service
from api.schemas.requests import ArchiveAgentRequest, CreateAgentRequest, UpdateAgentRequest
from api.schemas.responses import AgentResponse, CommandAcceptedResponse
from application.commands import ArchiveAgentCommand, CreateAgentCommand, UpdateAgentCommand

router = APIRouter(prefix="/agents", tags=["agents"])


@router.post("", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def create_agent(
    request: CreateAgentRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = CreateAgentCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        agent_id=request.agent_id,
        department_id=request.department_id,
        agent_name=request.agent_name,
        role_id=request.role_id,
        rank_id=request.rank_id,
        authority_level=request.authority_level,
    )
    return dispatcher.dispatch(command)


@router.get("/{agent_id}", response_model=AgentResponse, status_code=status.HTTP_200_OK)
def get_agent(
    agent_id: str,
    query_service: Annotated[OrganizationQueryService, Depends(get_query_service)],
) -> AgentResponse:
    return query_service.get_agent(agent_id)


@router.get("", response_model=list[AgentResponse], status_code=status.HTTP_200_OK)
def list_agents(
    query_service: Annotated[OrganizationQueryService, Depends(get_query_service)],
) -> list[AgentResponse]:
    return query_service.list_agents()


@router.patch("/{agent_id}", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def update_agent(
    agent_id: str,
    request: UpdateAgentRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = UpdateAgentCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        agent_id=agent_id,
        department_id=request.department_id,
        agent_name=request.agent_name,
        role_id=request.role_id,
        rank_id=request.rank_id,
        authority_level=request.authority_level,
        status=request.status,
    )
    return dispatcher.dispatch(command)


@router.delete("/{agent_id}", response_model=CommandAcceptedResponse, status_code=status.HTTP_202_ACCEPTED)
def archive_agent(
    agent_id: str,
    request: ArchiveAgentRequest,
    dispatcher: Annotated[CommandDispatcher, Depends(get_command_dispatcher)],
) -> CommandAcceptedResponse:
    command = ArchiveAgentCommand(
        organization_id=request.organization_id,
        actor_id=request.actor_id,
        reason=request.reason,
        metadata=request.metadata,
        agent_id=agent_id,
    )
    return dispatcher.dispatch(command)
