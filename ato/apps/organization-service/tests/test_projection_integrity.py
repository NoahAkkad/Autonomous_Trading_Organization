"""Institutional acceptance tests for projection integrity."""

from pathlib import Path
import sys
from collections.abc import Iterator
from contextlib import contextmanager

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

SERVICE_ROOT = Path(__file__).resolve().parents[1]
if str(SERVICE_ROOT) not in sys.path:
    sys.path.insert(0, str(SERVICE_ROOT))
TEST_ROOT = Path(__file__).resolve().parent
if str(TEST_ROOT) not in sys.path:
    sys.path.insert(0, str(TEST_ROOT))

from events import (
    AgentCreated,
    AgentDemoted,
    AgentPromoted,
    AgentUpdated,
    DepartmentArchived,
    DepartmentCreated,
    DepartmentUpdated,
    OrganizationArchived,
    OrganizationCreated,
    OrganizationUpdated,
    PermissionGranted,
    PermissionRevoked,
    RelationshipCreated,
    RelationshipRemoved,
    RoleAssigned,
    RoleRevoked,
)
from projections import (
    AgentProjection,
    Base,
    DepartmentProjection,
    OrganizationProjection,
    ProjectionRepository,
    RelationshipProjection,
)
from projectors import AgentProjector, DepartmentProjector, OrganizationProjector, RelationshipProjector
from test_organization_lifecycle import AGENTS, DEPARTMENTS, ORGANIZATION_ID, RELATIONSHIPS, build_bootstrap_events


@contextmanager
def projection_session() -> Iterator[Session]:
    engine = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    engine.dispose()


def apply_projection_events(session: Session) -> None:
    repository = ProjectionRepository(session)
    organization_projector = OrganizationProjector(repository)
    department_projector = DepartmentProjector(repository)
    agent_projector = AgentProjector(repository)
    relationship_projector = RelationshipProjector(repository)
    for event in build_bootstrap_events():
        if isinstance(event, OrganizationCreated):
            organization_projector.apply_organization_created(event)
        elif isinstance(event, OrganizationUpdated):
            organization_projector.apply_organization_updated(event)
        elif isinstance(event, OrganizationArchived):
            organization_projector.apply_organization_archived(event)
        elif isinstance(event, DepartmentCreated):
            department_projector.apply_department_created(event)
        elif isinstance(event, DepartmentUpdated):
            department_projector.apply_department_updated(event)
        elif isinstance(event, DepartmentArchived):
            department_projector.apply_department_archived(event)
        elif isinstance(event, AgentCreated):
            agent_projector.apply_agent_created(event)
        elif isinstance(event, AgentUpdated):
            agent_projector.apply_agent_updated(event)
        elif isinstance(event, RoleAssigned):
            agent_projector.apply_role_assigned(event)
        elif isinstance(event, RoleRevoked):
            agent_projector.apply_role_revoked(event)
        elif isinstance(event, AgentPromoted):
            agent_projector.apply_agent_promoted(event)
        elif isinstance(event, AgentDemoted):
            agent_projector.apply_agent_demoted(event)
        elif isinstance(event, PermissionGranted):
            agent_projector.apply_permission_granted(event)
        elif isinstance(event, PermissionRevoked):
            agent_projector.apply_permission_revoked(event)
        elif isinstance(event, RelationshipCreated):
            relationship_projector.apply_relationship_created(event)
        elif isinstance(event, RelationshipRemoved):
            relationship_projector.apply_relationship_removed(event)
    session.commit()


def test_build_projections_and_verify_projection_integrity() -> None:
    with projection_session() as session:
        apply_projection_events(session)

        organization = session.get(OrganizationProjection, ORGANIZATION_ID)
        departments = session.scalars(select(DepartmentProjection)).all()
        agents = session.scalars(select(AgentProjection)).all()
        relationships = session.scalars(select(RelationshipProjection)).all()

        assert organization is not None
        assert organization.department_count == len(DEPARTMENTS)
        assert organization.agent_count == len(AGENTS)
        assert len(departments) == len(DEPARTMENTS)
        assert len(agents) == len(AGENTS)
        assert len(relationships) == len(RELATIONSHIPS)


def test_verify_read_models() -> None:
    with projection_session() as session:
        apply_projection_events(session)

        ceo = session.get(AgentProjection, "AGENT-CEO")
        registrar = session.get(AgentProjection, "AGENT-REG")
        executive_office = session.get(DepartmentProjection, "DEPT-EXEC")

        assert ceo is not None
        assert ceo.agent_name == "CEO"
        assert ceo.role == "ROLE-CEO"
        assert ceo.rank == "RANK-C-SUITE"
        assert ceo.version == 4
        assert registrar is not None
        assert registrar.role == "ROLE-REGISTRAR"
        assert executive_office is not None
        assert executive_office.agent_count == 1
