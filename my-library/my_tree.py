"""
Tree Structure Template
"""

import collections
import io
import sys

# Q1: Find the maximum distance between two vertices of this tree.
_INPUT1 = """\
8
0 1
0 2
1 3
1 7
2 4
2 5
5 6
"""
sys.stdin = io.StringIO(_INPUT1)


def bfs(graph, vertex_start):
    """BFS queue version"""

    que = collections.deque([])
    que.append(vertex_start)
    visited = set()
    visited.add(vertex_start)
    distance = collections.defaultdict(int)  # distance from vertex_start

    while len(que) > 0:
        vertex = que.popleft()
        for neighbor in graph[vertex]:
            # Check if the next vertex is already visited.
            if neighbor in visited:
                continue
            # Calculate the distance of neighbor from vertex_start, then add it to the queue.
            distance[neighbor] = distance[vertex] + 1
            que.append(neighbor)
            visited.add(neighbor)

    return distance


def dfs(graph, vertex_start, visited: set = None, distance: dict = None):
    """DFS recursive version"""

    if visited is None:
        visited = set()
    if distance is None:
        distance = collections.defaultdict(int)

    visited.add(vertex_start)
    print(visited)

    for neighbor in graph[vertex_start]:
        # Check if the next vertex is already visited.
        if neighbor in visited:
            continue
        # Calculate the distance of neighbor from vertex_start, then add it to the queue.
        distance[neighbor] = distance[vertex_start] + 1
        dfs(graph, neighbor, visited, distance)

    return distance


if __name__ == "__main__":
    N = int(input())
    G = collections.defaultdict(list)
    for i in range(N-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    # print(G)

    # BFS version
    distance1 = bfs(G, 0)
    print(distance1)

    distance2 = bfs(G, max(distance1, key=distance1.get))
    print(distance2)

    print(max(distance2.values()))

    # DFS version
    distance3 = dfs(G, 0)
    print(distance3)

    distance4 = dfs(G, max(distance3, key=distance3.get))
    print(distance4)

    print(max(distance4.values()))
