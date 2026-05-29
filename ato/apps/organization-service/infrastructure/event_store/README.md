# Event Store

Contains the SQLAlchemy persistence model and repository for the organization-service event store.

This module is PostgreSQL compatible and is intentionally limited to storing and reading event records. It does not contain business logic, API routes, CQRS projections, or event publishing.
