# QUESTION:
# Given a linked list containing only 0, 1 and 2,
# sort the list in ascending order.
#
# APPROACH:
# 1. Count the occurrences of 0, 1 and 2.
# 2. Traverse the linked list again.
# 3. Replace node values based on the frequency counts.
#
# This method changes node values, not node links.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def sort_012(head: Node | None) -> Node | None:
    if head is None:
        return None

    count = [0, 0, 0]
    current = head

    # Count frequencies.
    while current:
        if current.data not in (0, 1, 2):
            raise ValueError("List must contain only 0, 1 and 2")

        count[current.data] += 1
        current = current.next

    # Replace node values in sorted order.
    current = head

    for value in range(3):
        for _ in range(count[value]):
            current.data = value
            current = current.next

    return head


# CODE:
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(0)
# head.next.next.next = Node(1)
# head.next.next.next.next = Node(2)
#
# head = sort_012(head)
#
# current = head
# while current:
#     print(current.data, end=" ")
#     current = current.next
# Output: 0 1 1 2 2


# TIME COMPLEXITY = O(N)
# Two traversals of the linked list.
#
# SPACE COMPLEXITY = O(1)
# Fixed-size frequency array.
