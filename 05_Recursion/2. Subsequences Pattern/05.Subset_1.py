# QUESTION:
# Given an array of N integers, generate the sum of every
# possible subset.
#
# Return all subset sums in ascending order.
#
# Example:
# Input: [2, 3]
# Output: [0, 2, 3, 5]
#
# APPROACH:
# 1. Recursively process each array element.
# 2. Include the element in the current sum.
# 3. Exclude the element from the current sum.
# 4. When all elements are processed, store the sum.
# 5. Sort all resulting sums.


def subset_sums(arr: list[int]) -> list[int]:
    result = []
    n = len(arr)

    def solve(index: int, current_sum: int) -> None:
        if index == n:
            result.append(current_sum)
            return

        # Include current element.
        solve(index + 1, current_sum + arr[index])

        # Exclude current element.
        solve(index + 1, current_sum)

    solve(0, 0)

    return sorted(result)


# CODE:
# print(subset_sums([2, 3]))       # [0, 2, 3, 5]
# print(subset_sums([1, 2, 3]))    # [0, 1, 2, 3, 3, 4, 5, 6]
# print(subset_sums([]))           # [0]


# TIME COMPLEXITY = O(N * 2^N)
# 2^N subset sums are generated and then sorted.
# Sorting takes O(2^N * N).
#
# SPACE COMPLEXITY = O(N) auxiliary recursion depth.
# Output storage is O(2^N).
