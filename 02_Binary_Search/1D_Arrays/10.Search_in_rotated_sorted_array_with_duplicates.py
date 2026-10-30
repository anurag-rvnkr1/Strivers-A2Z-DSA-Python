# QUESTION:
# Search target in a rotated sorted array that may contain duplicates.
# Return True if target exists, otherwise False.

# APPROACH:
# Use binary search. When left, middle, and right values are equal,
# shrink both boundaries because the sorted half is ambiguous.

def search_rotated_duplicates(nums: list[int], target: int) -> bool:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True

        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False


# CODE:
# print(search_rotated_duplicates([2, 5, 6, 0, 0, 1, 2], 0))  # True
# print(search_rotated_duplicates([2, 5, 6, 0, 0, 1, 2], 3))  # False

# TIME COMPLEXITY = O(log N) average; O(N) worst case
# SPACE COMPLEXITY = O(1)
