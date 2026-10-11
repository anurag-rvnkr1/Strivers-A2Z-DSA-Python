"""
QUESTION:-

You are given a 0-indexed integer array nums of even length containing
an equal number of positive and negative integers.

Rearrange the array so that:

-> Every consecutive pair has opposite signs.
-> The relative order of positive numbers is preserved.
-> The relative order of negative numbers is preserved.
-> The array starts with a positive number.

Example:
Input:
nums = [3, 1, -2, -5, 2, -4]

Output:
[3, -2, 1, -5, 2, -4]
"""

"""
APPROACH:-

-> Create an answer array of the same size.
-> Positive numbers go to indices:
      0, 2, 4, ...
-> Negative numbers go to indices:
      1, 3, 5, ...
-> Maintain two pointers:
      positive_index
      negative_index
-> Traverse the original array once.
-> Place each value into its appropriate position.

Because we process positive and negative values from left to right,
their relative ordering is automatically preserved.
"""

# CODE:-

def rearrange_array(nums: list[int]) -> list[int]:
    result = [0] * len(nums)

    positive_index = 0
    negative_index = 1

    for num in nums:
        if num > 0:
            result[positive_index] = num
            positive_index += 2
        else:
            result[negative_index] = num
            negative_index += 2

    return result


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(N)
