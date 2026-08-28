"""A stack implemented with a Python list. Push and pop are O(1) amortized."""

from __future__ import annotations


class Stack:
    def __init__(self) -> None:
        self._items: list[object] = []

    def push(self, item: object) -> None:
        self._items.append(item)

    def pop(self) -> object:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)

    def __bool__(self) -> bool:
        return bool(self._items)


if __name__ == "__main__":
    stack = Stack()
    for value in ("first", "second", "third"):
        stack.push(value)
    while stack:
        print(stack.pop())

