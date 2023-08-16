import io
import sys

_INPUT = """\
6 6
3
2 3 6
3
2 4 6
2
3 6
3
1 5 6
3
1 3 6
2
1 4
"""
sys.stdin = io.StringIO(_INPUT)

# N以下の整数からなる集合がM個
N, M = map(int, input().split())
C = []
for i in range(M):
    dummy = int(input())
    C.append(set(map(int, input().split())))

answer = 0
for i in range(1 << M):

    # 表示用（何番目の組み合わせか）
    # print(f'{i} : ', end='')

    temp_set = set()

    # M個の集合の中からどれが選ばれているか（どのbitが1なのか）
    for j in range(M):

        # 選ばれているとき
        if i & (1 << j):

            # 表示用（選ばれている集合）
            # print(C[j], end=' ')
            temp_set.update(C[j])

    # 条件を満たしている場合カウントアップ
    # print(temp_set)
    if len(temp_set) == N:
        answer += 1

print(answer)
