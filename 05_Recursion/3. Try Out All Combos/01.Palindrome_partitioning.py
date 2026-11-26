# QUESTION:
# Given a string s, partition it so that every substring
# in the partition is a palindrome.
# Return all possible palindrome partitions.
#
# Example:
# Input: "aab"
# Output: [["a", "a", "b"], ["aa", "b"]]
#
# APPROACH:
# 1. Start partitioning from index 0.
# 2. Try every possible substring starting at the current index.
# 3. Check whether the substring is a palindrome.
# 4. If valid, add it to the current partition.
# 5. Recursively partition the remaining string.
# 6. Backtrack after each recursive call.


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


def partition(s: str) -> list[list[str]]:
    result = []
    current = []

    def solve(start: int) -> None:
        if start == len(s):
            result.append(current.copy())
            return

        for end in range(start, len(s)):
            substring = s[start:end + 1]

            if is_palindrome(substring):
                current.append(substring)
                solve(end + 1)
                current.pop()

    solve(0)

    return result


# CODE:
# print(partition("aab"))
# Output: [["a", "a", "b"], ["aa", "b"]]
#
# print(partition("a"))
# Output: [["a"]]
#
# print(partition("aaa"))
# Output: [
#   ["a", "a", "a"],
#   ["a", "aa"],
#   ["aa", "a"],
#   ["aaa"]
# ]


# TIME COMPLEXITY = O(N * 2^N)
# There can be up to 2^(N-1) possible partitions.
# Checking substrings adds up to polynomial work.
#
# SPACE COMPLEXITY = O(N)
# Recursion depth and current partition, excluding output.
