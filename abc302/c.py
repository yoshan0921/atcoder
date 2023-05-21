import itertools
import io
import sys

_INPUT = """\
4 4
bbed
abcd
abed
fbed
"""
sys.stdin = io.StringIO(_INPUT)


N, M = map(int, input().split())
S = [input() for i in range(N)]
# print(S)

pattern_list = list(itertools.permutations(S))
# print(pattern_list)

for i in pattern_list:
    flg = True
    # print("i=" + str(i))
    for j in range(N-1):
        # print(i[j], i[j+1])
        count = 0
        for k in range(M):
            if i[j][k] == i[j+1][k]:
                count += 1
        else:
            if count < M-1:
                # print("ng")
                flg = False
                break
            # else:
            #     print("ok")
    else:
        if flg == True:
            print("Yes")
            break
        # else:
        #     print("Failed")
else:
    print("No")
