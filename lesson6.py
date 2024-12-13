# 6
print('666666 モジュールとパッケージ')

print('コマンドライン引数')
import sys
print(sys.argv)

# utilsをフルパスでimport
import lesson_pkg.utils
print(lesson_pkg.utils.say_twice('wwwww'))

# utilsをimport. as で別名もつけれるよ
from lesson_pkg import utils
print(utils.say_twice('aaaa'))

# 関数だけをimport この利用方法はあまり推奨されない
from lesson_pkg.utils import say_twice
print(say_twice('bbb'))



from lesson_pkg.talk import human
from lesson_pkg.talk import animal

human.cry()
animal.cry()


# 組み込み関数 sorted
print(globals())


ranking = {
    'A': 100,
    'B': 85,
    'C': 90
}

for key in ranking:
    print(key)

print(ranking.get('A'))
print(sorted(ranking, key=ranking.get, reverse=True))


# 標準ライブラリ
# collections, defaultdict,

s = 'alkdjfiejfalskdjflsa;gihw'

d={}
for c in s:
    if c not in d:
        d[c]=0
    d[c] = d[c] + 1
print(d)


d={}
for c in s:
    d.setdefault(c, 0)
    d[c] = d[c] + 1
print(d)

# 標準ライブラリ
from collections import defaultdict

d = defaultdict(int)
for c in s:
    d[c]+=1
print(d)
print(d['a'])


# PyPI (term color)
from termcolor import colored
print(colored('test','red'))



# import の順序の推奨 標準、外部、自作、設定の順番が良いと言われているよ
import collections
import os 
import sys

import termcolor

import lesson_pkg

import config

print(sys.path)
print(termcolor.__file__)
print(lesson_pkg.__file__)
print(config.__file__)

print(__name__)

