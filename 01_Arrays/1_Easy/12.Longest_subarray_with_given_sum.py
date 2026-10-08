"""
QUESTION:-
Given an array A of size N and an integer K, return the length of the longest
subarray whose sum equals K.

Example:
Input:
A = [1, 2, 3, 1, 1, 1, 1]
K = 3

Output:
3

Explanation:
The longest valid subarray can be [1, 1, 1].
"""

"""
APPROACH:-
-> Use a sliding window with two pointers.
-> Expand the right side and add each new element to the current sum.
-> While the sum is greater than K, move the left pointer and subtract.
-> Whenever the sum equals K, update the maximum window length.

IMPORTANT:
This O(N) sliding-window solution is correct when the array contains only
non-negative values, which is the condition used by the common A2Z version.

For arrays that may contain negative values, use a prefix-sum + hash map approach.
"""

# CODE:-

def longest_subarray_with_sum_k(nums: list[int], k: int) -> int:
    """Return longest subarray length with sum k for non-negative nums."""
    left = 0
    current_sum = 0
    best = 0

    for right, value in enumerate(nums):
        current_sum += value

        while left <= right and current_sum > k:
            current_sum -= nums[left]
            left += 1

        if current_sum == k:
            best = max(best, right - left + 1)

    return best


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
