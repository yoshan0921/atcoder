import math
import io
import sys
import bisect
import collections
import itertools
sys.setrecursionlimit(10**9)

_INPUT = """\
8 28 936294041850197
1 2 473294720906780
1 3 743030800139244
1 4 709363019414774
1 5 383643612490312
1 6 557102781022861
1 7 623179288538138
1 8 739618599410809
2 3 857687812294404
2 4 893923168139714
2 5 581822471860662
2 6 740549363586558
2 7 307226438833222
2 8 447399029952998
3 4 636318083622768
3 5 44548707643622
3 6 307262781240755
3 7 12070267388230
3 8 700247263184082
4 5 560567890325333
4 6 704726113717147
4 7 588263818615687
4 8 549007536393172
5 6 779230871080408
5 7 825982583786498
5 8 713928998174272
6 7 751331074538826
6 8 449873635430228
7 8 11298381761479
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    from heapq import heappush, heappop

    n, m, k = map(int, input().split())

    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v, w = map(int, input().split())

        graph[u-1].append((v-1, w))  # u->vの辺
        graph[v-1].append((u-1, w))  # v->uの辺

    # プリム法
    # 頂点がマークされているか確認する配列
    marked = [False for _ in range(n)]

    # マークされている頂点数を数える
    marked_cnt = 0

    # はじめに0頂点をマーク
    marked[0] = True
    marked_cnt += 1

    # heap
    q = []

    # 頂点0に隣接する辺を保存
    for j, c in graph[0]:
        heappush(q, (c, j))

    total = 0

    # すべての頂点をマークするまでwhileループ
    while marked_cnt < n:
        # 最小の重みの辺をheapで取り出す
        c, i = heappop(q)

        # マークされているならスキップ
        if marked[i]:
            continue

        # 頂点をマーク
        marked[i] = True
        marked_cnt += 1

        total += c

        # 頂点iに隣接する辺を保存
        for j, c in graph[i]:
            # マークされていればスキップ
            if marked[j]:
                continue

            heappush(q, (c, j))

    print(total % k)


if __name__ == '__main__':
    main()
