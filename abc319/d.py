import io
import sys
# import bisect
# import collections
# import itertools

_INPUT = """\
5 5
5 5 5 5 5
"""
sys.stdin = io.StringIO(_INPUT)

INF = 10**9


def calc_line(data, line_limit):
    if max(data) > line_limit:
        return INF

    # 横幅を特定文字通に固定した時に何行必要になるかを返す
    line_num = 1
    line_word_count = 0
    for word in data:
        # 最初の単語の場合
        if line_word_count == 0:
            line_word_count = word
            continue

        line_word_count += 1 + word

        # 1行の文字数がline_limitを超えたら、次の行に移る
        if line_word_count > line_limit:
            # 収まらなかった単語を次の行に移す
            line_num += 1
            line_word_count = word
    return line_num


def binary_search_v2(data: list, value: int):
    """
    left は「常に」条件を満たさない
    right は「常に」条件を満たす
    right - left = 1 になるまで範囲を狭める (最後は right が条件を満たす最小)
    """
    # 最長の単語の長さ
    left = 0  # max(data)
    # 全ての単語の長さの和＋空白の数（１行に全て収まる場合）
    right = sum(data) + N - 1

    # 二分探索
    while right - left > 1:
        mid = (left + right) // 2

        # print("**********")
        # print(calc_line(data, mid))
        # print("**********")

        # 指定行数以下に収まっている場合、さらに横幅を狭める
        if calc_line(data, mid) <= value:
            right = mid
        else:
            # 指定行数以下に収まっている場合、さらに横幅を広げる
            left = mid

        # print("**********")
        # print(left, mid, right)
        # print("**********")

    return right


N, M = map(int, input().split())
L = list(map(int, input().split()))

ret = binary_search_v2(L, M)
# ret = calc_line(L, 6)
print(ret)
