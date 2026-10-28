# QUESTION:
# Return the first index i where nums[i] >= target.
# If no such index exists, return len(nums).

# APPROACH:
# Binary search for the first element greater than or equal to target.

def lower_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left


# CODE:
# print(lower_bound([1, 2, 2, 4, 6], 2))  # 1
# print(lower_bound([1, 2, 4, 6], 3))     # 2

# TIME COMPLEXITY = O(log N)
# SPACE COMPLEXITY = O(1)
