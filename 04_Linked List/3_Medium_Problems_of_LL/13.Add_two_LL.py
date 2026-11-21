# QUESTION:
# Given two non-empty linked lists representing two non-negative
# integers, add the numbers and return their sum as a linked list.
#
# Digits are stored in reverse order.
#
# Example:
# Input:
# List 1: 2 -> 4 -> 3
# List 2: 5 -> 6 -> 4
#
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
# APPROACH:
# 1. Traverse both linked lists simultaneously.
# 2. Add corresponding digits and carry.
# 3. Store total % 10 in a new node.
# 4. Update carry = total // 10.
# 5. Continue until both lists and carry are exhausted.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def add_two_numbers(
    l1: Node | None,
    l2: Node | None
) -> Node | None:

    dummy = Node(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        total = carry

        if l1:
            total += l1.data
            l1 = l1.next

        if l2:
            total += l2.data
            l2 = l2.next

        carry = total // 10
        digit = total % 10

        current.next = Node(digit)
        current = current.next

    return dummy.next


# CODE:
# l1 = Node(2)
# l1.next = Node(4)
# l1.next.next = Node(3)
#
# l2 = Node(5)
# l2.next = Node(6)
# l2.next.next = Node(4)
#
# result = add_two_numbers(l1, l2)
#
# current = result
# while current:
#     print(current.data, end=" ")
#     current = current.next
# Output: 7 0 8
#
# Explanation: 342 + 465 = 807


# TIME COMPLEXITY = O(max(N, M))
# Each input node is visited once.
#
# SPACE COMPLEXITY = O(max(N, M))
# The output linked list stores the resulting digits.
# Auxiliary space excluding output = O(1).
