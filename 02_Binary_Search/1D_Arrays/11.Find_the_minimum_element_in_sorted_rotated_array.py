# QUESTION:
# Find the minimum element in a rotated sorted array
# containing distinct elements.

# APPROACH:
# Compare the middle element with the rightmost element.
# If nums[mid] > nums[right], the minimum lies to the right.
# Otherwise, it lies at mid or to the left.

def find_min(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must not be empty")

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


# CODE:
# print(find_min([4, 5, 6, 7, 0, 1, 2]))  # 0

# TIME COMPLEXITY = O(log N)
# SPACE COMPLEXITY = O(1)
