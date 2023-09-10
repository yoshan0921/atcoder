import io
import sys
import bisect
import collections
import itertools

_INPUT = """\
7
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
ans = ["-" for _ in range(N+1)]


def get_divisors_list(num):
    # 約数一覧を出力する関数
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if i**2 == num:
                continue
            divisors.append(int(num/i))
    return sorted(divisors)


d = get_divisors_list(N)
# print(d)

for i in range(N+1):
    for j in d:
        if j > 9:
            break
        if i == 0:
            ans[i] = str(d[0])
            break
        elif i >= (N/j) and (i*j) % N == 0:
            ans[i] = str(j)
            break

print("".join(ans))
