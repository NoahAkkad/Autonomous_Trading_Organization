"""Institutional acceptance tests for agent bootstrap lifecycle."""

from pathlib import Path
import sys

SERVICE_ROOT = Path(__file__).resolve().parents[1]
if str(SERVICE_ROOT) not in sys.path:
    sys.path.insert(0, str(SERVICE_ROOT))
TEST_ROOT = Path(__file__).resolve().parent
if str(TEST_ROOT) not in sys.path:
    sys.path.insert(0, str(TEST_ROOT))

from test_organization_lifecycle import AGENTS, ORGANIZATION_ID, build_bootstrap_events


def test_create_agents_assign_roles_ranks_and_permissions() -> None:
    events = build_bootstrap_events()
    agent_created = [event for event in events if str(event.event_type) == "agent.created"]
    role_assigned = [event for event in events if str(event.event_type) == "role.assigned"]
    rank_assigned = [event for event in events if str(event.event_type) == "agent.promoted"]
    permissions_granted = [event for event in events if str(event.event_type) == "permission.granted"]

    assert len(agent_created) == len(AGENTS)
    assert len(role_assigned) == len(AGENTS)
    assert len(rank_assigned) == len(AGENTS)
    assert len(permissions_granted) == len(AGENTS)
    assert [event.agent_name for event in agent_created] == [agent_name for _, agent_name, _, _, _, _ in AGENTS]
    assert all(event.organization_id == ORGANIZATION_ID for event in agent_created)
