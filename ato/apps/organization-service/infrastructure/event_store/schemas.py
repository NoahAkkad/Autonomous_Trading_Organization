"""Typed event store data transfer schemas."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import UUID


JsonObject = dict[str, Any]


@dataclass(frozen=True, slots=True, kw_only=True)
class EventStoreAppendRecord:
    event_id: UUID
    organization_id: str
    aggregate_id: str
    aggregate_type: str
    event_type: str
    event_version: int
    timestamp: datetime
    actor_id: str
    correlation_id: str
    causation_id: str
    payload_json: JsonObject = field(default_factory=dict)
    metadata_json: JsonObject = field(default_factory=dict)
    audit_metadata_json: JsonObject = field(default_factory=dict)


@dataclass(frozen=True, slots=True, kw_only=True)
class EventStoreRecord:
    event_id: UUID
    event_sequence: int
    organization_id: str
    aggregate_id: str
    aggregate_type: str
    event_type: str
    event_version: int
    timestamp: datetime
    actor_id: str
    correlation_id: str
    causation_id: str
    payload_json: JsonObject
    metadata_json: JsonObject
    audit_metadata_json: JsonObject
