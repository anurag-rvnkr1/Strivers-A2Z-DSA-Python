# QUESTION:
# Given a linked list, determine whether it contains a cycle.
#
# APPROACH:
# Use Floyd's Cycle Detection Algorithm.
# Slow moves one step and fast moves two steps.
# If they meet, a cycle exists.
# If fast reaches None, no cycle exists.

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

def detect_loop(head: Node | None) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False

# CODE:
# head = Node(1)
# second = Node(2)
# third = Node(3)
#
# head.next = second
# second.next = third
# third.next = second
#
# print(detect_loop(head))  # True
#
# head = Node(1)
# head.next = Node(2)
# print(detect_loop(head))  # False

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
