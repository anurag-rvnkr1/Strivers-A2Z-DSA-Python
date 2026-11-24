# QUESTION:
# Given n pairs of parentheses, generate all combinations
# of well-formed parentheses.
#
# Example:
# Input: n = 3
# Output:
# ["((()))", "(()())", "(())()", "()(())", "()()()"]
#
# APPROACH:
# 1. Track the number of opening and closing parentheses.
# 2. Add '(' while open_count < n.
# 3. Add ')' only when close_count < open_count.
# 4. When both counts reach n, store the combination.


def generate_parenthesis(n: int) -> list[str]:
    result = []

    def solve(
        current: str,
        open_count: int,
        close_count: int
    ) -> None:

        if open_count == n and close_count == n:
            result.append(current)
            return

        if open_count < n:
            solve(current + "(", open_count + 1, close_count)

        if close_count < open_count:
            solve(current + ")", open_count, close_count + 1)

    solve("", 0, 0)

    return result


# CODE:
# print(generate_parenthesis(1))  # ["()"]
# print(generate_parenthesis(2))  # ["(())", "()()"]
# print(generate_parenthesis(3))
# ["((()))", "(()())", "(())()", "()(())", "()()()"]
# print(generate_parenthesis(0))  # [""]


# TIME COMPLEXITY = O(Cn * N)
# Cn is the nth Catalan number; N = 2*n characters per answer.
#
# SPACE COMPLEXITY = O(N) auxiliary recursion depth.
# Output storage is O(Cn * N).
