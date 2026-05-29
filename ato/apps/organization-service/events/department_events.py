"""Department event models."""

from typing import Literal, NewType

from .base_event import AggregateType, BaseEvent

DepartmentId = NewType("DepartmentId", str)


class DepartmentCreated(BaseEvent):
    event_type: Literal["department.created"] = "department.created"
    aggregate_type: AggregateType = AggregateType("department")
    department_id: DepartmentId
    department_name: str
    department_code: str
    status: str


class DepartmentUpdated(BaseEvent):
    event_type: Literal["department.updated"] = "department.updated"
    aggregate_type: AggregateType = AggregateType("department")
    department_id: DepartmentId
    department_name: str | None = None
    department_code: str | None = None
    status: str | None = None


class DepartmentArchived(BaseEvent):
    event_type: Literal["department.archived"] = "department.archived"
    aggregate_type: AggregateType = AggregateType("department")
    department_id: DepartmentId
