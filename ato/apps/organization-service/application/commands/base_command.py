"""Base command model for organization-service request objects."""

from datetime import datetime, timezone
from typing import NewType, TypeAlias
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

ActorId = NewType("ActorId", str)
CommandId = NewType("CommandId", str)
CommandType = NewType("CommandType", str)
OrganizationId = NewType("OrganizationId", str)

MetadataValue: TypeAlias = str | int | float | bool | None
CommandMetadata: TypeAlias = dict[str, MetadataValue]


def new_command_id() -> CommandId:
    """Create an opaque command identifier."""
    return CommandId(str(uuid4()))


def utc_now() -> datetime:
    """Create a timezone-aware command timestamp."""
    return datetime.now(timezone.utc)


class OrganizationCommand(BaseModel):
    """Base request object for organization-service commands."""

    model_config = ConfigDict(extra="forbid", frozen=True, str_strip_whitespace=True)

    command_id: CommandId = Field(default_factory=new_command_id)
    command_type: CommandType
    organization_id: OrganizationId
    actor_id: ActorId
    timestamp: datetime = Field(default_factory=utc_now)
    reason: str
    metadata: CommandMetadata = Field(default_factory=dict)
