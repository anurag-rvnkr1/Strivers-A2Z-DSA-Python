# QUESTION:
# Check whether an array is sorted in non-decreasing order.

# APPROACH:
# Compare each element with its previous element.
# Equal adjacent elements are allowed.

def is_sorted(nums: list[int]) -> bool:
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False

    return True


# CODE:
# print(is_sorted([1, 2, 2, 4]))  # True
# print(is_sorted([1, 3, 2, 4]))  # False

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
