# QUESTION:
# Given a linked list, remove the N-th node from its end.
#
# APPROACH:
# 1. Create a dummy node before the head.
# 2. Move fast pointer N steps ahead.
# 3. Move fast and slow together until fast reaches the last node.
# 4. Delete the node immediately after slow.
# 5. Return dummy.next.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def remove_nth_from_end(
    head: Node | None,
    n: int
) -> Node | None:

    if n <= 0:
        return head

    dummy = Node(0)
    dummy.next = head

    slow = fast = dummy

    # Move fast pointer n steps ahead.
    for _ in range(n):
        fast = fast.next

        if fast is None:
            return head

    # Move both pointers until fast reaches the last node.
    while fast.next:
        slow = slow.next
        fast = fast.next

    # Remove the N-th node from the end.
    target = slow.next
    slow.next = target.next

    return dummy.next


# CODE:
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
#
# head = remove_nth_from_end(head, 2)
#
# current = head
# while current:
#     print(current.data, end=" ")
#     current = current.next
# Output: 1 2 3 5
#
# head = remove_nth_from_end(head, 4)
# Output: 2 3 5


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
