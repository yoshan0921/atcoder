"""
Depth First Search Template
"""
import collections
import io
import sys
import time

sys.setrecursionlimit(10**6)

# Q1: Start from vertex 0 and find all vertices that can be reached from it
_INPUT1 = """\
8 12
0 1
0 4
1 3
1 7
2 0
2 4
3 2
5 3
5 4
5 6
6 3
6 7
"""

# Q2: Answer how many connected group this graph consists of.
_INPUT2 = """\
9 11
0 1
0 2
0 4
1 8
2 4
2 8
3 5
3 6
4 7
5 6
7 8
"""


sys.stdin = io.StringIO(_INPUT1)


def dfs_stack_for_graph(graph, vertex_start):
    """DFS stack version"""

    stack = [vertex_start]
    visited = set()
    visited.add(vertex_start)

    while stack:
        vertex = stack.pop()
        for neighbor in graph[vertex]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            stack.append(neighbor)

    return visited


def dfs_recursive_for_graph(graph, vertex_start, visited: set = None):
    """DFS recursive version"""

    if visited is None:
        visited = set()

    visited.add(vertex_start)
    for neighbor in graph[vertex_start]:
        if neighbor in visited:
            continue
        dfs_recursive_for_graph(graph, neighbor, visited)

    return visited


if __name__ == "__main__":
    N, M = map(int, input().split())

    G = collections.defaultdict(list)
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    print(G)

# Q1
    # Stack version
    time_start = time.time()
    visited = dfs_stack_for_graph(G, 0)
    print(visited)
    print(f"processing time={time.time() - time_start:06.5f}")

    # Recursive version
    time_start = time.time()
    visited = dfs_recursive_for_graph(G, 0)
    print(visited)
    print(f"processing time={time.time() - time_start:06.5f}")

# Q2
    # # Stack version
    # time_start = time.time()
    # ans = set()
    # count = 0
    # for i in range(N):
    #     if i in ans:
    #         continue
    #     ans.update(dfs_stack_for_graph(G, i))
    #     count += 1
    # print(count)
    # print(f"processing time={time.time() - time_start:06.5f}")

    # # Recursive version
    # time_start = time.time()
    # ans = set()
    # count = 0
    # for i in range(N):
    #     if i in ans:
    #         continue
    #     ans.update(dfs_recursive_for_graph(G, i))
    #     count += 1
    # print(count)
    # print(f"processing time={time.time() - time_start:06.5f}")
