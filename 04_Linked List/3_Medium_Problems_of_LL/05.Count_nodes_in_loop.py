# QUESTION:
# Given a linked list containing a loop, count the number
# of nodes present in the loop.
# Return 0 if there is no loop.
#
# APPROACH:
# 1. Use slow and fast pointers to detect a loop.
# 2. When they meet, keep one pointer fixed.
# 3. Move the other pointer until it returns to the meeting node.
# 4. Count the number of movements.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def count_nodes_in_loop(head: Node | None) -> int:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            count = 1
            current = slow.next

            while current is not slow:
                count += 1
                current = current.next

            return count

    return 0


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
# print(count_nodes_in_loop(head))  # 3
#
# head = Node(1)
# head.next = Node(2)
# print(count_nodes_in_loop(head))  # 0


# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
