# QUESTION:
# Given a collection of candidates and a target,
# find all unique combinations that sum to the target.
#
# Each candidate can be used only once.
# The input may contain duplicate values, but output combinations
# must be unique.
#
# Example:
# candidates = [10, 1, 2, 7, 6, 1, 5]
# target = 8
#
# Output:
# [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
#
# APPROACH:
# 1. Sort the candidates.
# 2. Use backtracking to select candidates.
# 3. Move to index + 1 after including an element.
# 4. Skip duplicate values at the same recursion level.
# 5. Stop when the remaining target reaches zero.


def combination_sum2(
    candidates: list[int],
    target: int
) -> list[list[int]]:

    candidates = sorted(candidates)

    result = []
    current = []

    def solve(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(current.copy())
            return

        for i in range(start, len(candidates)):
            # Skip duplicate choices at the same level.
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            value = candidates[i]

            if value > remaining:
                break

            current.append(value)

            # Each element can be used only once.
            solve(i + 1, remaining - value)

            current.pop()

    solve(0, target)

    return result


# CODE:
# print(combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))
# Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
#
# print(combination_sum2([2, 5, 2, 1, 2], 5))
# Output: [[1, 2, 2], [5]]


# TIME COMPLEXITY = O(2^N * N)
# Exponential subset exploration, with combination copying.
#
# SPACE COMPLEXITY = O(N)
# Recursion stack and current combination.
# Output storage is additional.
