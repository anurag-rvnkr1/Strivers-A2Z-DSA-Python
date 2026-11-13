# QUESTION:
# Given a doubly linked list, reverse the linked list
# and return its new head.
#
# Example:
# Input:  3 <-> 4 <-> 5
# Output: 5 <-> 4 <-> 3
#
# APPROACH:
# 1. Start traversing from the head.
# 2. Store the original next node.
# 3. Swap the next and prev pointers.
# 4. Move to the original next node.
# 5. The last processed node becomes the new head.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


def reverse_dll(head: Node | None) -> Node | None:
    current = head
    new_head = None

    while current:
        # Store original next node.
        next_node = current.next

        # Swap next and prev pointers.
        current.next = current.prev
        current.prev = next_node

        # The original last node becomes the new head.
        if current.prev is None:
            new_head = current

        # Continue using the original next node.
        current = current.prev

    return new_head


# CODE:
# head = Node(3)
# second = Node(4)
# third = Node(5)
#
# head.next = second
# second.prev = head
# second.next = third
# third.prev = second
#
# head = reverse_dll(head)
#
# current = head
# while current:
#     print(current.data, end=" ")
#     current = current.next
# Output: 5 4 3


# TIME COMPLEXITY = O(N)
# Every node is visited exactly once.
#
# SPACE COMPLEXITY = O(1)
# Only constant extra pointers are used.
