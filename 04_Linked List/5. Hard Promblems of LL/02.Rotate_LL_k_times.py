# QUESTION:
# Given the head of a linked list, rotate the list to the right
# by k positions.
#
# Example:
# Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
# Output: 4 -> 5 -> 1 -> 2 -> 3
#
# APPROACH:
# 1. Calculate the length of the linked list.
# 2. Connect the last node to the head to form a circle.
# 3. Reduce k using k % length.
# 4. Find the new tail at position length - k - 1.
# 5. Break the circular link and return the new head.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def rotate_right(
    head: Node | None,
    k: int
) -> Node | None:

    if head is None or head.next is None or k == 0:
        return head

    # Calculate length and find original tail.
    length = 1
    tail = head

    while tail.next:
        tail = tail.next
        length += 1

    k %= length

    if k == 0:
        return head

    # Form a circular linked list.
    tail.next = head

    # Find the new tail.
    steps = length - k
    new_tail = head

    for _ in range(steps - 1):
        new_tail = new_tail.next

    # Break the circle.
    new_head = new_tail.next
    new_tail.next = None

    return new_head


# CODE:
# head = Node(1)
# current = head
#
# for value in [2, 3, 4, 5]:
#     current.next = Node(value)
#     current = current.next
#
# head = rotate_right(head, 2)
#
# current = head
# while current:
#     print(current.data, end=" ")
#     current = current.next
#
# Output: 4 5 1 2 3
#
# print(rotate_right(head, 5) is head)  # True


# TIME COMPLEXITY = O(N)
# Length calculation and new-tail traversal take O(N).
#
# SPACE COMPLEXITY = O(1)
# Only constant extra pointers are used.
