"""Repository operations for organization-service projections."""

from .models import (
    AgentProjection,
    DepartmentProjection,
    OrganizationProjection,
    RelationshipProjection,
)
from sqlalchemy.orm import Session


class ProjectionRepository:
    """SQLAlchemy repository for CQRS read models."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def upsert_organization(self, projection: OrganizationProjection) -> None:
        self._session.merge(projection)
        self._session.flush()

    def update_organization(self, organization_id: str, **fields: object) -> None:
        projection = self._session.get(OrganizationProjection, organization_id)
        if projection is None:
            return
        self._assign_fields(projection, fields)
        self._session.flush()

    def increment_organization_department_count(self, organization_id: str) -> None:
        projection = self._session.get(OrganizationProjection, organization_id)
        if projection is None:
            return
        projection.department_count += 1
        self._session.flush()

    def increment_organization_agent_count(self, organization_id: str) -> None:
        projection = self._session.get(OrganizationProjection, organization_id)
        if projection is None:
            return
        projection.agent_count += 1
        self._session.flush()

    def upsert_department(self, projection: DepartmentProjection) -> None:
        self._session.merge(projection)
        self._session.flush()

    def update_department(self, department_id: str, **fields: object) -> None:
        projection = self._session.get(DepartmentProjection, department_id)
        if projection is None:
            return
        self._assign_fields(projection, fields)
        self._session.flush()

    def increment_department_agent_count(self, department_id: str) -> None:
        projection = self._session.get(DepartmentProjection, department_id)
        if projection is None:
            return
        projection.agent_count += 1
        self._session.flush()

    def upsert_agent(self, projection: AgentProjection) -> None:
        self._session.merge(projection)
        self._session.flush()

    def update_agent(self, agent_id: str, **fields: object) -> None:
        projection = self._session.get(AgentProjection, agent_id)
        if projection is None:
            return
        self._assign_fields(projection, fields)
        self._session.flush()

    def upsert_relationship(self, projection: RelationshipProjection) -> None:
        self._session.merge(projection)
        self._session.flush()

    def update_relationship(self, relationship_id: str, **fields: object) -> None:
        projection = self._session.get(RelationshipProjection, relationship_id)
        if projection is None:
            return
        self._assign_fields(projection, fields)
        self._session.flush()

    @staticmethod
    def _assign_fields(projection: object, fields: dict[str, object]) -> None:
        for field_name, value in fields.items():
            setattr(projection, field_name, value)
