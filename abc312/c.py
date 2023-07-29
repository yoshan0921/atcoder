import bisect
import io
import sys

_INPUT = """\
2 2
80
100 200
"""
sys.stdin = io.StringIO(_INPUT)

# 条件：
# りんごを X 円以上で売ってもよいと考える売り手の人数が、
# りんごを X 円以下で買ってもよいと考える買い手の人数以上である。

# N: 売り手
# M: 買い手
N, M = map(int, input().split())

# 売り手の情報
N_info = list(map(int, input().split()))
M_info = list(map(int, input().split()))
N_info.sort()
M_info.sort()

param = N_info.copy()
for i in M_info:
    param.append(i + 1)

param_set = set(param)
param_list = list(param_set)
param_list.sort()

ans = 0

for i in param_list:
    ret_N = bisect.bisect_right(N_info, i)
    ret_M = M - bisect.bisect_left(M_info, i)
    if ret_N >= ret_M:
        ans = i
        break

print(ans)
