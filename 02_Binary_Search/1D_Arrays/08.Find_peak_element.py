# QUESTION:
# Find an index of a peak element.
# A peak is strictly greater than its existing neighbors.
# Assume adjacent elements are unequal.

# APPROACH:
# If nums[mid] < nums[mid + 1], a peak exists to the right.
# Otherwise, a peak exists at mid or to the left.

def find_peak_element(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must not be empty")

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


# CODE:
# print(find_peak_element([1, 2, 3, 1]))  # 2

# TIME COMPLEXITY = O(log N)
# SPACE COMPLEXITY = O(1)
