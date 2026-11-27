# QUESTION:
# Given an undirected graph and M colors, determine whether
# the graph can be colored using at most M colors such that
# no two adjacent vertices have the same color.
#
# Return True if coloring is possible, otherwise False.
#
# APPROACH:
# 1. Maintain a color array initialized to zero.
# 2. Assign colors to vertices one by one.
# 3. Check whether a color conflicts with an adjacent vertex.
# 4. If valid, recursively color the next vertex.
# 5. Backtrack if no valid coloring is found.


def graph_coloring(
    graph: list[list[int]],
    m: int
) -> bool:

    n = len(graph)

    if n == 0:
        return True

    if m <= 0:
        return False

    colors = [0] * n

    def is_safe(node: int, color: int) -> bool:
        for neighbor in range(n):
            if graph[node][neighbor] and colors[neighbor] == color:
                return False

        return True

    def solve(node: int) -> bool:
        if node == n:
            return True

        for color in range(1, m + 1):
            if is_safe(node, color):
                colors[node] = color

                if solve(node + 1):
                    return True

                # Backtrack.
                colors[node] = 0

        return False

    return solve(0)


# CODE:
# graph = [
#     [0, 1, 1],
#     [1, 0, 1],
#     [1, 1, 0]
# ]
#
# print(graph_coloring(graph, 3))  # True
# print(graph_coloring(graph, 2))  # False
#
# A triangle requires 3 different colors.


# TIME COMPLEXITY = O(M^N * N)
# Up to M choices per vertex and O(N) adjacency checking.
#
# SPACE COMPLEXITY = O(N)
# Color array and recursion stack.
