"""Institutional acceptance tests for state rebuild from event store."""

from pathlib import Path
import sys
from typing import Any

SERVICE_ROOT = Path(__file__).resolve().parents[1]
if str(SERVICE_ROOT) not in sys.path:
    sys.path.insert(0, str(SERVICE_ROOT))
TEST_ROOT = Path(__file__).resolve().parent
if str(TEST_ROOT) not in sys.path:
    sys.path.insert(0, str(TEST_ROOT))

from test_organization_lifecycle import AGENTS, DEPARTMENTS, ORGANIZATION_ID, RELATIONSHIPS, build_bootstrap_events


def rebuild_state(events: list[Any]) -> dict[str, dict[str, Any]]:
    state: dict[str, dict[str, Any]] = {
        "organizations": {},
        "departments": {},
        "agents": {},
        "relationships": {},
    }
    for event in events:
        event_type = str(event.event_type)
        if event_type == "organization.created":
            state["organizations"][str(event.organization_id)] = {
                "organization_name": event.organization_name,
                "short_name": event.short_name,
                "status": event.status,
                "constitution_version": event.constitution_version,
                "governance_version": event.governance_version,
            }
        elif event_type == "department.created":
            state["departments"][str(event.department_id)] = {
                "organization_id": str(event.organization_id),
                "department_name": event.department_name,
                "department_code": event.department_code,
                "status": event.status,
            }
        elif event_type == "agent.created":
            state["agents"][str(event.agent_id)] = {
                "organization_id": str(event.organization_id),
                "department_id": str(event.department_id),
                "agent_name": event.agent_name,
                "role": str(event.role_id),
                "rank": str(event.rank_id),
                "authority_level": event.authority_level,
                "status": event.status,
                "version": event.version,
            }
        elif event_type == "role.assigned":
            state["agents"][str(event.agent_id)]["role"] = str(event.role_id)
            state["agents"][str(event.agent_id)]["version"] = event.version
        elif event_type == "agent.promoted":
            state["agents"][str(event.agent_id)]["rank"] = str(event.new_rank_id)
            state["agents"][str(event.agent_id)]["version"] = event.version
        elif event_type == "permission.granted":
            state["agents"][str(event.agent_id)]["version"] = event.version
        elif event_type == "relationship.created":
            state["relationships"][str(event.relationship_id)] = {
                "source_agent_id": str(event.source_agent_id),
                "target_agent_id": str(event.target_agent_id),
                "relationship_type": event.relationship_type,
                "status": "active",
            }
    return state


def test_rebuild_state_from_event_store_matches_original_state() -> None:
    rebuilt_state = rebuild_state(build_bootstrap_events())

    assert rebuilt_state["organizations"][ORGANIZATION_ID]["organization_name"] == (
        "Autonomous Trading Organization"
    )
    assert set(rebuilt_state["departments"]) == {department_id for department_id, _, _ in DEPARTMENTS}
    assert set(rebuilt_state["agents"]) == {agent_id for agent_id, _, _, _, _, _ in AGENTS}
    assert set(rebuilt_state["relationships"]) == {
        relationship_id for relationship_id, _, _, _ in RELATIONSHIPS
    }
    assert rebuilt_state["agents"]["AGENT-CEO"]["role"] == "ROLE-CEO"
    assert rebuilt_state["agents"]["AGENT-CEO"]["rank"] == "RANK-C-SUITE"
    assert rebuilt_state["agents"]["AGENT-CEO"]["version"] == 4
