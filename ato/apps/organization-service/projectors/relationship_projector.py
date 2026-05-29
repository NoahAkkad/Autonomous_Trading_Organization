"""Projector for relationship events."""

from events import RelationshipCreated, RelationshipRemoved
from projections import ProjectionRepository, RelationshipProjection


class RelationshipProjector:
    """Applies relationship events to relationship_projection."""

    def __init__(self, repository: ProjectionRepository) -> None:
        self._repository = repository

    def apply_relationship_created(self, event: RelationshipCreated) -> None:
        self._repository.upsert_relationship(
            RelationshipProjection(
                relationship_id=str(event.relationship_id),
                source_agent_id=str(event.source_agent_id),
                target_agent_id=str(event.target_agent_id),
                relationship_type=event.relationship_type,
                status="active",
                created_at=event.timestamp,
            )
        )

    def apply_relationship_removed(self, event: RelationshipRemoved) -> None:
        self._repository.update_relationship(
            str(event.relationship_id),
            status="removed",
        )
