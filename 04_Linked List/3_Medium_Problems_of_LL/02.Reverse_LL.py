# QUESTION:
# Reverse a singly linked list and return its new head.
#
# APPROACH:
# Maintain three pointers: previous, current and next_node.
# Reverse each node's next pointer while traversing the list.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def reverse_list(head: Node | None) -> Node | None:
    previous = None
    current = head

    while current:
        next_node = current.next

        current.next = previous
        previous = current
        current = next_node

    return previous


# CODE:
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
#
# head = reverse_list(head)
#
# current = head
# while current:
#     print(current.data, end=" ")
#     current = current.next
# Output: 3 2 1


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
