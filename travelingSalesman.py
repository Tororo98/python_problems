from functools import lru_cache
import sys

def tspGrid(horizontal, vertical):
    m, n = len(horizontal), len(horizontal[0]) + 1
    total_cells = m * n

    # Convert grid positions to indices and vice versa
    def pos_to_idx(x, y):
        return x * n + y

    def idx_to_pos(idx):
        return divmod(idx, n)

    # Build the graph: each cell (i,j) has up to 4 neighbors (up, down, left, right)
    from collections import defaultdict
    graph = defaultdict(dict)
    for i in range(m):
        for j in range(n - 1):
            u = pos_to_idx(i, j)
            v = pos_to_idx(i, j + 1)
            cost = horizontal[i][j]
            graph[u][v] = cost
            graph[v][u] = cost

    for i in range(m - 1):
        for j in range(n):
            u = pos_to_idx(i, j)
            v = pos_to_idx(i + 1, j)
            cost = vertical[i][j]
            graph[u][v] = cost
            graph[v][u] = cost

    @lru_cache(None)
    def dp(curr, visited):
        if visited == (1 << total_cells) - 1:
            return graph[curr].get(0, float('inf'))  # Must return to start

        res = float('inf')
        for neighbor in graph[curr]:
            if not (visited & (1 << neighbor)):
                res = min(res, graph[curr][neighbor] + dp(neighbor, visited | (1 << neighbor)))
        return res

    # Start at cell (0,0) -> index 0, and mark it visited
    result = dp(0, 1)
    return result if result != float('inf') else 0