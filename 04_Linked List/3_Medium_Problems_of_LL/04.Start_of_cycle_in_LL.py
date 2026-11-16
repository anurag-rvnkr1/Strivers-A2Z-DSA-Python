# QUESTION:
# Given a linked list containing a cycle, return the node
# where the cycle begins.
# Return None if there is no cycle.
#
# APPROACH:
# 1. Use slow and fast pointers to detect a meeting point.
# 2. If they meet, move one pointer back to head.
# 3. Move both pointers one step at a time.
# 4. Their next meeting point is the cycle's starting node.

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

def detect_cycle_start(head: Node | None) -> Node | None:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            slow = head

            while slow is not fast:
                slow = slow.next
                fast = fast.next

            return slow

    return None

# CODE:
# head = Node(1)
# second = Node(2)
# third = Node(3)
# fourth = Node(4)
#
# head.next = second
# second.next = third
# third.next = fourth
# fourth.next = second
#
# start = detect_cycle_start(head)
# print(start.data if start else None)  # 2

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
