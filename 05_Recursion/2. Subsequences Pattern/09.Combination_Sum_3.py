# QUESTION:
# Find all combinations of k distinct numbers from 1 to 9
# whose sum equals n.
#
# Each number can be used at most once.
#
# Example:
# Input: k = 3, n = 7
# Output: [[1, 2, 4]]
#
# APPROACH:
# 1. Start with numbers from 1 to 9.
# 2. Choose or skip each number.
# 3. Move forward after selecting a number.
# 4. Stop when k numbers have been selected.
# 5. Store the combination only when its sum equals n.


def combination_sum3(k: int, n: int) -> list[list[int]]:
    result = []
    current = []

    def solve(start: int, remaining: int) -> None:
        if len(current) == k:
            if remaining == 0:
                result.append(current.copy())
            return

        if remaining <= 0:
            return

        for value in range(start, 10):
            if value > remaining:
                break

            current.append(value)
            solve(value + 1, remaining - value)
            current.pop()

    solve(1, n)

    return result


# CODE:
# print(combination_sum3(3, 7))   # [[1, 2, 4]]
# print(combination_sum3(3, 9))   # [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
# print(combination_sum3(4, 1))   # []


# TIME COMPLEXITY = O(2^9)
# At most 9 numbers are explored.
#
# SPACE COMPLEXITY = O(K)
# Recursion depth and current combination.
# Output storage is additional.
