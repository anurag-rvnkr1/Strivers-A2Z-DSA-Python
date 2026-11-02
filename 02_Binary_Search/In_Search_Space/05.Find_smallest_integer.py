# QUESTION:
# Find the smallest positive divisor such that the sum of
# ceiling(nums[i] / divisor) for all elements is <= threshold.
# Example: nums = [1, 2, 5, 9], threshold = 6 -> 5

# APPROACH:
# Binary search the divisor from 1 to max(nums).
# For each divisor, calculate the sum of ceiling divisions.
# Find the smallest divisor satisfying the threshold.

def smallest_divisor(nums: list[int], threshold: int) -> int:
    if not nums or threshold < len(nums):
        return -1

    left, right = 1, max(nums)

    while left <= right:
        mid = (left + right) // 2

        total = sum(
            (num + mid - 1) // mid for num in nums
        )

        if total <= threshold:
            right = mid - 1
        else:
            left = mid + 1

    return left


# CODE:
# print(smallest_divisor([1, 2, 5, 9], 6))  # 5

# TIME COMPLEXITY = O(N * log M)
# SPACE COMPLEXITY = O(1)
# M = maximum element in nums
