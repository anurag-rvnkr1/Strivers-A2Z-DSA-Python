# QUESTION:
# Given a rotated sorted array of distinct elements,
# find how many times it has been rotated.
# Example: [4, 5, 1, 2, 3] -> 2

# APPROACH:
# The minimum element's index gives the number of right rotations.
# Use binary search to locate the minimum element.

def count_rotations(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must not be empty")

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return left


# CODE:
# print(count_rotations([4, 5, 1, 2, 3]))  # 2
# print(count_rotations([1, 2, 3, 4, 5]))  # 0

# TIME COMPLEXITY = O(log N)
# SPACE COMPLEXITY = O(1)
