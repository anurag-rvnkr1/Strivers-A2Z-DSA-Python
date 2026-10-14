"""
QUESTION:-

Given an integer array nums, find the subarray with the largest sum
and return its sum.

Example 1:
Input:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output:
6

Explanation:
The subarray [4, -1, 2, 1] has the largest sum = 6.

Example 2:
Input:
nums = [1]

Output:
1
"""

"""
APPROACH:-

Use Kadane's Algorithm.

-> Maintain current_sum representing the best subarray ending at the
   current position.
-> Add the current element to current_sum.
-> Update the maximum answer.
-> If current_sum becomes negative, reset it to zero because a negative
   prefix can only reduce the sum of a future subarray.

Important:
The answer is updated BEFORE resetting current_sum, so arrays containing
only negative numbers are handled correctly.
"""

# CODE:-

def max_sub_array(nums: list[int]) -> int:
    current_sum = 0
    best_sum = float("-inf")

    for num in nums:
        current_sum += num
        best_sum = max(best_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    return int(best_sum)


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
