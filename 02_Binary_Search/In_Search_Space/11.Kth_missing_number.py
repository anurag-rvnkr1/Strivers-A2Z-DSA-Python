# QUESTION:
# Given a strictly increasing sorted array of positive integers,
# return the kth missing positive integer.
# Example: arr = [2, 3, 4, 7, 11], k = 5 -> 9

# APPROACH:
# Missing numbers before index i = arr[i] - (i + 1).
# Binary search for the first index where missing count >= k.
# Derive the answer from the boundary.

def find_kth_positive(arr: list[int], k: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        missing = arr[mid] - (mid + 1)

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1

    return left + k


# CODE:
# print(find_kth_positive([2, 3, 4, 7, 11], 5))  # 9

# TIME COMPLEXITY = O(log N)
# SPACE COMPLEXITY = O(1)
