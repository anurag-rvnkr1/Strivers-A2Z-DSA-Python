# QUESTION:
# Given two strings s and t, determine whether they are isomorphic.
# Each character in s must map consistently to one character in t.
# No two different characters can map to the same character.
# Example: s = "egg", t = "add" -> True
# Example: s = "foo", t = "bar" -> False

# APPROACH:
# Maintain two dictionaries:
# 1. Mapping from s to t.
# 2. Mapping from t to s.
# Check both mappings to guarantee a one-to-one relationship.

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_s_to_t = {}
    map_t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False
        else:
            map_s_to_t[char_s] = char_t

        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return False
        else:
            map_t_to_s[char_t] = char_s

    return True


# CODE:
# print(is_isomorphic("egg", "add"))  # True
# print(is_isomorphic("foo", "bar"))  # False
# print(is_isomorphic("paper", "title"))  # True

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(K)
# K = number of distinct characters
