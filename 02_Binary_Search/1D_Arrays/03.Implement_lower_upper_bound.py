# QUESTION:
# Implement lower bound and upper bound for a sorted array.
# Lower bound: first index with value >= target.
# Upper bound: first index with value > target.

# APPROACH:
# Use binary search to find the first index satisfying
# each respective condition.

def lower_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left


def upper_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left


# CODE:
# nums = [1, 2, 2, 2, 4, 6]
# print(lower_bound(nums, 2))  # 1
# print(upper_bound(nums, 2))  # 4

# TIME COMPLEXITY = O(log N) per function
# SPACE COMPLEXITY = O(1)
