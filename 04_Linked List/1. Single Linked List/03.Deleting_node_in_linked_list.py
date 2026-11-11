# QUESTION:
# Given a singly linked list and an integer x,
# delete the x-th node from the linked list.
#
# Position uses 1-based indexing.
#
# Example:
# Input: 1 -> 3 -> 4, x = 3
# Output: 1 -> 3
#
# APPROACH:
# 1. If the list is empty or x is invalid, return the head.
# 2. If x == 1, delete the head by returning head.next.
# 3. Otherwise, traverse to the node just before position x.
# 4. Skip the node to be deleted by updating the next pointer.
# 5. Return the modified head.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def delete_node(
    head: Node | None,
    x: int
) -> Node | None:

    if head is None or x <= 0:
        return head

    # Delete the first node.
    if x == 1:
        return head.next

    current = head
    position = 1

    # Reach the node immediately before position x.
    while current and position < x - 1:
        current = current.next
        position += 1

    # Position is outside the linked list.
    if current is None or current.next is None:
        return head

    # Delete the target node.
    current.next = current.next.next

    return head


def print_linked_list(head: Node | None) -> None:
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# CODE:
# head = Node(1)
# head.next = Node(3)
# head.next.next = Node(4)
#
# head = delete_node(head, 3)
# print_linked_list(head)
# Output: 1 -> 3 -> None
#
# head = Node(1)
# head.next = Node(5)
# head.next.next = Node(2)
# head.next.next.next = Node(9)
#
# head = delete_node(head, 2)
# print_linked_list(head)
# Output: 1 -> 2 -> 9 -> None
#
# head = delete_node(head, 1)
# print_linked_list(head)
# Output: 2 -> 9 -> None


# TIME COMPLEXITY = O(N)
# In the worst case, we traverse the linked list.
#
# SPACE COMPLEXITY = O(1)
# Only constant extra variables are used.
