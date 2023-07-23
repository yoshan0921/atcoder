import collections
import io
import sys

_INPUT = """\
8
3 7 4 7 3 3 8 2
"""
sys.stdin = io.StringIO(_INPUT)

# N = int(input())
# A = list(map(int, input().split()))

# G = []
# for i in range(len(A)):
#     G.append([i+1, A[i]])
# # print(G)

# checked = [False] * (N+1)
# count = 0
# node = []
# i = 4
# while True:
#     set_node = set(node)
#     if i in set_node:
#         idx = node.index(i)
#         count = len(node) - idx
#         print(count)
#         print(*node[idx:])
#         break
#     node.append(i)
#     i = G[i-1][1]

N = int(input())
A = list(map(int, ("0 " + input()).split()))
# print(A)
now = 1
for _ in range(N):
    now = A[now]  # 予めN回移動する
# print("now=" + str(now))
B = []
while A[now] != 0:
    A[now], now = 0, A[now]
    # print(A[now], now)
    B.append(now)
    # print(A)
print(len(B))
print(*B)
