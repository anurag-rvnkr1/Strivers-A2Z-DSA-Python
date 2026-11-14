# QUESTION:
# Given a doubly linked list and a position x,
# delete the node at position x.
#
# Position x uses 1-based indexing.
#
# Example:
# Input: 1 <-> 3 <-> 4, x = 3
# Output: 1 <-> 3
#
# APPROACH:
# 1. Check whether the list is empty or position is invalid.
# 2. Traverse to the node at position x.
# 3. Connect its previous node to its next node.
# 4. Update the next node's prev pointer.
# 5. If deleting the head, update the head.
# 6. Return the modified head.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


def delete_node(
    head: Node | None,
    x: int
) -> Node | None:

    if head is None or x <= 0:
        return head

    current = head

    # Traverse to the x-th node (1-based indexing).
    for _ in range(x - 1):
        if current is None:
            return head

        current = current.next

    # Position does not exist.
    if current is None:
        return head

    previous_node = current.prev
    next_node = current.next

    # Update previous node's next pointer.
    if previous_node:
        previous_node.next = next_node
    else:
        # Deleting the head node.
        head = next_node

    # Update next node's previous pointer.
    if next_node:
        next_node.prev = previous_node

    # Disconnect deleted node.
    current.prev = None
    current.next = None

    return head


def print_forward(head: Node | None) -> None:
    current = head

    while current:
        print(current.data, end=" <-> ")
        current = current.next

    print("None")


# CODE:
# head = Node(1)
# second = Node(3)
# third = Node(4)
#
# head.next = second
# second.prev = head
# second.next = third
# third.prev = second
#
# head = delete_node(head, 3)
# print_forward(head)
# Output: 1 <-> 3 <-> None
#
# head = delete_node(head, 1)
# print_forward(head)
# Output: 3 <-> None
#
# head = delete_node(head, 5)
# print_forward(head)
# Output: 3 <-> None


# TIME COMPLEXITY = O(N)
# Traversal takes O(N) in the worst case.
# Deletion and pointer updates take O(1).
#
# SPACE COMPLEXITY = O(1)
# Only constant extra pointers are used.
