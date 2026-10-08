"""
QUESTION:-
Given an array nums containing n distinct numbers in the range [0, n], return
the only number in the range that is missing.

Example 1:
Input:  nums = [3, 0, 1]
Output: 2

Example 2:
Input:  nums = [0, 1]
Output: 2
"""

"""
APPROACH:-
-> The numbers from 0 to n have an expected sum of n * (n + 1) // 2.
-> Calculate the actual sum of the elements.
-> The difference between expected and actual sums is the missing number.

An XOR solution is also possible, but the arithmetic version is concise.
"""

# CODE:-

def missing_number(nums: list[int]) -> int:
    """Return the missing number from the range [0, n]."""
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
