"""
QUESTION:-
Given a non-empty array nums, every element appears twice except for one.
Find the element that appears only once.

The solution must run in linear time and use constant extra space.

Example 1:
Input:  nums = [2, 2, 1]
Output: 1

Example 2:
Input:  nums = [4, 1, 2, 1, 2]
Output: 4
"""

"""
APPROACH:-
-> XOR has two important properties:
   x ^ x = 0
   x ^ 0 = x

-> XOR every element in the array.
-> All duplicated values cancel each other.
-> The value left in the accumulator is the element that appears once.

This is the optimal O(N) / O(1) solution for LeetCode 136.
"""

# CODE:-

def single_number(nums: list[int]) -> int:
    """Return the unique element when every other element appears twice."""
    xor_result = 0

    for num in nums:
        xor_result ^= num

    return xor_result


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
