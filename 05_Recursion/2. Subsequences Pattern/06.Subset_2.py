# QUESTION:
# Given an array that may contain duplicate elements,
# return all possible unique subsets.
#
# Example:
# Input: [1, 2, 2]
# Output:
# [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
#
# APPROACH:
# 1. Sort the array.
# 2. Use recursive backtracking.
# 3. At every recursion level, choose an element.
# 4. Skip equal elements at the same recursion level.
# 5. Store every constructed subset.


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums.sort()

    result = []
    current = []

    def solve(start: int) -> None:
        result.append(current.copy())

        for i in range(start, len(nums)):
            # Skip duplicate choices at the same recursion level.
            if i > start and nums[i] == nums[i - 1]:
                continue

            current.append(nums[i])
            solve(i + 1)

            # Backtrack.
            current.pop()

    solve(0)

    return result


# CODE:
# print(subsets_with_dup([1, 2, 2]))
# print(subsets_with_dup([0]))
# print(subsets_with_dup([1, 1, 1]))


# TIME COMPLEXITY = O(N * 2^N)
# Subsets are generated and copied; sorting initially costs O(N log N).
#
# SPACE COMPLEXITY = O(N) auxiliary recursion/current subset.
# Output storage can be O(N * 2^N).
