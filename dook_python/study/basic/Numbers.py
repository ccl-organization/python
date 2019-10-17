#!/usr/bin/python3

from math  import floor
from  random import choice


print ("abs(-40) : ", abs(-40))
print ("abs(100.10) : ", abs(100.10))
#floor(x) 返回数字的下舍整数，小于或等于 x。

print(floor(3.4))
print(floor(-3.4))

print ("从 range(100) 返回一个随机数 : ",choice(range(100)))
print ("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", choice([1, 2, 3, 5, 9]))
print ("从字符串中 'Runoob' 返回一个随机字符 : ", choice('Runoob'))

#randrange() 方法返回指定递增基数集合中的一个随机数，基数默认值为1。
import random

# 从 1-100 中选取一个奇数
print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))

# 从 0-99 选取一个随机数
print("randrange(100) : ", random.randrange(100))

import random

list = [20, 16, 10, 5];
random.shuffle(list)
print("随机排序列表 : ", list)

random.shuffle(list)
print("随机排序列表 : ", list)