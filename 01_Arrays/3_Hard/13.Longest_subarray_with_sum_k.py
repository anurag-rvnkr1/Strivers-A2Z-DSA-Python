# QUESTION:
# Find the length of the longest subarray with sum equal to k.
# The array may contain positive, negative, and zero values.
# Example: [10, 5, 2, 7, 1, 9], k = 15 -> 4

# APPROACH:
# Maintain a running prefix sum and store the first index
# at which each prefix sum appears. If prefix_sum - k has
# appeared before, the intervening subarray sums to k.

def longest_subarray_with_sum_k(nums: list[int], k: int) -> int:
    first_index = {0: -1}
    prefix_sum = 0
    longest = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum - k in first_index:
            longest = max(longest, i - first_index[prefix_sum - k])

        if prefix_sum not in first_index:
            first_index[prefix_sum] = i

    return longest


# CODE:
# print(longest_subarray_with_sum_k([10, 5, 2, 7, 1, 9], 15))  # 4

# TIME COMPLEXITY = O(N) average
# SPACE COMPLEXITY = O(N)
