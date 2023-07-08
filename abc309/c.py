import bisect
import copy
import io
import sys

_INPUT = """\
15 158260522
877914575 2436426
24979445 61648772
623690081 33933447
476190629 62703497
211047202 71407775
628894325 31963982
822804784 50968417
430302156 82631932
161735902 80895728
923078537 7723857
189330739 10286918
802329211 4539679
303238506 17063340
492686568 73361868
125660016 50287940
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(reverse=True)
# print(AB)

Ans = []
Tmp = []
for i in range(N):
    if i == 0:
        Ans.append([AB[i][0], AB[i][1]])
        Tmp.append(AB[i][1])
    else:
        Ans.append([AB[i][0], Ans[i-1][1] + AB[i][1]])
        Tmp.append(Ans[i-1][1] + AB[i][1])

# print(Ans)
# print(Tmp)

ret = bisect.bisect_right(Tmp, K)
# print(ret)

if ret == N:
    print(1)
else:
    print(Ans[ret][0]+1)
