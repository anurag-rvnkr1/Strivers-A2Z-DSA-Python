# QUESTION:
# Create a linked list using input pairs (value, position).
#
# If position is 0, insert the value at the beginning.
# If position is 1, insert the value at the end.
#
# Example:
# Input:  [(9, 0), (5, 1), (6, 1), (2, 0), (5, 0)]
# Output: 5 -> 2 -> 9 -> 5 -> 6
#
# APPROACH:
# 1. Create a new node for every insertion.
# 2. For beginning insertion, point the new node to head.
# 3. Update head to the new node.
# 4. For end insertion, traverse to the last node.
# 5. Connect the last node to the new node.
# 6. Handle an empty linked list separately.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def insert_at_beginning(
    head: Node | None,
    value: int
) -> Node:
    new_node = Node(value)
    new_node.next = head

    return new_node


def insert_at_end(
    head: Node | None,
    value: int
) -> Node:
    new_node = Node(value)

    if head is None:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node

    return head


def construct_linked_list(
    operations: list[tuple[int, int]]
) -> Node | None:
    head = None

    for value, position in operations:
        if position == 0:
            head = insert_at_beginning(head, value)

        elif position == 1:
            head = insert_at_end(head, value)

        else:
            raise ValueError("Position must be 0 or 1")

    return head


def print_linked_list(head: Node | None) -> None:
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# CODE:
# operations = [(9, 0), (5, 1), (6, 1), (2, 0), (5, 0)]
# head = construct_linked_list(operations)
# print_linked_list(head)
# Output: 5 -> 2 -> 9 -> 5 -> 6 -> None
#
# head = insert_at_beginning(None, 10)
# head = insert_at_end(head, 20)
# print_linked_list(head)
# Output: 10 -> 20 -> None


# TIME COMPLEXITY:
# insert_at_beginning = O(1)
# insert_at_end = O(N)
# construct_linked_list = O(N^2) worst case
# because every end insertion may traverse the current list.
#
# SPACE COMPLEXITY = O(N)
# N nodes are created.
# Each individual insertion uses O(1) auxiliary space.
