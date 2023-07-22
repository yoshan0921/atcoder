import collections
import io
import sys

_INPUT = """\
8
3 7 4 7 3 3 8 2
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

G = []
for i in range(len(A)):
    G.append([i+1, A[i]])
# print(G)

checked = [False] * (N+1)
count = 0
node = []
i = 1
while True:
    set_node = set(node)
    if i in set_node:
        idx = node.index(i)
        print(count)
        print(*node[idx:])
        break
    count += 1
    node.append(i)
    i = G[i-1][1]
