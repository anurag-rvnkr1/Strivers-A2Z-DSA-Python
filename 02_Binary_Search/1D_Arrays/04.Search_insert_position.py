# QUESTION:
# Return the index where target is found in a sorted array.
# If absent, return the index where it should be inserted.

# APPROACH:
# Find the first index where nums[index] >= target.

def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left


# CODE:
# print(search_insert([1, 3, 5, 6], 5))  # 2
# print(search_insert([1, 3, 5, 6], 2))  # 1

# TIME COMPLEXITY = O(log N)
# SPACE COMPLEXITY = O(1)
