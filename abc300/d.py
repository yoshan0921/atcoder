import itertools
import math
import io
import sys

_INPUT = """\
1000000000
"""
sys.stdin = io.StringIO(_INPUT)


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
    N = int(input())
    prime = get_prime_v2(1000000)

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
