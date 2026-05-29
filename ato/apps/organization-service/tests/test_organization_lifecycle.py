"""Institutional acceptance tests for the ATO organization lifecycle."""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Any
from uuid import UUID, uuid5, NAMESPACE_URL

SERVICE_ROOT = Path(__file__).resolve().parents[1]
if str(SERVICE_ROOT) not in sys.path:
    sys.path.insert(0, str(SERVICE_ROOT))

from events import (  # noqa: E402
    AgentCreated,
    AgentPromoted,
    BaseEvent,
    DepartmentCreated,
    OrganizationCreated,
    PermissionGranted,
    RelationshipCreated,
    RoleAssigned,
)
from infrastructure.event_store.models import EventStore  # noqa: E402
from infrastructure.event_store.repository import EventStoreRepository  # noqa: E402
from infrastructure.event_store.schemas import EventStoreAppendRecord, EventStoreRecord  # noqa: E402

ORGANIZATION_ID = "ORG-0001"
ORGANIZATION_NAME = "Autonomous Trading Organization"
ORGANIZATION_SHORT_NAME = "ATO"
ACTOR_ID = "SYSTEM-BOOTSTRAP"
CORRELATION_ID = "CORR-ATO-BOOTSTRAP-0001"

DEPARTMENTS = [
    ("DEPT-EXEC", "Executive Office", "EXEC"),
    ("DEPT-GOV", "Governance Department", "GOV"),
    ("DEPT-RISK", "Risk Department", "RISK"),
    ("DEPT-RESEARCH", "Research Department", "RESEARCH"),
    ("DEPT-AUDIT", "Audit Department", "AUDIT"),
    ("DEPT-KNOWLEDGE", "Knowledge Department", "KNOWLEDGE"),
    ("DEPT-MEMORY", "Memory Department", "MEMORY"),
    ("DEPT-ORG", "Organization Department", "ORG"),
]

AGENTS = [
    ("AGENT-CEO", "CEO", "DEPT-EXEC", "ROLE-CEO", "RANK-C-SUITE", "PERMISSION-EXECUTE"),
    ("AGENT-CGO", "Chief Governance Officer", "DEPT-GOV", "ROLE-CGO", "RANK-C-SUITE", "PERMISSION-GOVERN"),
    ("AGENT-CRO", "CRO", "DEPT-RISK", "ROLE-CRO", "RANK-C-SUITE", "PERMISSION-RISK"),
    ("AGENT-HOR", "Head of Research", "DEPT-RESEARCH", "ROLE-HOR", "RANK-HEAD", "PERMISSION-RESEARCH"),
    ("AGENT-CA", "Chief Auditor", "DEPT-AUDIT", "ROLE-CA", "RANK-C-SUITE", "PERMISSION-AUDIT"),
    ("AGENT-CKO", "Chief Knowledge Officer", "DEPT-KNOWLEDGE", "ROLE-CKO", "RANK-C-SUITE", "PERMISSION-KNOWLEDGE"),
    ("AGENT-CMO", "Chief Memory Officer", "DEPT-MEMORY", "ROLE-CMO", "RANK-C-SUITE", "PERMISSION-MEMORY"),
    ("AGENT-REG", "Corporate Registrar", "DEPT-ORG", "ROLE-REGISTRAR", "RANK-OFFICER", "PERMISSION-REGISTER"),
]

RELATIONSHIPS = [
    ("REL-CEO-CGO", "AGENT-CEO", "AGENT-CGO", "supervises"),
    ("REL-CEO-CRO", "AGENT-CEO", "AGENT-CRO", "supervises"),
    ("REL-CEO-HOR", "AGENT-CEO", "AGENT-HOR", "supervises"),
    ("REL-CEO-CA", "AGENT-CEO", "AGENT-CA", "supervises"),
    ("REL-CEO-CKO", "AGENT-CEO", "AGENT-CKO", "supervises"),
    ("REL-CEO-CMO", "AGENT-CEO", "AGENT-CMO", "supervises"),
    ("REL-CEO-REG", "AGENT-CEO", "AGENT-REG", "supervises"),
]


def build_bootstrap_events() -> list[BaseEvent]:
    events: list[BaseEvent] = [
        OrganizationCreated(
            organization_id=ORGANIZATION_ID,
            aggregate_id=ORGANIZATION_ID,
            version=1,
            actor_id=ACTOR_ID,
            correlation_id=CORRELATION_ID,
            causation_id="CMD-CREATE-ORG",
            organization_name=ORGANIZATION_NAME,
            short_name=ORGANIZATION_SHORT_NAME,
            status="active",
            constitution_version="v1",
            governance_version="v1",
            metadata={"reason": "institutional bootstrap"},
        )
    ]
    events.extend(
        DepartmentCreated(
            organization_id=ORGANIZATION_ID,
            aggregate_id=department_id,
            version=1,
            actor_id=ACTOR_ID,
            correlation_id=CORRELATION_ID,
            causation_id=f"CMD-CREATE-{department_id}",
            department_id=department_id,
            department_name=department_name,
            department_code=department_code,
            status="active",
            metadata={"reason": "institutional bootstrap"},
        )
        for department_id, department_name, department_code in DEPARTMENTS
    )
    events.extend(
        AgentCreated(
            organization_id=ORGANIZATION_ID,
            aggregate_id=agent_id,
            version=1,
            actor_id=ACTOR_ID,
            correlation_id=CORRELATION_ID,
            causation_id=f"CMD-CREATE-{agent_id}",
            agent_id=agent_id,
            department_id=department_id,
            agent_name=agent_name,
            role_id="ROLE-PENDING",
            rank_id="RANK-PENDING",
            authority_level=1,
            status="active",
            metadata={"reason": "institutional bootstrap"},
        )
        for agent_id, agent_name, department_id, _, _, _ in AGENTS
    )
    events.extend(
        RoleAssigned(
            organization_id=ORGANIZATION_ID,
            aggregate_id=agent_id,
            version=2,
            actor_id=ACTOR_ID,
            correlation_id=CORRELATION_ID,
            causation_id=f"CMD-ASSIGN-ROLE-{agent_id}",
            agent_id=agent_id,
            role_id=role_id,
            metadata={"reason": "institutional bootstrap"},
        )
        for agent_id, _, _, role_id, _, _ in AGENTS
    )
    events.extend(
        AgentPromoted(
            organization_id=ORGANIZATION_ID,
            aggregate_id=agent_id,
            version=3,
            actor_id=ACTOR_ID,
            correlation_id=CORRELATION_ID,
            causation_id=f"CMD-ASSIGN-RANK-{agent_id}",
            agent_id=agent_id,
            previous_rank_id="RANK-PENDING",
            new_rank_id=rank_id,
            metadata={"reason": "institutional bootstrap"},
        )
        for agent_id, _, _, _, rank_id, _ in AGENTS
    )
    events.extend(
        PermissionGranted(
            organization_id=ORGANIZATION_ID,
            aggregate_id=agent_id,
            version=4,
            actor_id=ACTOR_ID,
            correlation_id=CORRELATION_ID,
            causation_id=f"CMD-GRANT-PERMISSION-{agent_id}",
            agent_id=agent_id,
            permission_id=permission_id,
            metadata={"reason": "institutional bootstrap"},
        )
        for agent_id, _, _, _, _, permission_id in AGENTS
    )
    events.extend(
        RelationshipCreated(
            organization_id=ORGANIZATION_ID,
            aggregate_id=relationship_id,
            version=1,
            actor_id=ACTOR_ID,
            correlation_id=CORRELATION_ID,
            causation_id=f"CMD-CREATE-{relationship_id}",
            relationship_id=relationship_id,
            source_agent_id=source_agent_id,
            target_agent_id=target_agent_id,
            relationship_type=relationship_type,
            metadata={"reason": "institutional bootstrap"},
        )
        for relationship_id, source_agent_id, target_agent_id, relationship_type in RELATIONSHIPS
    )
    return events


def append_record_from_event(event: BaseEvent) -> EventStoreAppendRecord:
    payload = event.model_dump(mode="json")
    return EventStoreAppendRecord(
        event_id=UUID(str(event.event_id)),
        organization_id=str(event.organization_id),
        aggregate_id=str(event.aggregate_id),
        aggregate_type=str(event.aggregate_type),
        event_type=str(event.event_type),
        event_version=event.version,
        timestamp=event.timestamp,
        actor_id=str(event.actor_id),
        correlation_id=str(event.correlation_id),
        causation_id=str(event.causation_id),
        payload_json=payload,
        metadata_json=dict(event.metadata),
        audit_metadata_json={
            "actor_id": str(event.actor_id),
            "correlation_id": str(event.correlation_id),
            "causation_id": str(event.causation_id),
        },
    )


class InMemoryEventStore:
    def __init__(self) -> None:
        self._records: list[EventStoreRecord] = []

    def append_event(self, event: EventStoreAppendRecord) -> EventStoreRecord:
        record = self._record_from_append(event)
        self._records.append(record)
        return record

    def append_events(self, events: list[EventStoreAppendRecord]) -> list[EventStoreRecord]:
        return [self.append_event(event) for event in events]

    def get_event_stream(self) -> list[EventStoreRecord]:
        return list(self._records)

    def get_events_by_aggregate(self, aggregate_id: str) -> list[EventStoreRecord]:
        return [record for record in self._records if record.aggregate_id == aggregate_id]

    def _record_from_append(self, event: EventStoreAppendRecord) -> EventStoreRecord:
        return EventStoreRecord(
            event_id=event.event_id,
            event_sequence=len(self._records) + 1,
            organization_id=event.organization_id,
            aggregate_id=event.aggregate_id,
            aggregate_type=event.aggregate_type,
            event_type=event.event_type,
            event_version=event.event_version,
            timestamp=event.timestamp,
            actor_id=event.actor_id,
            correlation_id=event.correlation_id,
            causation_id=event.causation_id,
            payload_json=event.payload_json,
            metadata_json=event.metadata_json,
            audit_metadata_json=event.audit_metadata_json,
        )


def build_event_store() -> tuple[InMemoryEventStore, list[EventStoreRecord]]:
    store = InMemoryEventStore()
    records = store.append_events([append_record_from_event(event) for event in build_bootstrap_events()])
    return store, records


def deterministic_event_id(name: str) -> UUID:
    return uuid5(NAMESPACE_URL, f"ato.acceptance.{name}")


def test_create_organization_event_is_valid() -> None:
    event = build_bootstrap_events()[0]

    assert isinstance(event, OrganizationCreated)
    assert event.organization_id == ORGANIZATION_ID
    assert event.organization_name == ORGANIZATION_NAME
    assert event.short_name == ORGANIZATION_SHORT_NAME
    assert event.status == "active"
    assert event.constitution_version == "v1"
    assert event.governance_version == "v1"


def test_verify_events_created_for_full_bootstrap_lifecycle() -> None:
    events = build_bootstrap_events()
    event_types = [str(event.event_type) for event in events]

    assert len(events) == 48
    assert event_types.count("organization.created") == 1
    assert event_types.count("department.created") == 8
    assert event_types.count("agent.created") == 8
    assert event_types.count("role.assigned") == 8
    assert event_types.count("agent.promoted") == 8
    assert event_types.count("permission.granted") == 8
    assert event_types.count("relationship.created") == 7


def test_event_store_repository_maps_append_record_to_model() -> None:
    event = build_bootstrap_events()[0]
    append_record = append_record_from_event(event)

    model = EventStoreRepository._to_model(append_record)

    assert isinstance(model, EventStore)
    assert model.event_id == append_record.event_id
    assert model.organization_id == ORGANIZATION_ID
    assert model.aggregate_id == ORGANIZATION_ID
    assert model.event_type == "organization.created"
    assert model.payload_json["organization_name"] == ORGANIZATION_NAME
