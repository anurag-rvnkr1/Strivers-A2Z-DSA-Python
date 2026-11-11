# QUESTION:
# Construct a singly linked list from an array and return
# the head of the linked list.
#
# Example:
# Input:  [1, 2, 3, 4, 5]
# Output: 1 -> 2 -> 3 -> 4 -> 5
#
# APPROACH:
# 1. Create the head node using the first array element.
# 2. Maintain a pointer named current.
# 3. Traverse the remaining array elements.
# 4. Create a new node for every element.
# 5. Connect the new node to the current node.
# 6. Return the head.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def construct_ll(arr: list[int]) -> Node | None:
    if not arr:
        return None

    head = Node(arr[0])
    current = head

    for value in arr[1:]:
        current.next = Node(value)
        current = current.next

    return head


def print_linked_list(head: Node | None) -> None:
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# CODE:
# head = construct_ll([1, 2, 3, 4, 5])
# print_linked_list(head)
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
#
# head = construct_ll([2, 4])
# print_linked_list(head)
# Output: 2 -> 4 -> None
#
# head = construct_ll([])
# print_linked_list(head)
# Output: None


# TIME COMPLEXITY = O(N)
# Each array element is processed exactly once.
#
# SPACE COMPLEXITY = O(N)
# N nodes are created for the linked list.
# Auxiliary space excluding the output list = O(1).
