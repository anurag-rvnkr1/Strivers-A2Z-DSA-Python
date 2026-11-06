# QUESTION:
# Given two sorted arrays, find the kth element in
# their combined sorted order. k uses 1-based indexing.
# Example:
# arr1 = [2, 3, 6, 7, 9]
# arr2 = [1, 4, 8, 10]
# k = 5
# Output: 6

# APPROACH:
# Binary search the partition of the smaller array.
# Select exactly k elements on the left side.
# Find a valid partition where left-side elements
# are <= right-side elements.
# The kth element is the maximum of the left-side values.

def kth_element(
    arr1: list[int], arr2: list[int], k: int
) -> int:
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    n, m = len(arr1), len(arr2)

    if k < 1 or k > n + m:
        raise ValueError("k must be between 1 and the total array length")

    left = max(0, k - m)
    right = min(k, n)

    while left <= right:
        cut1 = (left + right) // 2
        cut2 = k - cut1

        left1 = arr1[cut1 - 1] if cut1 > 0 else float("-inf")
        right1 = arr1[cut1] if cut1 < n else float("inf")

        left2 = arr2[cut2 - 1] if cut2 > 0 else float("-inf")
        right2 = arr2[cut2] if cut2 < m else float("inf")

        if left1 <= right2 and left2 <= right1:
            return int(max(left1, left2))

        elif left1 > right2:
            right = cut1 - 1
        else:
            left = cut1 + 1

    raise ValueError("Input arrays must be sorted")


# CODE:
# print(kth_element([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))  # 6

# TIME COMPLEXITY = O(log(min(N, M)))
# SPACE COMPLEXITY = O(1)
