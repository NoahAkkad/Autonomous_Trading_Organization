# API

Exposes organization-service management REST APIs using FastAPI.

Routes validate HTTP requests, create application command objects, and delegate work through dependency-injected interfaces. Routes do not contain business logic, authentication, persistence, Event Bus integration, Redis, Kafka, or CQRS projection behavior.
