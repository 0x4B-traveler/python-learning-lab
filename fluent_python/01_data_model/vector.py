"""A small Vector example inspired by Fluent Python's data model chapter."""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Vector:
    x: float
    y: float

    def __repr__(self) -> str:
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    vector = Vector(3, 4)
    print(vector, abs(vector), bool(vector))
    print(vector + Vector(1, 2))

