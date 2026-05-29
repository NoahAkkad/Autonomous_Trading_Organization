"""Domain-only validation helpers."""

from collections.abc import Sized
from typing import TypeVar

T = TypeVar("T", bound=Sized)


def require_present(value: T, field_name: str) -> T:
    """Require a domain value to be present without depending on infrastructure."""
    if len(value) == 0:
        raise ValueError(f"{field_name} must be present")
    return value
