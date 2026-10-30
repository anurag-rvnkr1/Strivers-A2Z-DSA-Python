# QUESTION:
# In a sorted array where every element appears twice except one,
# find the element that appears only once.
# Assume the array length is odd.

# APPROACH:
# Align the middle index to an even index.
# If nums[mid] == nums[mid + 1], the single element is farther right.
# Otherwise, it lies at mid or to the left.

def single_non_duplicate(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must not be empty")

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid

    return nums[left]


# CODE:
# print(single_non_duplicate([1, 1, 2, 3, 3, 4, 4]))  # 2

# TIME COMPLEXITY = O(log N)
# SPACE COMPLEXITY = O(1)
