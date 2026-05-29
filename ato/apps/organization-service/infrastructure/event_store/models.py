"""SQLAlchemy models for the organization-service event store."""

from datetime import datetime
from typing import Any
from uuid import UUID

from sqlalchemy import BigInteger, DateTime, Identity, Index, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class for event store SQLAlchemy models."""


class EventStore(Base):
    """PostgreSQL-compatible event store table."""

    __tablename__ = "event_store"
    __table_args__ = (
        UniqueConstraint("event_sequence", name="uq_event_store_event_sequence"),
        Index("ix_event_store_organization_id", "organization_id"),
        Index("ix_event_store_aggregate_id", "aggregate_id"),
        Index("ix_event_store_aggregate_type", "aggregate_type"),
        Index("ix_event_store_event_type", "event_type"),
        Index("ix_event_store_timestamp", "timestamp"),
        Index("ix_event_store_correlation_id", "correlation_id"),
    )

    event_id: Mapped[UUID] = mapped_column(
        PostgresUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
    )
    event_sequence: Mapped[int] = mapped_column(
        BigInteger,
        Identity(),
        nullable=False,
        unique=True,
    )
    organization_id: Mapped[str] = mapped_column(String(128), nullable=False)
    aggregate_id: Mapped[str] = mapped_column(String(128), nullable=False)
    aggregate_type: Mapped[str] = mapped_column(String(128), nullable=False)
    event_type: Mapped[str] = mapped_column(String(128), nullable=False)
    event_version: Mapped[int] = mapped_column(BigInteger, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    actor_id: Mapped[str] = mapped_column(String(128), nullable=False)
    correlation_id: Mapped[str] = mapped_column(String(128), nullable=False)
    causation_id: Mapped[str] = mapped_column(String(128), nullable=False)
    payload_json: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False)
    metadata_json: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False)
    audit_metadata_json: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False)
