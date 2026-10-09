"""
QUESTION:-

Given an array of integers nums and an integer target, return the indices
of the two numbers such that they add up to target.

You may assume that each input has exactly one solution, and you may not
use the same element twice.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9
"""

"""
APPROACH:-

-> Use a hash map to store each number and its index.
-> For every element, calculate its complement:
      complement = target - current
-> If the complement already exists in the hash map, we found the answer.
-> Otherwise, store the current number and its index.
-> Return the two indices.

This is the optimal hash-map solution for LeetCode 1.
"""

# CODE:-

def two_sum(nums: list[int], target: int) -> list[int]:
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index:
            return [num_to_index[complement], i]

        num_to_index[num] = i

    return [-1, -1]


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(N)
