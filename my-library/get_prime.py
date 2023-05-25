"""
Sieve of Eratosthenes（エラトステネスのふるい）
"""

import math


def get_prime(n):
    if n <= 1:                  # 1以下の場合
        return []               # 空リストを返す
    prime = [2]                 # 素数リストを 2 だけで作成
    limit = int(math.sqrt(n))   # 検索する上限を設定(nの平方根)
    print("limit=" + str(limit))

    # 奇数のリストを作成, Range(start, stop, step)
    data = [i for i in range(3, n, 2)]
    while limit >= data[0]:                 # 上限≧奇数の先頭の場合
        prime.append(data[0])               # 素数リストに奇数の先頭を追加
        # 奇数リストのうち、先頭の数で割り切れないものでリストを作成
        data = [j for j in data if j % data[0] != 0]

    return prime + data       # 素数リストと奇数のリストを合わせて返す


def get_prime_v2(limit):
    prime = []
    for i in range(2, limit):
        print(int(limit**0.5)+1)
        print("i=" + str(i))
        # for j in range(2, int(limit**0.5)+1):
        for j in range(2, i):
            print("j=" + str(j))
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime


if __name__ == "__main__":
    # print(get_prime(100))         # 100までの素数を求める
    print(get_prime_v2(10))         # 100までの素数を求める
