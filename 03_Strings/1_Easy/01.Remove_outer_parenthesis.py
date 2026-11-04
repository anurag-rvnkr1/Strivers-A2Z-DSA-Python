# QUESTION:
# Given a valid parentheses string, remove the outermost
# parentheses of every primitive substring.
# Example: "(()())(())" -> "()()()"

# APPROACH:
# Track the current nesting depth.
# Add '(' only when already inside a primitive.
# Add ')' only when it does not close the outermost pair.

def remove_outer_parentheses(s: str) -> str:
    result = []
    depth = 0

    for char in s:
        if char == '(':
            if depth > 0:
                result.append(char)
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                result.append(char)

    return "".join(result)


# CODE:
# print(remove_outer_parentheses("(()())(())"))  # "()()()"
# print(remove_outer_parentheses("(()())(())(()(()))"))  # "()()()()(())"

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(N)
