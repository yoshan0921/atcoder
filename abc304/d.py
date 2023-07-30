import bisect
import collections
import io
import sys

_INPUT = """\
4 4
4
1 1
3 1
3 3
1 3
1
2
1
2
"""
sys.stdin = io.StringIO(_INPUT)

W, H = map(int, input().split())
N = int(input())
sb = [list(map(int, input().split())) for _ in range(N)]
sb_sorted = sorted(sb)

# print(sb_sorted)
# sb_set = set(sb)
# print(sb_set)

A = int(input())
x_line = list(map(int, input().split()))
x_line.append(W)
B = int(input())
y_line = list(map(int, input().split()))
y_line.append(H)

ans = collections.defaultdict(int)
for i in range(N):
    x = bisect.bisect_left(x_line, sb_sorted[i][0])
    y = bisect.bisect_left(y_line, sb_sorted[i][1])
    ans[(x, y)] += 1

# for i in x_line:
#     for j in y_line:
#         ans[str(i)+'_'+str(j)] = 0
# print(ans)

# for x in x_line:
#     check_list = []
#     for i in sb_sorted[:]:
#         if i[0] <= x:
#             check_list.append(i)
#         else:
#             break

#     for y in y_line:
#         for j in check_list[:]:
#             if j[1] <= y:
#                 ans[str(x)+'_'+str(y)] += 1
#                 sb_sorted.remove(j)
#                 check_list.remove(j)
#             # else:
#             #     ans[str(x)+'_'+str(y)] = 0

# print(len(ans))
# print(ans)
if len(ans) < (A+1)*(B+1):
    print(0, max(ans.values()))
else:
    print(min(ans.values()), max(ans.values()))
