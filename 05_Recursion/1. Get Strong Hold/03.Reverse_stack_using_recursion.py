# QUESTION:
# Reverse a stack using recursion.
#
# Do not use any extra data structure.
# Use only the recursion call stack.
#
# Example:
# Input:  [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
#
# APPROACH:
# 1. Pop the top element from the stack.
# 2. Recursively reverse the remaining stack.
# 3. Insert the popped element at the bottom.
# 4. Repeat until the entire stack is reversed.


def insert_at_bottom(stack: list[int], element: int) -> None:
    # Base case: stack is empty.
    if not stack:
        stack.append(element)
        return

    # Remove top element.
    top = stack.pop()

    # Recursively insert element at bottom.
    insert_at_bottom(stack, element)

    # Restore removed element.
    stack.append(top)


def reverse_stack(stack: list[int]) -> None:
    # Base case.
    if not stack:
        return

    # Remove the top element.
    top = stack.pop()

    # Reverse remaining stack.
    reverse_stack(stack)

    # Insert removed element at the bottom.
    insert_at_bottom(stack, top)


# CODE:
# stack = [1, 2, 3, 4, 5]
# reverse_stack(stack)
# print(stack)  # [5, 4, 3, 2, 1]
#
# stack = [10, 20, 30]
# reverse_stack(stack)
# print(stack)  # [30, 20, 10]
#
# stack = []
# reverse_stack(stack)
# print(stack)  # []


# TIME COMPLEXITY = O(N^2)
# Inserting each element at the bottom takes O(N).
# This operation is repeated N times.
#
# SPACE COMPLEXITY = O(N)
# Recursive call stack.
# No additional data structure is used.
