import io
import re
import sys

_INPUT = """\
8
a(b(d))c
"""
sys.stdin = io.StringIO(_INPUT)


def remove_str_start_length(s, start, length):
    return s[:start] + s[start + length:]


N = int(input())
S = input()
# print(S)

regex = re.compile('\([a-z]*\)')

while True:
    # m = re.search('\([a-z]*\)', ret)
    m = regex.search(S)

    # if m:
    #     print(m.group())
    #     print(m.start())
    #     print(m.end())
    #     print(m.span())
    # else:
    #     break
    if not m:
        break

    S = remove_str_start_length(S, m.start(), m.end()-m.start())


print(S)
