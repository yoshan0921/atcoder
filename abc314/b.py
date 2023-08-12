import collections
import io
import sys

_INPUT = """\
4
3
7 19 20
4
4 19 24 0
2
26 10
3
19 31 24
19
"""
sys.stdin = io.StringIO(_INPUT)
N = int(input())
person_bet = collections.defaultdict(set)

for i in range(N):
    dummy = input()
    person_bet[i+1] = set(map(int, input().split()))

X = int(input())

# XにBetしている人を抽出
# XにBetしている人がいない場合は0を出力して終了
filterd_person = dict(filter(lambda item: X in item[1], person_bet.items()))
if len(filterd_person) == 0:
    print(0)
    exit(0)

# Betしている個数でソート
filterd_person2 = dict(sorted(filterd_person.items(), key=lambda x: len(x[1])))
min_value = len(list(filterd_person2.values())[0])

# Betしている個数が最小の人を抽出
filterd_person3 = dict(filter(lambda item: len(
    item[1]) == min_value, filterd_person2.items()))

# 回答出力
print(len(filterd_person3))
print(*filterd_person3.keys())
