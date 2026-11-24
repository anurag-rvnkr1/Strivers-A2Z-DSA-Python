# QUESTION:
# Given a string of lowercase English letters, count the
# number of distinct non-empty substrings.
#
# Note:
# The reference filename says "substrings", but its actual
# implementation generates distinct SUBSEQUENCES, including
# the empty subsequence.
#
# Example:
# Input: "gfg"
# Distinct subsequences:
# "", "g", "f", "gf", "fg", "gg", "gfg"
# Output: 7
#
# APPROACH:
# 1. Recursively process each character.
# 2. Include the current character.
# 3. Exclude the current character.
# 4. Store generated subsequences in a set.
# 5. Return the number of distinct subsequences modulo 10^9+7.
#
# This deliberately follows the source implementation.


MOD = 10**9 + 7


def count_distinct_subsequences(s: str) -> int:
    distinct = set()

    def solve(index: int, current: str) -> None:
        if index == len(s):
            distinct.add(current)
            return

        # Include current character.
        solve(index + 1, current + s[index])

        # Exclude current character.
        solve(index + 1, current)

    solve(0, "")

    return len(distinct) % MOD


# CODE:
# print(count_distinct_subsequences("gfg"))  # 7
# print(count_distinct_subsequences("aaa"))  # 4
# print(count_distinct_subsequences(""))     # 1 (empty subsequence)


# TIME COMPLEXITY = O(N * 2^N) approximately
# Up to 2^N subsequences are generated and stored.
# String creation and hashing can take O(N).
#
# SPACE COMPLEXITY = O(N * 2^N)
# Set stores distinct generated subsequences.
