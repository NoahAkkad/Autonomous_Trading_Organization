"""Strongly typed textual value aliases for the organization domain."""

from typing import NewType

DepartmentCode = NewType("DepartmentCode", str)
DomainName = NewType("DomainName", str)
