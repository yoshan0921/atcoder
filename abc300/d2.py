import itertools
import math
import io
import sys

_INPUT = """\
100
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
# sqrt(N) 以下の素数の列挙
sieve = [1] * (math.isqrt(N) + 1)
primes = []

for p in range(2, len(sieve)):
    if sieve[p] == 0:
        continue
    primes.append(p)
    for j in range(p * p, len(sieve), p):
        sieve[j] = 0

print(sieve)
print(primes)


# prefix_sum[n] : (n 以下の素数の個数)
prefix_sum = sieve
for i in range(len(prefix_sum) - 1):
    prefix_sum[i + 1] += prefix_sum[i]

print(prefix_sum)

ans = 0
# a, b を全探索する
for i in range(len(primes)):
    a = primes[i]
    if a * a * a * a * a >= N:
        break
    for j in range(i + 1, len(primes)):
        b = primes[j]
        if a * a * b * b * b >= N:
            break
        ans += prefix_sum[math.isqrt(N // (a * a * b))] - prefix_sum[b]
print(ans)
