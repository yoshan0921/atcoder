import io
import sys

_INPUT = """\
4 3
1 3 6
0 1 11
1 2 7
"""
sys.stdin = io.StringIO(_INPUT)

# 辺情報を表す構造体


class edge:
    def __init__(self, end, leng):
        self.end = end      # 辺の終点
        self.leng = leng    # 辺の重み


INF = 10**9  # 初期化で使う十分大きな数

# main
# 入力を受け取る
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    u, v, w = map(int, input().split())
    G[u].append(edge(v, w))

# done[i]：頂点iの最短距離が確定しているかどうかを表すリスト
done = [False for _ in range(N)]
# dist[i]：頂点0から頂点iへの暫定的な経路長
dist = [INF for _ in range(N)]
dist[0] = 0

while True:
    # v：次に見るべき頂点、d：仮の最小値
    v, d = -1, 2*INF

    # ステップ1
    # 当該頂点までの距離が未確定、且つ、distが最小の値を探す。
    # つまり、done[v]がFalse、且つdist[v]が最小のvを探す。
    for i in range(N):
        if done[i] == False and dist[i] < d:
            v = i
            d = dist[i]

    # もしそのようなvが見つからない場合、
    # すべての done[v]がTrueになっているので終了する。
    if v == -1:
        break

    # print(f"最小距離の頂点={v}")
    # print(dist)

    # ステップ2
    # 頂点vを始点とする辺に対し、distの更新をする。
    # 元々のdistの値と、頂点vのdistにv-e間の距離足した値を比較する。
    # 小さい方を新しいdistとして採用する。
    for e in G[v]:
        dist[e.end] = min(dist[e.end], dist[v] + e.leng)

    # 操作 3. を実行する (頂点 v への最短距離が確定したことを表す)
    done[v] = True

# 答えを出力する
for i in range(N):
    print(dist[i])
