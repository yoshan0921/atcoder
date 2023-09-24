import bisect
import collections
import itertools
# ==========================================================
# 累積和

print("\n累積和")
test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = itertools.accumulate(test_data)
print(list(result))

# ==========================================================
# 二分探索 - bisectモジュール
# bisectを使う時、入力するリストはすでにソート済みであることが前提。
# bisect_leftは、指定値が既にリストにある場合に前に挿入する。
# bisect_rightは、指定値が既にリストにある場合に後ろに挿入する。

print("\n二分探索 - bisectモジュール ")
test_data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
result1 = bisect.bisect_left(test_data, 5)
result2 = bisect.bisect_right(test_data, 5)
print(result1)
print(result2)

# リストへの挿入まで行う場合はinsortを使う。
test_data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
bisect.insort_left(test_data, 5)
print(test_data)

test_data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
bisect.insort_right(test_data, 5)
print(test_data)

# ==========================================================
# キュー
# queueはスレッドセーフ
# dequeはスレッドアンセーフではない？
# dequeの方が処理は高速

print("\nキュー - deque")
deque = collections.deque([0, 1, 2, 3, 4, 5])

# 追加
deque.append("a")
deque.appendleft("b")
print(deque)

# 取り出し
result1 = deque.pop()
result2 = deque.popleft()
print(result1, result2)

# ==========================================================
# 辞書 - defaultdict
# <list> or <dict> = collections.defaultdict(<型>)

print("\n辞書 - defaultdict")
dict_int = collections.defaultdict(int)
dict_list = collections.defaultdict(list)
dict_set = collections.defaultdict(set)

dict_int[1] = 123
dict_list[1] = [1, 2, 3]
dict_set[1] = {1, 2, 3}
dict_list[1].append(4)
dict_set[1].add(3)
print(dict_int)
print(dict_list)
print(dict_set)

# 辞書のフィルター
# valueにblueを含むキーを抽出

print("\n辞書 - valueにblueを含むキーを抽出")
dict_set = collections.defaultdict(set)
test_data = [(1, 'red'), (2, 'blue'), (3, 'green'),
             (1, 'green'), (3, 'blue'), (2, 'yellow')]
for k, v in test_data:
    dict_set[k].add(v)
print(dict_set)

dict_filtered = dict(filter(lambda item: 'blue' in item[1], dict_set.items()))
print(dict_filtered)

# 辞書のソート
# マイナスをつけると降順になる

dict_sorted = dict(sorted(dict_filtered.items(), key=lambda x: x[0]))
print(dict_sorted)
dict_sorted = dict(sorted(dict_filtered.items(), key=lambda x: -x[0]))
print(dict_sorted)

# dict型に変換しない場合はタプルが返ってくる
dict_sorted = sorted(dict_filtered.items(), key=lambda x: -x[0])
print(dict_sorted)

# ==========================================================
# 2次元リストのソート
# i[0]は昇順、i[1]は降順

print("\n2次元リストのソート")
test_data = [[1, 2], [1, 7], [1, 6], [2, 5], [2, 6]]
result = sorted(test_data, key=lambda i: (i[0], -i[1]))
print(result)


# ==========================================================
# カウント

print("\nカウント")
result = collections.Counter(
    ['a', 'a', 'b', 'd', 'e', 'a', 'z', 'e', 'b', 'a', 'c', 'b'])
print(result)
print(result['a'])

# ==========================================================
# グラフ

print("\n無向グラフ")
test_data = [[1, 2], [1, 3], [1, 4], [3, 4], [5, 6], [5, 7], [2, 7]]
dict = collections.defaultdict(list)
for a, b in test_data:
    dict[a].append(b)
    dict[b].append(a)
print(dict)
print(dict[1])

print("\n有向グラフ")
test_data = [[1, 2], [1, 3], [1, 4], [3, 4], [5, 6], [5, 7], [2, 7]]
dict = collections.defaultdict(list)
for a, b in test_data:
    dict[a].append(b)
print(dict)
print(dict[1])

# ==========================================================
# 組み合わせ

print("\n組み合わせ")
data = ['x1', 'x2', 'x3']
data = list(itertools.combinations(data, r=2))
print(data)

data = ['x1', 'x2', 'x3']
data = list(itertools.permutations(data, 2))
print(data)

# ==========================================================
# 10→2進進変換

print("\n10→2進進変換")
bin_str = format(57, 'b')
print(bin_str)

# ==========================================================
# 2進→10進変換

print("\n2→10進進変換")
bin_num = int('100010101', 2)
print(bin_num)

# ==========================================================
# 文字列操作

print("\n文字列の反転")
s1 = 'ABCDE'
s2 = s1[::-1]

print(s1)  # => "ABCDE"
print(s2)  # => "EDCBA"

print("\n文字列のスライス（前から）")
s1 = 'ABCDE'
s2 = s1[:3]

print(s1)  # => "ABCDE"
print(s2)  # => "EDCBA"

print("\n文字列のスライス（後から）")
s1 = 'ABCDE'
s2 = s1[-3:]

print(s1)  # => "ABCDE"
print(s2)  # => "EDCBA"

# # lambda式(1)
# prices = [3000, 2500, 10500, 4300]
# paymentList = list(map(lambda i: i*1.08, prices))
# print(paymentList)

# # lambda式(2)
# greeting = (lambda name: 'Hello ' + name)
# print(greeting("Yosuke"))
