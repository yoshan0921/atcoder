"""
Depth First Search Template
"""
import io
import sys

sys.setrecursionlimit(10**6)

_INPUT = """\
8 12
0 1
0 4
1 3
1 7
2 0
2 4
3 2
3 6
5 3
5 4
6 5
6 7
"""
sys.stdin = io.StringIO(_INPUT)


# 頂点vを始点とした深さ優先探索
def rec_v1(v, G, checked, ans):
    # 頂点vをチェック済にする
    checked[v] = True

    # 到達順に頂点を格納
    ans.append(v)

    # G[v]に含まれる頂点について確認する
    for v2 in G[v]:
        # v2がチェク済ならスキップする
        if checked[v2]:
            continue
        # v2始点で深さ優先探索を行う
        rec_v1(v2, G, checked, ans)

    # グラフではなく座標問題の場合
    # dfs(x+1, y)
    # dfs(x-1, y)
    # dfs(x, y+1)
    # dfs(x, y-1)
    return


# Input
N, M = map(int, input().split())

# グラフを表現する隣接リスト
G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    # 頂点aから頂点bへの辺を隣接リストに入れる
    G[a].append(b)

# 各G[v]を小さい順に並べる
for v in range(N):
    G[v].sort()

# checked[v]：頂点vがチェック済みならtrue、そうでないならfalse
checked = [False for _ in range(N)]

# 到達順に頂点を格納するリスト
ans = []

# 頂点 0 を始点として深さ優先探索を開始する
rec_v1(0, G, checked, ans)

print(ans)
