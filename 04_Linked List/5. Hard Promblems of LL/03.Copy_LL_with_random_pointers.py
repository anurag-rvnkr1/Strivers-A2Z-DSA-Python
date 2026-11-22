# QUESTION:
# Each node of a linked list contains:
# 1. data
# 2. next pointer
# 3. random pointer
#
# Create a deep copy of the linked list.
# The copied list must contain entirely new nodes.
# Its next and random pointers must preserve the original structure.
#
# APPROACH:
# Use the interweaving technique.
#
# 1. Insert a copied node immediately after each original node.
# 2. Set each copied node's random pointer using the original
#    node's random pointer.
# 3. Separate the original list and copied list.
# 4. Return the copied head.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.random = None


def copy_random_list(head: Node | None) -> Node | None:

    if head is None:
        return None

    # STEP 1: Create and interweave copied nodes.
    current = head

    while current:
        copied = Node(current.data)

        copied.next = current.next
        current.next = copied

        current = copied.next

    # STEP 2: Assign random pointers to copied nodes.
    current = head

    while current:
        copied = current.next

        if current.random:
            copied.random = current.random.next

        current = copied.next

    # STEP 3: Separate original and copied lists.
    current = head
    copied_head = head.next

    while current:
        copied = current.next
        original_next = copied.next

        current.next = original_next

        if original_next:
            copied.next = original_next.next
        else:
            copied.next = None

        current = original_next

    return copied_head


# CODE:
# head = Node(7)
# second = Node(13)
# third = Node(11)
# fourth = Node(10)
# fifth = Node(1)
#
# head.next = second
# second.next = third
# third.next = fourth
# fourth.next = fifth
#
# second.random = head
# third.random = fifth
# fourth.random = third
# fifth.random = head
#
# copied_head = copy_random_list(head)
#
# current = copied_head
# while current:
#     random_value = (
#         current.random.data if current.random else None
#     )
#     print(current.data, random_value)
#     current = current.next
#
# Original list remains unchanged.
# Copied nodes are independent from original nodes.
#
# Example 2:
# head = Node(1)
# head.random = head
# copied = copy_random_list(head)
# print(copied.data, copied.random.data)  # 1 1


# TIME COMPLEXITY = O(N)
# Three traversals of the original list.
#
# SPACE COMPLEXITY = O(1) auxiliary space
# No dictionary or additional mapping is used.
# The copied nodes themselves require O(N) output space.
