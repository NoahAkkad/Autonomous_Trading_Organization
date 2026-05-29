"""Repository for appending and reading organization-service events."""

from collections.abc import Sequence

from sqlalchemy import Select, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from .exceptions import EventStoreError
from .models import EventStore
from .schemas import EventStoreAppendRecord, EventStoreRecord


class EventStoreRepository:
    """SQLAlchemy-backed repository for the event_store table."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def append_event(self, event: EventStoreAppendRecord) -> EventStoreRecord:
        try:
            model = self._to_model(event)
            self._session.add(model)
            self._session.flush()
            return self._to_record(model)
        except SQLAlchemyError as exc:
            raise EventStoreError("failed to append event") from exc

    def append_events(
        self,
        events: Sequence[EventStoreAppendRecord],
    ) -> list[EventStoreRecord]:
        try:
            models = [self._to_model(event) for event in events]
            self._session.add_all(models)
            self._session.flush()
            return [self._to_record(model) for model in models]
        except SQLAlchemyError as exc:
            raise EventStoreError("failed to append events") from exc

    def get_event_stream(self) -> list[EventStoreRecord]:
        statement = select(EventStore).order_by(EventStore.event_sequence.asc())
        return self._execute_event_query(statement)

    def get_events_by_aggregate(self, aggregate_id: str) -> list[EventStoreRecord]:
        statement = (
            select(EventStore)
            .where(EventStore.aggregate_id == aggregate_id)
            .order_by(EventStore.event_sequence.asc())
        )
        return self._execute_event_query(statement)

    def _execute_event_query(self, statement: Select[tuple[EventStore]]) -> list[EventStoreRecord]:
        try:
            return [
                self._to_record(model)
                for model in self._session.execute(statement).scalars().all()
            ]
        except SQLAlchemyError as exc:
            raise EventStoreError("failed to read events") from exc

    @staticmethod
    def _to_model(event: EventStoreAppendRecord) -> EventStore:
        return EventStore(
            event_id=event.event_id,
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

    @staticmethod
    def _to_record(model: EventStore) -> EventStoreRecord:
        return EventStoreRecord(
            event_id=model.event_id,
            event_sequence=model.event_sequence,
            organization_id=model.organization_id,
            aggregate_id=model.aggregate_id,
            aggregate_type=model.aggregate_type,
            event_type=model.event_type,
            event_version=model.event_version,
            timestamp=model.timestamp,
            actor_id=model.actor_id,
            correlation_id=model.correlation_id,
            causation_id=model.causation_id,
            payload_json=model.payload_json,
            metadata_json=model.metadata_json,
            audit_metadata_json=model.audit_metadata_json,
        )
