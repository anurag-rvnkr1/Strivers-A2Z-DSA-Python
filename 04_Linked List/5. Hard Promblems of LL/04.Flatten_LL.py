# QUESTION:
# Given a linked list in which every node has:
# 1. next pointer to another list head.
# 2. bottom pointer to a sorted sub-linked list.
#
# Flatten the entire structure into one sorted linked list
# using bottom pointers.
#
# APPROACH:
# 1. Recursively flatten the list to the right.
# 2. Merge the current bottom list with the flattened right list.
# 3. Use the bottom pointer for merging.
# 4. Set next pointers to None in the flattened result.
#
# Each individual bottom-linked list is already sorted.


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.bottom = None


def merge(
    head1: Node | None,
    head2: Node | None
) -> Node | None:

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.data <= head2.data:
        result = head1
        result.bottom = merge(head1.bottom, head2)
    else:
        result = head2
        result.bottom = merge(head1, head2.bottom)

    result.next = None

    return result


def flatten(root: Node | None) -> Node | None:

    if root is None or root.next is None:
        return root

    # Flatten the remaining lists.
    right = flatten(root.next)

    # Merge current list with flattened right side.
    root.next = None

    return merge(root, right)


def print_flattened_list(head: Node | None) -> None:
    current = head

    while current:
        print(current.data, end=" ")
        current = current.bottom


# CODE:
# head = Node(5)
# head.bottom = Node(7)
# head.bottom.bottom = Node(8)
# head.bottom.bottom.bottom = Node(30)
#
# second = Node(10)
# second.bottom = Node(20)
#
# third = Node(19)
# third.bottom = Node(22)
# third.bottom.bottom = Node(50)
#
# fourth = Node(28)
# fourth.bottom = Node(35)
# fourth.bottom.bottom = Node(40)
# fourth.bottom.bottom.bottom = Node(45)
#
# head.next = second
# second.next = third
# third.next = fourth
#
# head = flatten(head)
# print_flattened_list(head)
#
# Output:
# 5 7 8 10 19 20 22 28 30 35 40 45 50


# TIME COMPLEXITY = O(N * K)
# N = number of top-level list heads.
# K = average number of nodes in each bottom list.
# Total nodes are approximately N*K.
# Each merge level processes nodes across the lists.
# Overall bound is O(T log N), where T is total nodes.
#
# SPACE COMPLEXITY = O(N)
# Recursive flatten and merge calls use stack space.
