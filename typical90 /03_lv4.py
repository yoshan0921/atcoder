import io
import sys
import itertools

_INPUT = """\
3
1 2
2 3
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# 頂点 s から DFS (ここではスタックを使う)


def dfs(s):
    # 頂点 s からの距離
    dist = [-1] * (N+1)
    dist[s] = 0

    # スタックで DFS
    st = [s]
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist[v] + 1

    # リターン
    return dist


# 頂点 0 から
dist0 = dfs(1)
# print(dist0)

# enumerateを使うことで（都市番号、距離）と表現。距離でMaxを取って後で都市番号を取り出す。
mv = max(enumerate(dist0), key=lambda x: x[1])[0]
distmv = dfs(mv)
print(max(distmv) + 1)
