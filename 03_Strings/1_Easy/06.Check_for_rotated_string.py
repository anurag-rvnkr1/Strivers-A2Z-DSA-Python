# QUESTION:
# Given two strings s and goal, check whether goal can be
# obtained by repeatedly moving the first character of s
# to the end.
# Example: s = "abcde", goal = "cdeab" -> True

# APPROACH:
# If both strings have equal length, concatenate s with itself.
# Every possible rotation of s must appear as a substring of s + s.

def rotate_string(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    return goal in (s + s)


# CODE:
# print(rotate_string("abcde", "cdeab"))  # True
# print(rotate_string("abcde", "abced"))  # False
# print(rotate_string("", ""))            # True

# TIME COMPLEXITY = O(N^2) worst case for substring search
# SPACE COMPLEXITY = O(N)
