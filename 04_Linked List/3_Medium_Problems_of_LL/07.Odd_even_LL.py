# QUESTION:
# Group all nodes at odd positions together, followed by
# nodes at even positions.
#
# Preserve the relative order of nodes within each group.
#
# APPROACH:
# 1. Maintain odd and even pointers.
# 2. Connect odd-position nodes together.
# 3. Connect even-position nodes together.
# 4. Attach the even list after the odd list.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def odd_even_list(head: Node | None) -> Node | None:
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head


# CODE:
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
#
# head = odd_even_list(head)
#
# current = head
# while current:
#     print(current.data, end=" ")
#     current = current.next
# Output: 1 3 5 2 4


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
