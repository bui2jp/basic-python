

#

num = 1
name = 'Taro'

print(num)
print(name)

print(num, type(num))
print(name, type(name))


name = num
print(num, type(num))
print(name, type(name))

print('Hi', 'test')

print(str(17/3))
print(str(17//3))


# 

import math
result = math.sqrt(25)
print(result)



# print(help(math))

# 文字列
s = 'test'
print(s)


# list

print('r.index')
r = [6,63,2,4,1,2,3,4,5,6,7,8,9]
print(r.index(1))
print(r.count(3))


if 50 in r:
    print('exist')


r.sort()
print(r)


r.sort(reverse=True)
print(r)


s = 'my name is mike'
print(s)
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)


#print(help(list))


# listのコピー
i = [1,2,3,4,5]
j = i
y = i.copy()
y = i[:] #これも値渡し

j[0] = 555
# リストなどは参照渡しだよ
print(i)
print(j)
print(y)

# 通常の変数は値渡しだよ
x = 123
y = x
y = 33
print(x, y)

# id
print(id(x))
print(id(y))


a = [1,2,3]
b = a
print(id(a)) # idは同じになる
print(id(b)) # idは同じになる


# リストの使い所
seat = []
print(seat)
min = 0
max = 5

seat.append('a')
seat.append('a')
seat.append('a')
seat.append('a')

if min <= len(seat) < max:
    print(True)
else:
    print(False)


# taple リストとの違いはアクセス方法かな
# データの書き換えはできないが、リストを入れることはできる

t = (1,2,3,4,5)
print(type(t))
print(t)
print(t[0])
print(t.count(2))

t = 123
print(t)

t = 123,
print(t)


new_tuple = (1,2,3) + (4,5,6)
print(new_tuple)


# tuple unpacking
num_tuple = (10,20)
print(new_tuple)

x, y = num_tuple
print(num_tuple)
print(x)
print(y)

# tupleが展開されてmin, maxへ代入される unpacking
min, max = 0, 100

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)


# tupleのつかいどころ tupleは中身を変更できない
chose_from_two = ("a","b","c")
answer = []
answer.append('A')
answer.append('B')
print(answer)


print('###')
print('辞書型 dict')

d = {'x': 10, 'y': 20}
print(d)
print(type(d))

print(d['x'])
print(d['y'])

# 辞書のコピー
d2 = d.copy()
d['x'] = 99
print(d)
print(d2)

# dictハッシュテーブルで管理されているのでリストの検索より早い

#集合 set
a = {1,2,3,4,5,5,5,5,2,2,3}
print(a)
print(type(a))

b = {2,4,5,8}
print(b)

print('#')
print('# list, tuple, dict, set のそれぞれの違い')
print('#')
# list
# 順序づけられたデータ
# インデックスでアクセス
l = ['python', 'Javascript', 'C++']
print(f'list: {l}')

# tuple
# 順序づけられたデータ
# インデックスでアクセス
# 変更不可　要素の追加や変更はできない
t=('python', 'Javascript', 'C++')
print(f'tuple: {t}')

# dict　辞書
# key: value形式のデータ
d = {'Japan':'jp', 'USA': 'en', 'China': 'zh'}
print(f'dict: {d}')

my_dict = {
    'aaa': 123,
    'bbb': 456,
    'ccc': 789,
    'aaa2': 123
}
print(f'my_dict: {my_dict}')
search_key = "aaa"
if search_key in my_dict:
    print('key exists.')
search_val = 123
# リスト内包表記
keys_with_value = [key for key, value in my_dict.items() if value == search_val]
print(f'keys_with_value: {keys_with_value}')

# set
# 集合を表す
set1 = {'v1', 'v2', 'v3', 'v1'}

print(f'set1: {set1}')
# print(f'pop: {set1.pop()}') # これはランダム
# print(f'remove: {set1.remove("v2")}')
print(f'set1: {set1}')

# set -> list リスト内包表記
#l1 = [i for i in set1 if i == 'v1']
l1 = [i for i in set1]
print(l1)
print(type(l1))

# set -> tuple
t1 = tuple(set1)
print(t1)
print(type(t1))
# 


# set -> dict
# listに直してからdictに変換
print(set1)

# to list
l1 = [i for i in set1]
print(l1)

# to dict キーと値は同じ
d1 = {k: k for k in l1} #これは辞書内包表記
print(d1)

# リスト内包表記とはリストを簡潔に作成する方法
# 辞書(dict)の場合は辞書内包表記
values = (1,2,3)
print(values, type(values))

# zipは複数のイテラブルを受け取りタプルを返す　
# zipはイテレータを返します
z = zip(values, set1) 

print(z)
d1 = dict(z)

print(d1, type(d1))
print(d1[1]) # dict
