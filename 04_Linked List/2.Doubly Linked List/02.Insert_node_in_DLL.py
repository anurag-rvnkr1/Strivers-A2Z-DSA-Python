# QUESTION:
# Given a doubly linked list, a position p and an integer x,
# insert a new node containing x immediately after the p-th node.
#
# Position p uses 0-based indexing.
#
# Example:
# Input: 2 <-> 4 <-> 5, p = 2, x = 6
# Output: 2 <-> 4 <-> 5 <-> 6
#
# APPROACH:
# 1. Traverse to the node at position p.
# 2. Create a new node.
# 3. Set its prev pointer to the current node.
# 4. Set its next pointer to the current node's next node.
# 5. Update the next node's prev pointer, if it exists.
# 6. Connect the current node to the new node.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


def add_node(
    head: Node | None,
    pos: int,
    data: int
) -> Node | None:

    if head is None or pos < 0:
        return head

    current = head

    # Reach the node at position pos.
    for _ in range(pos):
        if current.next is None:
            return head

        current = current.next

    new_node = Node(data)

    next_node = current.next

    # Connect new node with previous node.
    new_node.prev = current
    new_node.next = next_node

    # Update the next node's previous pointer.
    if next_node:
        next_node.prev = new_node

    # Connect current node with new node.
    current.next = new_node

    return head


def print_forward(head: Node | None) -> None:
    current = head

    while current:
        print(current.data, end=" <-> ")
        current = current.next

    print("None")


# CODE:
# head = Node(2)
# second = Node(4)
# third = Node(5)
#
# head.next = second
# second.prev = head
# second.next = third
# third.prev = second
#
# head = add_node(head, 2, 6)
# print_forward(head)
# Output: 2 <-> 4 <-> 5 <-> 6 <-> None
#
# head = add_node(head, 0, 44)
# print_forward(head)
# Output: 2 <-> 44 <-> 4 <-> 5 <-> 6 <-> None


# TIME COMPLEXITY = O(N)
# Traversal to position p takes O(N) in the worst case.
# Actual pointer insertion takes O(1).
#
# SPACE COMPLEXITY = O(1)
# Only one new node and constant extra pointers are used.
