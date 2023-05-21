import io
import sys
import bisect

_INPUT = """\
?0?10??0??0???0??0??0??0???0??0??0??0??
100
"""
sys.stdin = io.StringIO(_INPUT)

S = list(input())
N = int(input())

# check if S includes "?"
if "?" not in S:
    ret = int("".join(S), 2)
    if ret <= N:
        print(ret)
    else:
        print(-1)
    exit()

# convert all ? to 0
S_test = S.copy()
for a in range(len(S_test)):
    if S_test[a] == "?":
        S_test[a] = "0"

if int("".join(S_test), 2) > N:
    print(-1)
    exit()

c_str = []
n = len(S)
for i in range(N):
    # if i > N:
    #     continue
    i_bin = list(str(format(i, 'b').zfill(n)))
    for (j, k) in zip(i_bin, S):
        if k == "?":
            continue
        if j != k:
            break
    else:
        c_str.append(int("".join(i_bin), 2))
        # print(c_str)

ret = bisect.bisect(c_str, N)
if ret == 0:
    print(-1)
else:
    print(c_str[ret-1])
