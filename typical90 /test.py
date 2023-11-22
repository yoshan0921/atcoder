# 入力
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1  # 0-indexed に
    G[a].append(b)
    G[b].append(a)

# 頂点 s から DFS (ここではスタックを使う)


def dfs(s):
    # 頂点 s からの距離
    dist = [-1] * N
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
dist0 = dfs(0)
mv = max(enumerate(dist0), key=lambda x: x[1])[0]
distmv = dfs(mv)
print(max(distmv) + 1)
