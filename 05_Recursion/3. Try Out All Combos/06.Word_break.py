# QUESTION:
# Given a string s and a dictionary of words,
# determine whether s can be segmented into one or more
# dictionary words.
#
# Example:
# s = "leetcode"
# word_dict = ["leet", "code"]
# Output: True
#
# APPROACH:
# 1. Start from index zero.
# 2. Try every possible prefix of the remaining string.
# 3. If the prefix exists in the dictionary, recursively
#    process the remaining suffix.
# 4. Return True when the complete string is segmented.
# 5. Use memoization to avoid repeated states.


from functools import lru_cache


def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)

    if not s:
        return True

    max_length = max(map(len, words), default=0)

    @lru_cache(maxsize=None)
    def solve(index: int) -> bool:
        if index == len(s):
            return True

        end_limit = min(len(s), index + max_length)

        for end in range(index + 1, end_limit + 1):
            current_word = s[index:end]

            if current_word in words and solve(end):
                return True

        return False

    return solve(0)


# CODE:
# print(word_break("leetcode", ["leet", "code"]))  # True
# print(word_break("applepenapple", ["apple", "pen"]))  # True
# print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
# Output: False
#
# print(word_break("", []))  # True


# TIME COMPLEXITY = O(N^3) worst case
# There are O(N) memoized states, each testing O(N) substrings
# whose slicing and hashing can cost O(N).
# With bounded word length or optimized transitions, this can improve.
#
# SPACE COMPLEXITY = O(N + D)
# O(N) recursion/cache states, plus dictionary storage D.
