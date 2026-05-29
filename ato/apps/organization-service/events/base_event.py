"""Base event model for organization-service facts."""

from datetime import datetime, timezone
from typing import NewType, TypeAlias
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

ActorId = NewType("ActorId", str)
AggregateId = NewType("AggregateId", str)
AggregateType = NewType("AggregateType", str)
CausationId = NewType("CausationId", str)
CorrelationId = NewType("CorrelationId", str)
EventId = NewType("EventId", str)
EventType = NewType("EventType", str)
OrganizationId = NewType("OrganizationId", str)

MetadataValue: TypeAlias = str | int | float | bool | None
EventMetadata: TypeAlias = dict[str, MetadataValue]


def new_event_id() -> EventId:
    """Create an opaque event identifier."""
    return EventId(str(uuid4()))


def utc_now() -> datetime:
    """Create a timezone-aware event timestamp."""
    return datetime.now(timezone.utc)


class BaseEvent(BaseModel):
    """Base immutable fact recorded by the organization service."""

    model_config = ConfigDict(extra="forbid", frozen=True, str_strip_whitespace=True)

    event_id: EventId = Field(default_factory=new_event_id)
    event_type: EventType
    organization_id: OrganizationId
    aggregate_id: AggregateId
    aggregate_type: AggregateType
    version: int = Field(ge=1)
    timestamp: datetime = Field(default_factory=utc_now)
    actor_id: ActorId
    correlation_id: CorrelationId
    causation_id: CausationId
    metadata: EventMetadata = Field(default_factory=dict)
