"""Projector for agent, role, rank, and permission events."""

from events import (
    AgentArchived,
    AgentCreated,
    AgentDemoted,
    AgentPromoted,
    AgentUpdated,
    PermissionGranted,
    PermissionRevoked,
    RoleAssigned,
    RoleRevoked,
)
from projections import AgentProjection, ProjectionRepository


class AgentProjector:
    """Applies agent-related events to agent_projection."""

    def __init__(self, repository: ProjectionRepository) -> None:
        self._repository = repository

    def apply_agent_created(self, event: AgentCreated) -> None:
        self._repository.upsert_agent(
            AgentProjection(
                agent_id=str(event.agent_id),
                organization_id=str(event.organization_id),
                department_id=str(event.department_id),
                agent_name=event.agent_name,
                role=str(event.role_id),
                rank=str(event.rank_id),
                authority_level=event.authority_level,
                status=event.status,
                version=event.version,
                created_at=event.timestamp,
                updated_at=event.timestamp,
            )
        )
        self._repository.increment_organization_agent_count(str(event.organization_id))
        self._repository.increment_department_agent_count(str(event.department_id))

    def apply_agent_updated(self, event: AgentUpdated) -> None:
        fields: dict[str, object] = {
            "version": event.version,
            "updated_at": event.timestamp,
        }
        if event.department_id is not None:
            fields["department_id"] = str(event.department_id)
        if event.agent_name is not None:
            fields["agent_name"] = event.agent_name
        if event.role_id is not None:
            fields["role"] = str(event.role_id)
        if event.rank_id is not None:
            fields["rank"] = str(event.rank_id)
        if event.authority_level is not None:
            fields["authority_level"] = event.authority_level
        if event.status is not None:
            fields["status"] = event.status
        self._repository.update_agent(str(event.agent_id), **fields)

    def apply_agent_archived(self, event: AgentArchived) -> None:
        self._repository.update_agent(
            str(event.agent_id),
            status="archived",
            version=event.version,
            updated_at=event.timestamp,
        )

    def apply_role_assigned(self, event: RoleAssigned) -> None:
        self._repository.update_agent(
            str(event.agent_id),
            role=str(event.role_id),
            version=event.version,
            updated_at=event.timestamp,
        )

    def apply_role_revoked(self, event: RoleRevoked) -> None:
        self._repository.update_agent(
            str(event.agent_id),
            role=None,
            version=event.version,
            updated_at=event.timestamp,
        )

    def apply_agent_promoted(self, event: AgentPromoted) -> None:
        self._repository.update_agent(
            str(event.agent_id),
            rank=str(event.new_rank_id),
            version=event.version,
            updated_at=event.timestamp,
        )

    def apply_agent_demoted(self, event: AgentDemoted) -> None:
        self._repository.update_agent(
            str(event.agent_id),
            rank=str(event.new_rank_id),
            version=event.version,
            updated_at=event.timestamp,
        )

    def apply_permission_granted(self, event: PermissionGranted) -> None:
        self._repository.update_agent(
            str(event.agent_id),
            version=event.version,
            updated_at=event.timestamp,
        )

    def apply_permission_revoked(self, event: PermissionRevoked) -> None:
        self._repository.update_agent(
            str(event.agent_id),
            version=event.version,
            updated_at=event.timestamp,
        )
