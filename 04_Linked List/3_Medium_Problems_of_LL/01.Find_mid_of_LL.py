# QUESTION:
# Given the head of a singly linked list, find its middle node.
# If there are two middle nodes, return the second middle node.
#
# APPROACH:
# Use slow and fast pointers.
# Slow moves one step, fast moves two steps.
# When fast reaches the end, slow points to the middle.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def find_middle(head: Node | None) -> Node | None:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# CODE:
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
#
# middle = find_middle(head)
# print(middle.data)  # 3
#
# head.next.next.next.next.next = Node(6)
# print(find_middle(head).data)  # 4


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
