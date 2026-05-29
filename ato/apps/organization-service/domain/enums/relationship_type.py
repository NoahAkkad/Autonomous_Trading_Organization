"""Agent relationship classifications."""

from enum import StrEnum


class RelationshipType(StrEnum):
    REPORTS_TO = "reports_to"
    SUPERVISES = "supervises"
    COLLABORATES_WITH = "collaborates_with"
