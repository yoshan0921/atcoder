import io
import sys

_INPUT = """\
2021 617
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
if N == 1:
    ret = K
else:
    ret = (K * (K-1) * pow(K-2, N-2, 10**9+7)) % (10**9+7)
print(ret)
