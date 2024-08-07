

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


# 辞書型 dict
d = {'x': 10, 'y': 20}
print(d)
print(type(d))

print(d['x'])
print(d['y'])
