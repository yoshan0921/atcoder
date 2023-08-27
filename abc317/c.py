import collections
import io
import sys

_INPUT = """\
4 4
1 2 1
2 3 10
1 3 100
1 4 1000
"""
sys.stdin = io.StringIO(_INPUT)

# 街がN個
# 道路がM本
# i番目の道路は街Aと街Bを結ぶ。長さはC

N, M = map(int, input().split())
E = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    E[a][b] = c
    E[b][a] = c
print(E)

ans = 0
visited = [False]*(N+1)


def dfs(v, s):
    global ans
    visited[v] = True
    
    if s > ans:
        ans = s
    for i in range(1, N+1):
        if not visited[i] and E[v][i]:
            dfs(i, s+E[v][i])
    visited[v] = False


for i in range(1, N+1):
    dfs(i, 0)
print(ans)
