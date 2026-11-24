# QUESTION:
# Given an array of unique elements, return all possible subsets.
#
# Example:
# Input: [1, 2, 3]
# Output:
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
#
# APPROACH:
# For every element, make two recursive choices:
# 1. Include the current element.
# 2. Exclude the current element.
# Store the subset when all elements have been processed.


def subsets(nums: list[int]) -> list[list[int]]:
    result = []
    current = []

    def solve(index: int) -> None:
        if index == len(nums):
            result.append(current.copy())
            return

        # Include current element.
        current.append(nums[index])
        solve(index + 1)

        # Backtrack.
        current.pop()

        # Exclude current element.
        solve(index + 1)

    solve(0)

    return result


# CODE:
# print(subsets([1, 2, 3]))
# print(subsets([0]))  # [[], [0]]
# print(subsets([]))   # [[]]


# TIME COMPLEXITY = O(N * 2^N)
# There are 2^N subsets, and copying each subset takes O(N).
#
# SPACE COMPLEXITY = O(N) auxiliary recursion/current subset.
# Output storage is O(N * 2^N).
