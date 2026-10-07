"""
QUESTION:-
Given an integer array nums, move all 0s to the end while maintaining the
relative order of all non-zero elements.

The operation must be performed in-place.

Example 1:
Input:  nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Example 2:
Input:  nums = [0]
Output: [0]
"""

"""
APPROACH:-
-> Maintain a write pointer for the next position that should contain a
   non-zero value.
-> Traverse the array and whenever a non-zero value is found, swap it into
   the write position.
-> Advance the write pointer.
-> This keeps all non-zero elements in their original relative order and
   pushes zeros toward the end.

This is the standard in-place two-pointer solution for LeetCode 283.
"""

# CODE:-

def move_zeroes(nums: list[int]) -> None:
    """Move all zeroes to the end of nums in-place."""
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
