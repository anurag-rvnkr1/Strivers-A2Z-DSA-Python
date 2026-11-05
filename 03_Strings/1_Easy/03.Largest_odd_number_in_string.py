# QUESTION:
# Given a string representing a large positive integer,
# return the largest-valued odd-number substring.
# The substring must start from the beginning of the string.
# Return an empty string if no odd number exists.
# Example: "35427" -> "35427"
# Example: "4206" -> ""

# APPROACH:
# Scan from right to left to find the last odd digit.
# Return the substring from the beginning through that digit.

def largest_odd_number(num: str) -> str:
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[:i + 1]

    return ""


# CODE:
# print(largest_odd_number("35427"))  # "35427"
# print(largest_odd_number("4206"))   # ""

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(N) for the returned substring
