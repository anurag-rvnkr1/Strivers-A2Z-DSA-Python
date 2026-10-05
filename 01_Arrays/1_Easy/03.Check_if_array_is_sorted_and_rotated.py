"""
QUESTION:-
Given an array nums, return True if the array was originally sorted in
non-decreasing order and then rotated any number of positions.

Duplicates may be present.

Example 1:
Input:  nums = [3, 4, 5, 1, 2]
Output: True

Example 2:
Input:  nums = [2, 1, 3, 4]
Output: False
"""

"""
APPROACH:-
-> In a sorted-and-rotated array, there can be at most one position where
   nums[i] > nums[i + 1].
-> The last element and the first element are also adjacent because the array
   is circular.
-> Count these descending transitions.
-> If the count is 0 or 1, the array is valid; otherwise it is not.

This is the circular-order approach used by LeetCode.
"""

# CODE:-

def check(nums: list[int]) -> bool:
    """Return whether nums is sorted in non-decreasing order after rotation."""
    n = len(nums)

    if n <= 1:
        return True

    drops = 0

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            drops += 1

            if drops > 1:
                return False

    return True


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
