"""FastAPI dependencies for organization-service API routes."""

from typing import Protocol

from fastapi import HTTPException, status
from application.commands import OrganizationCommand
from .schemas.responses import (
    AgentResponse,
    CommandAcceptedResponse,
    DepartmentResponse,
    OrganizationResponse,
    RelationshipResponse,
)


class CommandDispatcher(Protocol):
    """Application-layer command dispatcher interface."""

    def dispatch(self, command: OrganizationCommand) -> CommandAcceptedResponse:
        """Dispatch a command request object."""


class OrganizationQueryService(Protocol):
    """Read-model query interface for organization management APIs."""

    def get_organization(self, organization_id: str) -> OrganizationResponse:
        """Return one organization projection."""

    def get_department(self, department_id: str) -> DepartmentResponse:
        """Return one department projection."""

    def list_departments(self) -> list[DepartmentResponse]:
        """Return department projections."""

    def get_agent(self, agent_id: str) -> AgentResponse:
        """Return one agent projection."""

    def list_agents(self) -> list[AgentResponse]:
        """Return agent projections."""

    def list_relationships(self) -> list[RelationshipResponse]:
        """Return relationship projections."""


class AcceptedCommandDispatcher:
    """Default command dispatcher for API contract validation."""

    def dispatch(self, command: OrganizationCommand) -> CommandAcceptedResponse:
        return CommandAcceptedResponse(
            command_id=str(command.command_id),
            command_type=str(command.command_type),
            status="accepted",
        )


def get_command_dispatcher() -> CommandDispatcher:
    """Return the configured command dispatcher."""
    return AcceptedCommandDispatcher()


class UnconfiguredOrganizationQueryService:
    """Default query service used until projection-backed queries are configured."""

    def get_organization(self, organization_id: str) -> OrganizationResponse:
        raise self._not_configured()

    def get_department(self, department_id: str) -> DepartmentResponse:
        raise self._not_configured()

    def list_departments(self) -> list[DepartmentResponse]:
        raise self._not_configured()

    def get_agent(self, agent_id: str) -> AgentResponse:
        raise self._not_configured()

    def list_agents(self) -> list[AgentResponse]:
        raise self._not_configured()

    def list_relationships(self) -> list[RelationshipResponse]:
        raise self._not_configured()

    @staticmethod
    def _not_configured() -> HTTPException:
        return HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="query service is not configured",
        )


def get_query_service() -> OrganizationQueryService:
    """Return the configured organization query service."""
    return UnconfiguredOrganizationQueryService()
