# QUESTION:
# Sort a stack using recursion such that the greatest
# element is at the top.
#
# Example:
# Input:  [11, 2, 32, 3, 41]
# Output: [2, 3, 11, 32, 41]
#
# Here, the rightmost element is the stack top.
#
# APPROACH:
# 1. Pop the top element.
# 2. Recursively sort the remaining stack.
# 3. Insert the popped element into its correct position.
# 4. Maintain smaller elements below larger elements.
# 5. The largest element will be at the top.


def insert_at_correct_position(
    stack: list[int],
    element: int
) -> None:

    # Insert when stack is empty or top is smaller.
    if not stack or stack[-1] < element:
        stack.append(element)
        return

    # Remove current top.
    top = stack.pop()

    # Recursively find correct position.
    insert_at_correct_position(stack, element)

    # Restore the removed element.
    stack.append(top)


def sort_stack(stack: list[int]) -> None:
    # Base case.
    if not stack:
        return

    # Remove top element.
    top = stack.pop()

    # Sort remaining stack.
    sort_stack(stack)

    # Insert element in sorted position.
    insert_at_correct_position(stack, top)


# CODE:
# stack = [3, 2, 1]
# sort_stack(stack)
# print(stack)  # [1, 2, 3]
#
# stack = [11, 2, 32, 3, 41]
# sort_stack(stack)
# print(stack)  # [2, 3, 11, 32, 41]
#
# stack = []
# sort_stack(stack)
# print(stack)  # []


# TIME COMPLEXITY = O(N^2)
# Each element may need to move through the stack.
#
# SPACE COMPLEXITY = O(N)
# Recursive call stack.
# No additional data structure is used.
