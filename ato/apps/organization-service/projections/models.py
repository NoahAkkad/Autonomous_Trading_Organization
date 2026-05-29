"""SQLAlchemy read models for organization-service projections."""

from datetime import datetime

from sqlalchemy import BigInteger, DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class for projection SQLAlchemy models."""


class OrganizationProjection(Base):
    """Read model for organization_projection."""

    __tablename__ = "organization_projection"

    organization_id: Mapped[str] = mapped_column(String(128), primary_key=True)
    organization_name: Mapped[str] = mapped_column(String(255), nullable=False)
    short_name: Mapped[str] = mapped_column(String(64), nullable=False)
    status: Mapped[str] = mapped_column(String(64), nullable=False)
    constitution_version: Mapped[str] = mapped_column(String(64), nullable=False)
    governance_version: Mapped[str] = mapped_column(String(64), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    department_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    agent_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)


class DepartmentProjection(Base):
    """Read model for department_projection."""

    __tablename__ = "department_projection"

    department_id: Mapped[str] = mapped_column(String(128), primary_key=True)
    organization_id: Mapped[str] = mapped_column(String(128), nullable=False)
    department_name: Mapped[str] = mapped_column(String(255), nullable=False)
    department_code: Mapped[str] = mapped_column(String(64), nullable=False)
    status: Mapped[str] = mapped_column(String(64), nullable=False)
    department_head_id: Mapped[str | None] = mapped_column(String(128), nullable=True)
    agent_count: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class AgentProjection(Base):
    """Read model for agent_projection."""

    __tablename__ = "agent_projection"

    agent_id: Mapped[str] = mapped_column(String(128), primary_key=True)
    organization_id: Mapped[str] = mapped_column(String(128), nullable=False)
    department_id: Mapped[str] = mapped_column(String(128), nullable=False)
    agent_name: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str | None] = mapped_column(String(128), nullable=True)
    rank: Mapped[str | None] = mapped_column(String(128), nullable=True)
    authority_level: Mapped[int] = mapped_column(BigInteger, nullable=False)
    status: Mapped[str] = mapped_column(String(64), nullable=False)
    version: Mapped[int] = mapped_column(BigInteger, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class RelationshipProjection(Base):
    """Read model for relationship_projection."""

    __tablename__ = "relationship_projection"

    relationship_id: Mapped[str] = mapped_column(String(128), primary_key=True)
    source_agent_id: Mapped[str] = mapped_column(String(128), nullable=False)
    target_agent_id: Mapped[str] = mapped_column(String(128), nullable=False)
    relationship_type: Mapped[str] = mapped_column(String(128), nullable=False)
    status: Mapped[str] = mapped_column(String(64), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
