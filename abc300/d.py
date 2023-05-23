import itertools
import math
import io
import sys

_INPUT = """\
1000000000
"""
sys.stdin = io.StringIO(_INPUT)


def get_prime(n):
    if n <= 1:                  # 1以下の場合
        return []               # 空リストを返す
    prime = [2]                 # 素数リストを 2 だけで作成
    limit = int(math.sqrt(n))   # 検索する上限を設定(nの平方根)
    print("limit=" + str(limit))

    # 奇数のリストを作成, Range(start, stop, step)
    data = [i for i in range(3, limit, 2)]

    while limit >= data[0] and len(data) > 1:                 # 上限≧奇数の先頭の場合
        prime.append(data[0])               # 素数リストに奇数の先頭を追加
        # 奇数リストのうち、先頭の数で割り切れないものでリストを作成
        data = [j for j in data if j % data[0] != 0]
        print(data)

    return prime + data       # 素数リストと奇数のリストを合わせて返す


if __name__ == "__main__":
    N = int(input())

    sieve = [1] * (math.isqrt(N) + 1)
    prime = []
    for p in range(2, len(sieve)):
        if sieve[p] == 0:
            continue
        prime.append(p)
        for j in range(p * p, len(sieve), p):
            sieve[j] = 0

    print(sieve)
    # print(prime)

    prefix_sum = sieve
    for i in range(len(prefix_sum) - 1):
        prefix_sum[i + 1] += prefix_sum[i]

    print(prefix_sum)

    # # limit = int(math.sqrt(N / 12))
    # prime = get_prime(N)

    # # prime = list(filter(lambda x: x <= limit, ret))
    # # print(prime)

    # combination = list(itertools.combinations(range(len(prime)), 3))
    # # print(combination)

    # count = 0

    # for i in combination:
    #     # print(i)
    #     ret1 = prime[i[0]]**2
    #     # print("ret1=" + str(ret1))
    #     if ret1 < N:
    #         ret2 = ret1 * prime[i[1]]
    #         # print("ret2=" + str(ret2))
    #         if ret2 < N:
    #             ret3 = ret2 * prime[i[2]]**2
    #             # print("ret3=" + str(ret3))
    #             if ret3 <= N:
    #                 count += 1
    #                 # print(prime[i[0]], prime[i[1]], prime[i[2]])
    # else:
    #     print(count)
