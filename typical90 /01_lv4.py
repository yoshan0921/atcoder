import io
import sys

_INPUT = """\
3 34
1
8 13 26
"""
sys.stdin = io.StringIO(_INPUT)


def check(l: int, data: list, value: int):
    prev = 0
    piece = 0
    for i in range(len(data)):
        if data[i] - data[prev] >= l:
            piece += 1
            prev = i

    if data[-1] - data[prev] >= l:
        piece += 1

    if piece >= value + 1:
        return True
    else:
        return False


def binary_search_v3(data: list, value: int):
    left = -1
    right = data[-1]
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid, data, value):
            left = mid
        else:
            right = mid
    return left


if __name__ == "__main__":
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    A.append(L)
    result = binary_search_v3(A, K)
    print(result)
