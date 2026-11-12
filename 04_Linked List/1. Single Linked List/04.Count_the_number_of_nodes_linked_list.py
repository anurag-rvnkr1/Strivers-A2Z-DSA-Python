# QUESTION:
# Given a singly linked list, find its length.
# Length is the total number of nodes in the list.
#
# Example:
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 5
#
# APPROACH:
# 1. Initialize count = 0.
# 2. Start traversing from the head.
# 3. Increment count for every visited node.
# 4. Move to the next node.
# 5. Stop when current becomes None.
# 6. Return count.

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

def get_count(head: Node | None) -> int:
    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    return count

# CODE:
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
#
# print(get_count(head))  # 5
#
# print(get_count(None))  # 0

# TIME COMPLEXITY = O(N)
# Every node is visited exactly once.
#
# SPACE COMPLEXITY = O(1)
# Only count and current variables are used.
