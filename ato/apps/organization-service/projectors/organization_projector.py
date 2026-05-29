"""Projector for organization events."""

from events import OrganizationArchived, OrganizationCreated, OrganizationUpdated
from projections import OrganizationProjection, ProjectionRepository


class OrganizationProjector:
    """Applies organization events to organization_projection."""

    def __init__(self, repository: ProjectionRepository) -> None:
        self._repository = repository

    def apply_organization_created(self, event: OrganizationCreated) -> None:
        self._repository.upsert_organization(
            OrganizationProjection(
                organization_id=str(event.organization_id),
                organization_name=event.organization_name,
                short_name=event.short_name,
                status=event.status,
                constitution_version=event.constitution_version,
                governance_version=event.governance_version,
                created_at=event.timestamp,
                updated_at=event.timestamp,
                department_count=0,
                agent_count=0,
            )
        )

    def apply_organization_updated(self, event: OrganizationUpdated) -> None:
        fields: dict[str, object] = {"updated_at": event.timestamp}
        if event.organization_name is not None:
            fields["organization_name"] = event.organization_name
        if event.short_name is not None:
            fields["short_name"] = event.short_name
        if event.status is not None:
            fields["status"] = event.status
        if event.constitution_version is not None:
            fields["constitution_version"] = event.constitution_version
        if event.governance_version is not None:
            fields["governance_version"] = event.governance_version
        self._repository.update_organization(str(event.organization_id), **fields)

    def apply_organization_archived(self, event: OrganizationArchived) -> None:
        self._repository.update_organization(
            str(event.organization_id),
            status="archived",
            updated_at=event.timestamp,
        )
