"""
QUESTION:-
Given an integer array nums sorted in non-decreasing order, remove duplicates
in-place so each unique element appears exactly once.

Return the number of unique elements k. The first k positions of nums must
contain the unique values in their original relative order.

Example 1:
Input:  nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]

Example 2:
Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
"""

"""
APPROACH:-
-> Use a write pointer k for the position of the last unique element.
-> Start scanning from index 1.
-> Whenever nums[j] differs from nums[k], a new unique value is found.
-> Increment k and copy nums[j] into nums[k].
-> Return k + 1.

This is the standard two-pointer solution expected by LeetCode.
"""

# CODE:-

def remove_duplicates(nums: list[int]) -> int:
    """Remove duplicates in-place and return the number of unique values."""
    if not nums:
        return 0

    k = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[k]:
            k += 1
            nums[k] = nums[j]

    return k + 1


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
