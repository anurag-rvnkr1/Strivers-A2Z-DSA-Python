# QUESTION:
# Given an array of non-negative integers and a target sum K,
# count all subsets whose sum equals K.
#
# Return the answer modulo 10^9 + 7.
#
# Example:
# Input: arr = [2, 3, 5, 6, 8, 10], K = 10
# Output: 3
#
# Valid subsets:
# [2, 3, 5], [2, 8], [10]
#
# APPROACH:
# 1. At each index, consider including the element.
# 2. Also consider excluding the element.
# 3. When all elements are processed, count the subset
#    if its sum equals the target.
#
# Memoization avoids recalculating the same states.


from functools import lru_cache

MOD = 10**9 + 7


def perfect_sum(arr: list[int], target: int) -> int:
    n = len(arr)

    @lru_cache(maxsize=None)
    def solve(index: int, remaining: int) -> int:
        if index == n:
            return 1 if remaining == 0 else 0

        # Exclude current element.
        exclude = solve(index + 1, remaining)

        # Include current element.
        include = 0
        if arr[index] <= remaining:
            include = solve(index + 1, remaining - arr[index])

        return (include + exclude) % MOD

    return solve(0, target)


# CODE:
# print(perfect_sum([2, 3, 5, 6, 8, 10], 10))  # 3
# print(perfect_sum([1, 2, 3], 3))             # 2
# print(perfect_sum([0, 0, 1], 1))             # 4
# print(perfect_sum([], 0))                    # 1


# TIME COMPLEXITY = O(N * K)
# At most N * (K + 1) memoized states.
#
# SPACE COMPLEXITY = O(N * K)
# Memoization cache and recursive call stack.
