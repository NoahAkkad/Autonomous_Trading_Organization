"""Event models for the organization service."""

from .agent_events import AgentArchived, AgentCreated, AgentUpdated
from .base_event import (
    ActorId,
    AggregateId,
    AggregateType,
    BaseEvent,
    CausationId,
    CorrelationId,
    EventId,
    EventMetadata,
    EventType,
    OrganizationId,
)
from .department_events import DepartmentArchived, DepartmentCreated, DepartmentUpdated
from .organization_events import (
    OrganizationArchived,
    OrganizationCreated,
    OrganizationUpdated,
)
from .permission_events import PermissionGranted, PermissionRevoked
from .rank_events import AgentDemoted, AgentPromoted
from .relationship_events import RelationshipCreated, RelationshipRemoved
from .role_events import RoleAssigned, RoleRevoked

__all__ = [
    "ActorId",
    "AgentArchived",
    "AgentCreated",
    "AgentDemoted",
    "AgentPromoted",
    "AgentUpdated",
    "AggregateId",
    "AggregateType",
    "BaseEvent",
    "CausationId",
    "CorrelationId",
    "DepartmentArchived",
    "DepartmentCreated",
    "DepartmentUpdated",
    "EventId",
    "EventMetadata",
    "EventType",
    "OrganizationArchived",
    "OrganizationCreated",
    "OrganizationId",
    "OrganizationUpdated",
    "PermissionGranted",
    "PermissionRevoked",
    "RelationshipCreated",
    "RelationshipRemoved",
    "RoleAssigned",
    "RoleRevoked",
]
