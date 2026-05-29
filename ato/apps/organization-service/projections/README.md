# Projections

Contains SQLAlchemy read models and repository operations for organization-service CQRS projections.

Projection models are PostgreSQL compatible read models only. They do not contain business logic, FastAPI routes, Event Bus integration, Redis, Kafka, or event publishing.
