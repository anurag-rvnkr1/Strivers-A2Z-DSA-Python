# QUESTION:
# Reverse the order of words in a string.
# Remove leading, trailing, and extra spaces.
# Separate the resulting words using exactly one space.
# Example: "  the sky  is blue  " -> "blue is sky the"

# APPROACH:
# Split the string into words, reverse their order,
# and join them with a single space.

def reverse_words(s: str) -> str:
    words = s.split()
    return " ".join(reversed(words))


# CODE:
# print(reverse_words("the sky is blue"))  # "blue is sky the"
# print(reverse_words("  hello world  "))  # "world hello"
# print(reverse_words("a good   example")) # "example good a"

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(N)
