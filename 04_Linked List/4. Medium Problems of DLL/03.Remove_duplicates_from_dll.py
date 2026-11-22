# QUESTION:
# Given a sorted doubly linked list, remove all duplicate nodes.
# Keep only one occurrence of each value.
#
# Example:
# Input:  1 <-> 1 <-> 2 <-> 3 <-> 3
#
# Output: 1 <-> 2 <-> 3
#
# APPROACH:
# 1. Start traversing from the head.
# 2. Compare the current node with its next node.
# 3. If both values are equal, delete the next node.
# 4. Update the current node's next pointer.
# 5. Update the following node's prev pointer.
# 6. Otherwise, move to the next node.
#
# Since the list is sorted, duplicates are adjacent.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


def remove_duplicates(head: Node | None) -> Node | None:
    if head is None:
        return None

    current = head

    while current and current.next:
        next_node = current.next

        if current.data == next_node.data:
            # Skip the duplicate node.
            current.next = next_node.next

            # Repair backward link.
            if next_node.next:
                next_node.next.prev = current

            # Disconnect duplicate.
            next_node.prev = None
            next_node.next = None

        else:
            current = current.next

    return head


def print_dll(head: Node | None) -> None:
    current = head

    while current:
        print(current.data, end=" <-> ")
        current = current.next

    print("None")


# CODE:
# head = Node(1)
# second = Node(1)
# third = Node(2)
# fourth = Node(3)
# fifth = Node(3)
#
# nodes = [head, second, third, fourth, fifth]
#
# for i in range(len(nodes) - 1):
#     nodes[i].next = nodes[i + 1]
#     nodes[i + 1].prev = nodes[i]
#
# head = remove_duplicates(head)
# print_dll(head)
# Output: 1 <-> 2 <-> 3 <-> None
#
# head = Node(1)
# head.next = Node(1)
# head.next.prev = head
# head.next.next = Node(1)
# head.next.next.prev = head.next
#
# head = remove_duplicates(head)
# print_dll(head)
# Output: 1 <-> None


# TIME COMPLEXITY = O(N)
# Every node is processed at most once.
#
# SPACE COMPLEXITY = O(1)
# Only constant extra pointers are used.
