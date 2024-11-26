print('04 lesson')

n = [1,2,3,4,12,1,2,3,4,5]




n.append(123)
n.insert(0,234)

n.remove(2)
n.remove(2)


print(n)



a = [1,2,3]
b = [4,5,6]

print(a)
print(b)

print(a+b)

a.extend(b)
print('a =', a )



# listのメソッド

r = [1,2,3,4,3,2,1]
print(r)
print(r.index(3))


print(r.count(4))


if 5 in r:
    print('in')
else:
    print('not in')


r.sort()
print(r)

r.sort(reverse=True)
print(r)


s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x=' '.join(to_split)
print(x)

# listのコピー
i = [1,2,3,4,5,6]
j = i #参照渡し
print(i)
print(j)

x1 = i.copy()
print('x1:', x1)

x2 = i[:]
print('x2:', x2)

print('リストやオブジェクトは参照渡し')

x=123
y=x
print(id(x), id(y))
y=213
print(id(x), id(y))

l1=[1,2,3]
l2=l1
print(id(l1), id(l2))
l2=l1.copy()
print(id(l1), id(l2))

#リストの使い方
# tuple (1,2,3,4) リストとの違いは変更可否　
# 変更されたくない場合はタプル
t = (1,2,3,4,5)
print(t)
print(t[-1])


t1 = 1,
t2 = 1
t3 = ()
t4 = (1,2,3)
print(t1, t2, t3, t4)


print(t4[0]+30)

t5 = t4 + t3
print(t5)


# タプルのアンパッキング

nums = (10,20)
print(nums)

x, y = nums
print(x, y)

i, j = 1,2
print(i,j)
j,i = i, j
print(i,j)

# 23
chose_from_two = ('A','B','C')
print(chose_from_two)

answer = []
answer.append('A')
answer.append('B')
print(answer)

# dict 辞書
d = { 'x': 10, 'y': 20}
print(d)
print(d['x'])
print(d['y'])
print(d)


d2 = dict(a=123,b=234)
print(d2)
#help(d2)


d1 = { 'x': 100, 'y': 200 }
print(d1)
d2 = { 'x': 500, 'z': 1000 }
print(d2)
d1.update(d2)
print(d1)

print(d1['x'])
print(d1['z'])


print(d1.get('x'))
print(d1.get('y'))
print(d1.get('z'))

# print(d1['xyz']) # will be KeyError
print(d1.get('xyz')) # will be None


d1.pop('x')
print(d1)
del d1['y']
print(d1)

d1.clear()
print(d1)

d1 = { 'a': 1 }
print('a' in d1)
print('b' in d1)


#
x = {'a':1, 'b':2}
y = x #参照渡し

y = x.copy() #値渡し


fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300
}

print(fruits['apple'])

fruitsx = {
    'apple': {},
    'banana': {},
    'orange': {}
}
print(fruitsx)

# 集合 set
a={1,2,3,4, 4,3,2,1,9,8}
print(type(a), a)
b={2,4,3,5,7}
c=a-b
print(c)
d=b-a
print(d)
e = a & b
print(e)
f = a | b
print(f)
g = a ^ b
print(g)


s = {1,2,3,4,5}
print(s)
s.add(6)
print(s)
s.add(6)
print(s)
s.remove(6)
print(s)
s.clear()
print(s)

# 共通点を見つける
friendsA = {'A', 'B', 'C'}
friendsB = {'D', 'B', 'E'}
print(friendsA & friendsB)

# listをSetにすると重複を除く
l = ['A', 'B', 'B', 'C', 'C', 'D']
print(l)
s = set(l)
print(s)

# コメント
"""
複数行のコメント
これもコメント
これもコメント
これもコメント
"""


# バックスラッシュで改行 opt + ¥
s = 'aaaaaaaa' \
    + 'bbbbbbbb'
print(s)

s = ('aaaaaaaa' 
    + 'bbbbbbbb')
print(s)

# if文
x = -10
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positie')

# 論理演算子

# enumerate関数
# zip関数

# dictをForループで処理
d = { 'x': 100, 'y': 200}
print(d)

for k, v in d.items():
    print(k, v)

# 関数定義
def functest():
    print('hi')

functest()
print(type(functest))

f = functest
f()


#def test_func(x, l=[]):
def test_func(x, l=None):    
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func(100)
print(r)
r = test_func(100)
print(r)

def say_something(word, *args): #tupleにして受け取れる
    print(word)
    print(args) 
    print(type(args))
    for arg in args:
        print(arg)
say_something('aaaa', 'b', 'test')

def menu(word, **kwargs):
    """ここに関数の説明
    """
    print(kwargs)
    print(type(kwargs))
    for k, v in kwargs.items():
        print(k, v)

menu('aaaa', entree='beef', drink='tea')


def outer(a, b):
    # inner func
    def plus(c, d):
        return c + d
    r = plus(a, b)
    print(a,b)

outer(1,2)

# closer
def outer(a, b):
    def inner():
        return a + b
    return inner

print(outer(1,2)())


#デコレーター
def print_info(func):
    def wrapper(*args, **kwargs):
        print('# start #')
        result = func(*args, **kwargs)        
        print('# end #')
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

#print(print_info(add_num)(10,201))
print(add_num(10,20))


# ラムダ
l = ['Mon', 'tue', 'wed', 'thu', 'fri', 'SAT', 'sun']
print(l)

def change_words(words, func):
    for w in words:
        print(func(w))

def sample_func(word):
    return word.capitalize()

change_words(l, sample_func)
change_words(l, lambda w: w.capitalize())
change_words(l, lambda w: w.lower())

# ジェネレーター yeildの利用
l = ['good aaaa','good bye','good bbbbb']
for i in l:
    print(i)

def greet():
    yield 'good aaa'
    yield 'good bbb'
    yield 'good ccc'

for g in greet():
    print(g)

print('###########################')
g = greet()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

# リスト内包表記 リストの生成
t = (1,2,3,4,5,6)
print([i for i in t if i % 2 == 0])

t2 = (5,6,7,8,9,10)
print([i*j for i in t for j in t2]) # わかりにくくなるので利用しても１つまで
