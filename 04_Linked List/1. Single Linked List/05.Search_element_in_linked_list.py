# QUESTION:
# Given a linked list containing n nodes and a key,
# check whether the key is present in the linked list.
#
# Return True if the key exists, otherwise return False.
#
# Example:
# Input:
# Linked list = 1 -> 2 -> 3 -> 4
# Key = 3
#
# Output: True
#
# APPROACH:
# 1. Start traversing from the head.
# 2. Compare each node's data with the key.
# 3. If a match is found, return True immediately.
# 4. If traversal finishes without a match, return False.

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

def search_key(
    n: int,
    head: Node | None,
    key: int
) -> bool:

    current = head
    visited = 0

    while current and visited < n:
        if current.data == key:
            return True

        current = current.next
        visited += 1

    return False

# CODE:
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
#
# print(search_key(4, head, 3))  # True
# print(search_key(4, head, 5))  # False
#
# print(search_key(0, None, 10))  # False

# TIME COMPLEXITY = O(N)
# In the worst case, every node is visited.
#
# SPACE COMPLEXITY = O(1)
# Only constant extra variables are used.
