import io
import sys

_INPUT = """\
3 100 50
60 20 40
"""
sys.stdin = io.StringIO(_INPUT)

N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

if P < min(D):
    print(P)
    exit(0)
else:
    if min(D)+Q < P:
        print(min(D)+Q)
        exit(0)
    else:
        print(P)
        exit(0)
