# QUESTION:
# Search target in a rotated sorted array with distinct elements.
# Return its index, or -1 if it is absent.

# APPROACH:
# At each step, identify which half is sorted.
# Decide whether target lies in that half.

def search_rotated(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# CODE:
# print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # 4

# TIME COMPLEXITY = O(log N)
# SPACE COMPLEXITY = O(1)
