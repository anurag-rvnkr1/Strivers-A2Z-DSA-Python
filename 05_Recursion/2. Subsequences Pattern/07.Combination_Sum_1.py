# QUESTION:
# Given distinct positive integers candidates and a target,
# find all unique combinations that sum to the target.
#
# Each candidate can be used unlimited times.
#
# Example:
# candidates = [2, 3, 6, 7], target = 7
# Output = [[2, 2, 3], [7]]
#
# APPROACH:
# 1. Sort the candidates.
# 2. At each index, choose to include or exclude the candidate.
# 3. When including, keep the same index because reuse is allowed.
# 4. When excluding, move to the next index.
# 5. Stop when target becomes zero or negative.


def combination_sum(
    candidates: list[int],
    target: int
) -> list[list[int]]:

    candidates = sorted(candidates)

    if any(value <= 0 for value in candidates):
        raise ValueError("Candidates must be positive integers")

    result = []
    current = []

    def solve(index: int, remaining: int) -> None:
        if remaining == 0:
            result.append(current.copy())
            return

        if index == len(candidates) or remaining < 0:
            return

        # Include candidate: same index allows reuse.
        current.append(candidates[index])
        solve(index, remaining - candidates[index])

        # Backtrack.
        current.pop()

        # Exclude candidate.
        solve(index + 1, remaining)

    solve(0, target)

    return result


# CODE:
# print(combination_sum([2, 3, 6, 7], 7))
# Output: [[2, 2, 3], [7]]
#
# print(combination_sum([2, 3, 5], 8))
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


# TIME COMPLEXITY = Exponential
# Depends on candidate values and target.
# A loose bound for positive integer candidates is O(2^(target/min_candidate))
# up to polynomial factors.
#
# SPACE COMPLEXITY = O(target/min_candidate)
# Maximum recursion depth and current combination.
# Output storage is additional.
