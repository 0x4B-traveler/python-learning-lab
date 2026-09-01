"""A simple dynamic array implementation backed by ``ctypes``."""

from __future__ import annotations

import ctypes
from typing import Any


class DynamicArray:
    def __init__(self) -> None:
        self._size = 0  # 实际元素个数。
        self._capacity = 1  # 初始容量设为 1。
        self._array = self._make_array(self._capacity)

    def _make_array(self, capacity: int) -> Any:
        """创建使用连续内存的底层数组。"""
        return (capacity * ctypes.py_object)()

    def _resize(self, new_capacity: int) -> None:
        """申请新内存，复制数据，并释放旧数组。"""
        new_array = self._make_array(new_capacity)
        for index in range(self._size):
            new_array[index] = self._array[index]
        self._array = new_array
        self._capacity = new_capacity

    def append(self, item: Any) -> None:
        """在末尾添加元素，时间复杂度均摊为 O(1)。"""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)

        self._array[self._size] = item
        self._size += 1

    def pop(self) -> Any:
        """弹出末尾元素，时间复杂度为 O(1)，并按需缩容。"""
        if self._size == 0:
            raise IndexError("pop from empty array")

        popped_item = self._array[self._size - 1]
        self._size -= 1

        # 缩容策略：size 降至 capacity 的 1/4 时，容量减半。
        # 使用 1/4 可以避免在临界点反复 push/pop 造成性能抖动。
        if self._size <= self._capacity // 4:
            new_capacity = max(1, self._capacity // 2)
            self._resize(new_capacity)

        return popped_item

    def __getitem__(self, index: int) -> Any:
        """按索引访问元素，例如 ``array[0]``。"""
        if not 0 <= index < self._size:
            raise IndexError("index out of bounds")
        return self._array[index]

    def __setitem__(self, index: int, value: Any) -> None:
        """按索引修改元素，例如 ``array[0] = 10``。"""
        if not 0 <= index < self._size:
            raise IndexError("index out of bounds")
        self._array[index] = value

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        elements = [str(self._array[index]) for index in range(self._size)]
        return "[" + ", ".join(elements) + "]"


if __name__ == "__main__":
    array = DynamicArray()
    print(f"初始容量：{array._capacity}")

    # 测试扩容。
    for value in range(5):
        array.append(value)
        print(f"添加 {value} -> Size: {len(array)}, Capacity: {array._capacity}")

    print(array)

    # 测试缩容。
    for _ in range(4):
        print(f"弹出元素：{array.pop()} -> Size: {len(array)}, Capacity: {array._capacity}")
