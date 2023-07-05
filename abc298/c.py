import collections
import io
import sys

_INPUT = """\
5
8
1 1 1
1 2 4
1 1 4
2 4
1 1 4
2 4
3 1
3 2
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
Q = int(input())
S = []

dict_box = collections.defaultdict(list)
dict_card = collections.defaultdict(set)

for i in range(Q):
    S = list(map(int, input().split()))
    if S[0] == 1:
        # 箱に何のカードが入っているのかを記録
        dict_box[S[2]].append(S[1])
        # カードがどの箱に入っているのかを記録
        dict_card[S[1]].add(S[2])
    elif S[0] == 2:
        print(*sorted(dict_box[S[1]]))
    elif S[0] == 3:
        print(*sorted(dict_card[S[1]]))
