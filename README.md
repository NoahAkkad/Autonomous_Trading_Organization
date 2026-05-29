# ATO

ATO (Autonomous Trading Organization) is an institutional autonomous AI organization platform.

This repository is intentionally at its first scaffold stage. It defines the production-oriented boundaries for future services, shared contracts, infrastructure, databases, documentation, and automation scripts without implementing trading logic, agent runtime logic, or mock behavior.

## Requirements

- Python 3.13+
- Docker and Docker Compose for future local infrastructure

## Current Scope

- Clean architecture folder layout
- Minimal Python project metadata
- Service entrypoint that verifies the scaffold can execute
- Responsibility READMEs for major areas

## Run

```bash
python ato/apps/organization-service/main.py
```

The current version exits successfully without starting an application server or background runtime.

## Architecture

- `ato/apps`: deployable application services
- `ato/shared`: cross-service primitives and contracts
- `ato/databases`: migrations and seed data
- `ato/infrastructure`: local and deployment infrastructure configuration
- `ato/docs`: architecture and delivery documentation
- `ato/scripts`: operational and developer automation

## Development Status

Ready for Sprint 1 development.
