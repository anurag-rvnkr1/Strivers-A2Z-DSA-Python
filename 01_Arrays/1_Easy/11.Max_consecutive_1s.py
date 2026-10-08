"""
QUESTION:-
Given a binary array nums, find the maximum number of consecutive 1s.

Example:
Input:  nums = [1, 1, 0, 1, 1, 1]
Output: 3
"""

"""
APPROACH:-
-> Keep a running count of the current consecutive 1s.
-> When the current value is 1, increment the count.
-> When it is 0, reset the count to zero.
-> Track the maximum count seen so far.

This is the standard one-pass solution for LeetCode 485.
"""

# CODE:-

def find_max_consecutive_ones(nums: list[int]) -> int:
    """Return the maximum number of consecutive 1s in nums."""
    current = 0
    best = 0

    for num in nums:
        if num == 1:
            current += 1
            best = max(best, current)
        else:
            current = 0

    return best


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
