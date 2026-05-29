# Projectors

Transforms organization-service events into SQLAlchemy CQRS read models.

Projectors update projections only. They do not contain FastAPI routes, Event Bus integration, Redis, Kafka, event publishing, or CQRS write-side behavior.
