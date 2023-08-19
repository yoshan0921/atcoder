import io
import sys

_INPUT = """\
19876
"""
sys.stdin = io.StringIO(_INPUT)


# 約数一覧を出力する関数
def get_divisors_list(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if i**2 == num:
                continue
            divisors.append(int(num/i))
    return sorted(divisors)


if __name__ == "__main__":
    N = int(input())

    # 約数の個数を管理
    table = [0 for _ in range(N)]
    for i in range(1, N):
        table[i] = len(get_divisors_list(i))

    ans = 0
    # AB の値を全探索
    for i in range(1, N):
        ab = i
        cd = N-i
        ans += table[ab]*table[cd]

    print(ans)
