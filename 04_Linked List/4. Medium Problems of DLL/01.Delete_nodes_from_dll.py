# QUESTION:
# Given a doubly linked list and an integer key,
# delete all occurrences of the key from the list.
#
# Example:
# Input:  2 <-> 2 <-> 10 <-> 8 <-> 4 <-> 2 <-> 5 <-> 2
# Key:    2
#
# Output: 10 <-> 8 <-> 4 <-> 5
#
# APPROACH:
# 1. Traverse the entire doubly linked list.
# 2. Check whether the current node contains the key.
# 3. If it matches, update the previous node's next pointer.
# 4. Update the next node's prev pointer.
# 5. If the current node is the head, update the head.
# 6. Continue traversal using the saved next pointer.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


def delete_all_occurrences(
    head: Node | None,
    key: int
) -> Node | None:

    current = head

    while current:
        next_node = current.next

        if current.data == key:
            # Update previous node.
            if current.prev:
                current.prev.next = current.next
            else:
                # Key occurs at the head.
                head = current.next

            # Update next node.
            if current.next:
                current.next.prev = current.prev

            # Disconnect the deleted node.
            current.prev = None
            current.next = None

        current = next_node

    return head


def print_dll(head: Node | None) -> None:
    current = head

    while current:
        print(current.data, end=" <-> ")
        current = current.next

    print("None")


# CODE:
# head = Node(2)
# second = Node(2)
# third = Node(10)
# fourth = Node(8)
# fifth = Node(4)
# sixth = Node(2)
# seventh = Node(5)
# eighth = Node(2)
#
# nodes = [
#     head, second, third, fourth,
#     fifth, sixth, seventh, eighth
# ]
#
# for i in range(len(nodes) - 1):
#     nodes[i].next = nodes[i + 1]
#     nodes[i + 1].prev = nodes[i]
#
# head = delete_all_occurrences(head, 2)
# print_dll(head)
# Output: 10 <-> 8 <-> 4 <-> 5 <-> None
#
# head = delete_all_occurrences(head, 10)
# print_dll(head)
# Output: 8 <-> 4 <-> 5 <-> None
#
# head = delete_all_occurrences(head, 100)
# print_dll(head)
# Output: 8 <-> 4 <-> 5 <-> None


# TIME COMPLEXITY = O(N)
# Each node is visited exactly once.
#
# SPACE COMPLEXITY = O(1)
# Only constant extra pointers are used.
