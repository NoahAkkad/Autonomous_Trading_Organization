"""Projector for department events."""

from events import DepartmentArchived, DepartmentCreated, DepartmentUpdated
from projections import DepartmentProjection, ProjectionRepository


class DepartmentProjector:
    """Applies department events to department_projection."""

    def __init__(self, repository: ProjectionRepository) -> None:
        self._repository = repository

    def apply_department_created(self, event: DepartmentCreated) -> None:
        self._repository.upsert_department(
            DepartmentProjection(
                department_id=str(event.department_id),
                organization_id=str(event.organization_id),
                department_name=event.department_name,
                department_code=event.department_code,
                status=event.status,
                department_head_id=None,
                agent_count=0,
                created_at=event.timestamp,
                updated_at=event.timestamp,
            )
        )
        self._repository.increment_organization_department_count(str(event.organization_id))

    def apply_department_updated(self, event: DepartmentUpdated) -> None:
        fields: dict[str, object] = {"updated_at": event.timestamp}
        if event.department_name is not None:
            fields["department_name"] = event.department_name
        if event.department_code is not None:
            fields["department_code"] = event.department_code
        if event.status is not None:
            fields["status"] = event.status
        self._repository.update_department(str(event.department_id), **fields)

    def apply_department_archived(self, event: DepartmentArchived) -> None:
        self._repository.update_department(
            str(event.department_id),
            status="archived",
            updated_at=event.timestamp,
        )
