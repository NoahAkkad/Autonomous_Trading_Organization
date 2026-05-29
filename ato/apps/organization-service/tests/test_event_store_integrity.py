"""Institutional acceptance tests for event store integrity."""

from pathlib import Path
import sys

from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import CreateTable

SERVICE_ROOT = Path(__file__).resolve().parents[1]
if str(SERVICE_ROOT) not in sys.path:
    sys.path.insert(0, str(SERVICE_ROOT))
TEST_ROOT = Path(__file__).resolve().parent
if str(TEST_ROOT) not in sys.path:
    sys.path.insert(0, str(TEST_ROOT))

from infrastructure.event_store.models import EventStore
from test_organization_lifecycle import (
    ACTOR_ID,
    CORRELATION_ID,
    ORGANIZATION_ID,
    build_event_store,
)


def test_event_store_integrity_and_ordering() -> None:
    store, records = build_event_store()
    stream = store.get_event_stream()

    assert stream == records
    assert [record.event_sequence for record in stream] == list(range(1, len(stream) + 1))
    assert len({record.event_id for record in stream}) == len(stream)
    assert all(record.organization_id == ORGANIZATION_ID for record in stream)
    assert all(record.actor_id == ACTOR_ID for record in stream)
    assert all(record.correlation_id == CORRELATION_ID for record in stream)


def test_events_by_aggregate_are_ordered() -> None:
    store, _ = build_event_store()
    aggregate_events = store.get_events_by_aggregate("AGENT-CEO")

    assert [record.event_type for record in aggregate_events] == [
        "agent.created",
        "role.assigned",
        "agent.promoted",
        "permission.granted",
    ]
    assert [record.event_version for record in aggregate_events] == [1, 2, 3, 4]


def test_event_store_model_is_postgresql_compatible() -> None:
    ddl = str(CreateTable(EventStore.__table__).compile(dialect=postgresql.dialect()))

    assert "CREATE TABLE event_store" in ddl
    assert "UUID" in ddl
    assert "BIGINT" in ddl
    assert "JSONB" in ddl


def test_verify_audit_traceability() -> None:
    _, records = build_event_store()

    assert all(record.audit_metadata_json["actor_id"] == ACTOR_ID for record in records)
    assert all(record.audit_metadata_json["correlation_id"] == CORRELATION_ID for record in records)
    assert all(record.audit_metadata_json["causation_id"] for record in records)
    assert all(record.metadata_json["reason"] == "institutional bootstrap" for record in records)
