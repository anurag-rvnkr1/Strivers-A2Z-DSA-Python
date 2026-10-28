# QUESTION:
# Given a sorted array and target x, return its index if found,
# otherwise return -1.

# APPROACH:
# Apply binary search by repeatedly halving the search interval.

def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# CODE:
# print(search([1, 3, 5, 7, 9], 7))  # 3

# TIME COMPLEXITY = O(log N)
# SPACE COMPLEXITY = O(1)
