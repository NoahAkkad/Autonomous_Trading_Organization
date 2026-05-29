"""Rank domain entity."""

from dataclasses import dataclass

from ..exceptions import InvalidRank
from ..value_objects import DomainName, RankId
from ..value_objects.validation import require_present


@dataclass(frozen=True, slots=True, kw_only=True)
class Rank:
    rank_id: RankId
    rank_name: DomainName
    level: int

    def __post_init__(self) -> None:
        require_present(self.rank_id, "rank_id")
        require_present(self.rank_name, "rank_name")
        if self.level < 0:
            raise InvalidRank("level must be non-negative")
