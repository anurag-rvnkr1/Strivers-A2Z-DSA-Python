"""
QUESTION:-
Given an integer array nums, rotate it left or right by k positions.

Example:
Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3

Right rotation -> [5, 6, 7, 1, 2, 3, 4]
Left rotation  -> [4, 5, 6, 7, 1, 2, 3]

LeetCode's "Rotate Array" specifically asks for right rotation.
"""

"""
APPROACH:-

Right rotation by k:
-> Normalize k using k % n.
-> Reverse the first n-k elements.
-> Reverse the last k elements.
-> Reverse the entire array.

Left rotation by k:
-> Normalize k using k % n.
-> Reverse the first k elements.
-> Reverse the remaining n-k elements.
-> Reverse the entire array.

This uses the reversal algorithm and works in-place.
"""

# CODE:-

def _reverse(nums: list[int], left: int, right: int) -> None:
    """Reverse nums[left:right+1] in-place."""
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def right_rotate(nums: list[int], k: int) -> None:
    """Rotate nums to the right by k positions in-place."""
    n = len(nums)

    if n == 0:
        return

    k %= n

    if k == 0:
        return

    _reverse(nums, 0, n - k - 1)
    _reverse(nums, n - k, n - 1)
    _reverse(nums, 0, n - 1)


def left_rotate(nums: list[int], k: int) -> None:
    """Rotate nums to the left by k positions in-place."""
    n = len(nums)

    if n == 0:
        return

    k %= n

    if k == 0:
        return

    _reverse(nums, 0, k - 1)
    _reverse(nums, k, n - 1)
    _reverse(nums, 0, n - 1)


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
