# QUESTION:
# Find the length of the longest subarray whose sum is zero.
# Example: [15, -2, 2, -8, 1, 7, 10, 23] -> 5

# APPROACH:
# Track the prefix sum and store its first occurrence.
# If a prefix sum repeats, the elements between its occurrences
# sum to zero.

def max_len(nums: list[int]) -> int:
    first_index = {0: -1}
    prefix_sum = 0
    longest = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum in first_index:
            longest = max(longest, i - first_index[prefix_sum])
        else:
            first_index[prefix_sum] = i

    return longest


# CODE:
# print(max_len([15, -2, 2, -8, 1, 7, 10, 23]))  # 5

# TIME COMPLEXITY = O(N) average
# SPACE COMPLEXITY = O(N)
