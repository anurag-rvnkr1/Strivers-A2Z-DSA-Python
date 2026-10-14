"""
QUESTION:-

Given an array of integers nums and an integer k, return the total number
of subarrays whose sum equals k.

Example:
Input:
nums = [1, 1, 1]
k = 2

Output:
2

Explanation:
The subarrays [1, 1] at indices [0, 1] and [1, 2] both have sum 2.
"""

"""
APPROACH:-

Use prefix sum + hash map.

Suppose the current prefix sum is:

    prefix_sum

We need an earlier prefix sum equal to:

    prefix_sum - k

because:

    prefix_sum - previous_prefix = k

-> Store the frequency of every prefix sum in a hash map.
-> Initialize prefix_sum 0 with frequency 1.
-> Traverse the array.
-> Add the current number to prefix_sum.
-> If prefix_sum - k exists, add its frequency to the answer.
-> Store the current prefix_sum.

This works even when the array contains negative numbers.
"""

# CODE:-

def subarray_sum(nums: list[int], k: int) -> int:
    prefix_sum = 0
    count = 0

    prefix_frequency = {0: 1}

    for num in nums:
        prefix_sum += num

        count += prefix_frequency.get(prefix_sum - k, 0)

        prefix_frequency[prefix_sum] = (
            prefix_frequency.get(prefix_sum, 0) + 1
        )

    return count


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(N)
