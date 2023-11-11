import io
import sys
import heapq


_INPUT = """\
4 3
1 2 314
1 3 159
1 4 265
"""
sys.stdin = io.StringIO(_INPUT)


class edge:
    # 辺情報を表す構造体
    def __init__(self, end, leng):
        self.end = end      # 辺の終点
        self.leng = leng    # 辺の重み


INF = 10**9  # 変数初期化用


def dijkstra(G, s):
    # done[i]：頂点iの最短距離が確定しているかどうかを表すリスト
    done = [False for _ in range(N)]
    # dist[i]：頂点0から頂点iへの暫定的な経路長
    dist = [INF for _ in range(N)]
    dist[s] = 0

    hq = []  # (仮の最短距離、頂点番号) を管理するヒープ
    heapq.heapify(hq)

    # ヒープに最初の時点における情報を入れておく
    for v in range(N):
        heapq.heappush(hq, (dist[v], v))

    while hq:
        # ヒープから最小の距離の頂点を取り出す
        d, v = heapq.heappop(hq)

        # 頂点vの最短距離がすでに確定しているなら、何もしない
        if done[v]:
            continue

        # print(f"最小距離の頂点={v}")
        # print(dist)

        # ステップ2
        # 頂点vを始点とする辺に対し、distの更新をする。
        # 元々のdistの値と、頂点vのdistにv-e間の距離足した値を比較する。
        # 小さい方を新しいdistとして採用する。
        for e in G[v]:
            dist[e.end] = min(dist[e.end], dist[v] + e.leng)
            heapq.heappush(hq, (dist[e.end], e.end))

        # 操作 3. を実行する (頂点 v への最短距離が確定したことを表す)
        done[v] = True

    return dist


if __name__ == "__main__":

    # 入力を受け取る
    N, M = map(int, input().split())

    G = [[] for _ in range(N)]
    for i in range(M):
        u, v, w = map(int, input().split())
        G[u-1].append(edge(v-1, w))
        G[v-1].append(edge(u-1, w))

    ret_front = dijkstra(G, 0)
    ret_back = dijkstra(G, N-1)

    for i in range(N):
        print(ret_front[i] + ret_back[i])
