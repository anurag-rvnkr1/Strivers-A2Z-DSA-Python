# QUESTION:
# Reverse a doubly linked list and return its new head.
#
# Example:
# Input:  75 <-> 122 <-> 59 <-> 196
# Output: 196 <-> 59 <-> 122 <-> 75
#
# APPROACH:
# 1. Start from the head.
# 2. Swap the next and prev pointers of each node.
# 3. After swapping, the old prev pointer points to
#    the next node in the original list.
# 4. Move using that pointer.
# 5. Return the last processed node as the new head.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


def reverse_dll(head: Node | None) -> Node | None:
    current = head
    new_head = None

    while current:
        # Swap both links.
        current.next, current.prev = current.prev, current.next

        # Save the new head.
        new_head = current

        # Move to the next node in the original list.
        current = current.prev

    return new_head


# CODE:
# head = Node(75)
# second = Node(122)
# third = Node(59)
# fourth = Node(196)
#
# head.next = second
# second.prev = head
# second.next = third
# third.prev = second
# third.next = fourth
# fourth.prev = third
#
# head = reverse_dll(head)
#
# current = head
# while current:
#     print(current.data, end=" ")
#     current = current.next
# Output: 196 59 122 75


# TIME COMPLEXITY = O(N)
# Every node is visited exactly once.
#
# SPACE COMPLEXITY = O(1)
# Only constant extra pointers are used.
