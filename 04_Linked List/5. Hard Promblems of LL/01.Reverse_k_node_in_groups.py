# QUESTION:
# Given the head of a linked list, reverse its nodes k at a time.
# If fewer than k nodes remain, leave those nodes unchanged.
#
# APPROACH:
# 1. Check whether at least k nodes remain.
# 2. Reverse exactly k nodes using three pointers.
# 3. Recursively process the remaining linked list.
# 4. Connect the tail of the reversed group to the
#    recursively processed remainder.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def reverse_k_group(
    head: Node | None,
    k: int
) -> Node | None:

    if head is None or k <= 1:
        return head

    # Check whether k nodes are available.
    current = head

    for _ in range(k):
        if current is None:
            return head
        current = current.next

    # Reverse exactly k nodes.
    previous = None
    current = head

    for _ in range(k):
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    # Connect the reversed group to the remaining list.
    head.next = reverse_k_group(current, k)

    return previous


# CODE:
# head = Node(1)
# current = head
#
# for value in [2, 3, 4, 5, 6, 7, 8]:
#     current.next = Node(value)
#     current = current.next
#
# head = reverse_k_group(head, 3)
#
# current = head
# while current:
#     print(current.data, end=" ")
#     current = current.next
#
# Output: 3 2 1 6 5 4 7 8
#
# Example 2:
# head = reverse_k_group(head, 2)
# Each complete group of two is reversed.


# TIME COMPLEXITY = O(N)
# Every node is processed once.
#
# SPACE COMPLEXITY = O(N/K)
# Recursive call stack, one call per group.
# Auxiliary space is O(1) for an iterative implementation.
