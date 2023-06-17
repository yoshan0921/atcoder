import bisect
import collections
import itertools

# 累積和
a1 = [1, 2, 3, 4, 5]
ret1 = itertools.accumulate(a1)
print(list(ret1))

# 二分探索
a2 = [1, 1, 2, 3, 4, 4, 4, 7, 8]
ret2 = bisect.bisect_left(a2, 4)
print(ret2)

a3 = [1, 1, 2, 3, 4, 4, 4, 7, 8]
ret3 = bisect.bisect_right(a3, 4)
print(ret3)

# キュー
dque = collections.deque([0, 1, 2, 3])
dque.append(4)
print(dque)
ret4 = dque.pop()
print(ret4)
dque.appendleft(4)
print(dque)
ret4 = dque.popleft()
print(ret4)

# カウント
ret5 = collections.Counter(
    ['a', 'a', 'b', 'd', 'e', 'a', 'z', 'e', 'b', 'a', 'c', 'b'])
print(ret5)
print(ret5['a'])

# 組み合わせ
a6 = ['x1', 'x2', 'x3']
ret6 = list(itertools.combinations(a6, r=2))
print(ret6)
print(ret6[0])
print(ret6[0][0])

# ソート
a7 = [[1, 2], [5, 7], [2, 6], [4, 5], [3, 6]]
a7.sort()
print(a7)

# 素数リスト
n = 100
primes = set(range(2, n+1))
for i in range(2, int(n**0.5+1)):
    primes.difference_update(range(i*2, n+1, i))
primes = list(primes)
print(primes)

# 内包表記
a8 = [x for x in range(10)]
print(a8)
a8 = [[0] for x in range(10)]
print(a8)

# 無向グラフ
a9 = [[1, 2], [1, 3], [1, 4], [3, 4], [5, 6], [5, 7], [2, 7]]
adj = collections.defaultdict(list)
for a, b in a9:
    adj[a].append(b)
    adj[b].append(a)
print(adj)
print(adj[1])

# 有向グラフ
a9 = [[1, 2], [1, 3], [1, 4], [3, 4], [5, 6], [5, 7], [2, 7]]
adj = collections.defaultdict(list)
for a, b in a9:
    adj[a].append(b)
print(adj)
print(adj[1])

# lambda式(1)
prices = [3000, 2500, 10500, 4300]
paymentList = list(map(lambda i: i*1.08, prices))
print(paymentList)

# lambda式(2)
greeting = (lambda name: 'Hello ' + name)
print(greeting("Yosuke"))

# *演算子でリストの要素を展開する
list1 = [0, 1, 2]
list2 = [3, 4, 5]
result = [*list1, *list2]
print(result)

# dictの初期化
# <list> or <dict> = [<式> for <変数> in <反復可能オブジェクト>]
dict = {key+1: 0 for key in range(5)}
print(dict)

# dictのソート
# ソート後はタプルになる。
ans = sorted(dict.items(), key=lambda i: i[1])
print(ans)
