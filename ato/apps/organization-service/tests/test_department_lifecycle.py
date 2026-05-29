"""Institutional acceptance tests for department bootstrap lifecycle."""

from pathlib import Path
import sys

SERVICE_ROOT = Path(__file__).resolve().parents[1]
if str(SERVICE_ROOT) not in sys.path:
    sys.path.insert(0, str(SERVICE_ROOT))
TEST_ROOT = Path(__file__).resolve().parent
if str(TEST_ROOT) not in sys.path:
    sys.path.insert(0, str(TEST_ROOT))

from test_organization_lifecycle import DEPARTMENTS, ORGANIZATION_ID, build_bootstrap_events


def test_create_departments_for_institutional_bootstrap() -> None:
    department_events = [
        event for event in build_bootstrap_events() if str(event.event_type) == "department.created"
    ]

    assert len(department_events) == len(DEPARTMENTS)
    assert [event.department_name for event in department_events] == [
        department_name for _, department_name, _ in DEPARTMENTS
    ]
    assert all(event.organization_id == ORGANIZATION_ID for event in department_events)
    assert all(event.status == "active" for event in department_events)
