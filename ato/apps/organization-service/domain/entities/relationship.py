"""Relationship domain entity."""

from dataclasses import dataclass

from ..enums import RelationshipType
from ..exceptions import InvalidRelationship
from ..value_objects import AgentId, RelationshipId
from ..value_objects.validation import require_present


@dataclass(frozen=True, slots=True, kw_only=True)
class Relationship:
    relationship_id: RelationshipId
    source_agent_id: AgentId
    target_agent_id: AgentId
    relationship_type: RelationshipType

    def __post_init__(self) -> None:
        require_present(self.relationship_id, "relationship_id")
        require_present(self.source_agent_id, "source_agent_id")
        require_present(self.target_agent_id, "target_agent_id")
        if self.source_agent_id == self.target_agent_id:
            raise InvalidRelationship("source_agent_id and target_agent_id must differ")
