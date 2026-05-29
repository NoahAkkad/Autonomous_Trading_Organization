"""Organization event models."""

from typing import Literal

from .base_event import AggregateType, BaseEvent


class OrganizationCreated(BaseEvent):
    event_type: Literal["organization.created"] = "organization.created"
    aggregate_type: AggregateType = AggregateType("organization")
    organization_name: str
    short_name: str
    status: str
    constitution_version: str
    governance_version: str


class OrganizationUpdated(BaseEvent):
    event_type: Literal["organization.updated"] = "organization.updated"
    aggregate_type: AggregateType = AggregateType("organization")
    organization_name: str | None = None
    short_name: str | None = None
    status: str | None = None
    constitution_version: str | None = None
    governance_version: str | None = None


class OrganizationArchived(BaseEvent):
    event_type: Literal["organization.archived"] = "organization.archived"
    aggregate_type: AggregateType = AggregateType("organization")
