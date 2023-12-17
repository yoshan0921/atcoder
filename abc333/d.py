from collections import deque
from copy import deepcopy
import io
import sys
import bisect
import collections
import itertools
import math
sys.setrecursionlimit(10**9)

_INPUT = """\
24
3 6
7 17
7 20
7 11
14 18
17 21
6 19
5 22
9 24
11 14
6 23
8 17
9 12
4 17
2 15
1 17
3 9
10 16
7 13
2 16
1 16
5 7
1 3
"""
sys.stdin = io.StringIO(_INPUT)


def dfs_iterative(graph, start):
    stack = [start]
    visited = set()

    while stack:
        vertex = stack.pop()
        if vertex == 1:
            continue
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return len(visited)


N = int(input())
tree = collections.defaultdict(list)

for i in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

delete_num = [0] * len(tree[1])

for i in range(len(tree[1])):
    delete_num[i] = dfs_iterative(tree, tree[1][i])

delete_num.sort(reverse=True)
ans = sum(delete_num[1:])
print(ans+1)
