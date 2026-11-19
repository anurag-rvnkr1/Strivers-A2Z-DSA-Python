# QUESTION:
# Delete the middle node of a singly linked list.
# For an even-length list, delete the second of the two middle nodes.
#
# APPROACH:
# 1. Handle empty and single-node lists.
# 2. Use slow and fast pointers.
# 3. Maintain a previous pointer to the slow pointer.
# 4. When fast reaches the end, slow is the middle node.
# 5. Delete it by updating previous.next.

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

def delete_middle(head: Node | None) -> Node | None:
    if head is None or head.next is None:
        return None

    slow = fast = head
    previous = None

    while fast and fast.next:
        previous = slow
        slow = slow.next
        fast = fast.next.next

    # Delete the middle node.
    previous.next = slow.next

    return head

# CODE:
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
#
# head = delete_middle(head)
#
# current = head
# while current:
#     print(current.data, end=" ")
#     current = current.next
# Output: 1 2 4 5
#
# head = delete_middle(None)
# print(head)  # None

# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
