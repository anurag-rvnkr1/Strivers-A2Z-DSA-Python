# QUESTION:
# Count the occurrences of a target in a sorted array.

# APPROACH:
# The count equals upper_bound(target) - lower_bound(target).

def count_occurrences(nums: list[int], target: int) -> int:
    def bound(strict: bool) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > target or (not strict and nums[mid] == target):
                right = mid
            else:
                left = mid + 1

        return left

    return bound(True) - bound(False)


# CODE:
# print(count_occurrences([1, 2, 2, 2, 4, 6], 2))  # 3
# print(count_occurrences([1, 2, 4, 6], 3))        # 0

# TIME COMPLEXITY = O(log N)
# SPACE COMPLEXITY = O(1)
