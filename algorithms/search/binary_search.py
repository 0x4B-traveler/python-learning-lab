"""Binary search on a sorted sequence: O(log n) time and O(1) space."""

from __future__ import annotations


def binary_search(values: list[int], target: int) -> int:
    left, right = 0, len(values) - 1
    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11]
    print(binary_search(numbers, 7))
    print(binary_search(numbers, 8))

