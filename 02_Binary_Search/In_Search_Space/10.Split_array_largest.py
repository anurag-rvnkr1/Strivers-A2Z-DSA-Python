# QUESTION:
# Split an array into k non-empty contiguous subarrays.
# Minimize the largest subarray sum.
# Example: nums = [7, 2, 5, 10, 8], k = 2 -> 18

# APPROACH:
# Binary search the maximum allowed subarray sum.
# Greedily create subarrays without exceeding that limit.
# The candidate is feasible when no more than k subarrays are needed.

def split_array(nums: list[int], k: int) -> int:
    if not nums or k <= 0 or k > len(nums):
        return -1

    def can_split(limit: int) -> bool:
        parts = 1
        current_sum = 0

        for num in nums:
            if current_sum + num > limit:
                parts += 1
                current_sum = num
            else:
                current_sum += num

            if parts > k:
                return False

        return True

    left, right = max(nums), sum(nums)

    while left <= right:
        mid = (left + right) // 2

        if can_split(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


# CODE:
# print(split_array([7, 2, 5, 10, 8], 2))  # 18

# TIME COMPLEXITY = O(N * log S)
# SPACE COMPLEXITY = O(1)
# S = sum of array elements
