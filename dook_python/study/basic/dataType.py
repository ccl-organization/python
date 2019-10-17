# !/usr/bin/python3



''' 
基本数据类型
字符串
数字
列表 [1,'a']   list
元组 (1,'a')   数组
Set（集合）  {1,'a'}  hashset
Dictionary（字典）   {'a':'钩子',1:'b'}    map



# str = 'Runoob'
print(str)  # 输出字符串
print(str[0:]) # 输出第N 个到结尾
print(str[0:-2])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nruno\nob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

input("\n\n按下 enter 键后退出。")


# !/usr/bin/python3

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

list[0:2]=[]
print(list)



input = 'I like runoob'
inputWords = input.split(" ")
# 翻转字符串
# 假设列表 list = [1,2,3,4],
# list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
# inputWords[-1::-1] 有三个参数
# 第一个参数 -1 表示最后一个元素
# 第二个参数为空，表示移动到列表末尾
# 第三个参数为步长，-1 表示逆向
inputWords = inputWords[-1::-1]

# 重新组合字符串
output = ' '.join(inputWords)
print(output)


# !/usr/bin/python3

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号



student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a 和 b 的差集

print(a | b)  # a 和 b 的并集

print(a & b)  # a 和 b 的交集

print(a ^ b)  # a 和 b 中不同时存在的元素



dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict)
print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

'''

# 转为int   int('X',base)  把base进制到X转为10进制到int

i=int('10',2)
i=int('100')
print(i)

f=float('10')
print(f)

s = 'RUNOOB'
s1=str(s)
dict1 = {'runoob': 'runoob.com', 'google': 'google.com'};
s2=str(dict1)
print(s1)
print(s2)

#repr() 函数将对象转化为供解释器读取的形式。
dict1 = {'runoob': 'runoob.com', 'google': 'google.com'};
r1=repr(dict1)
print(r1)

#eval() 函数用来执行一个字符串表达式，并返回表达式的值。
x = 7
e1=eval( '3 * x' )

e2=eval('pow(2,2)')
print(e1,e2)

#tuple 函数将列表转换为元组。

list1= ['Google', 'Taobao','Taobao', 'Runoob', 'Baidu']
tuple1=tuple(list1)
print(tuple1)

#list() 方法用于将元组或字符串转换为列表。
#注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print ("列表元素 : ", list1)

str="Hello World"
list2=list(str)
print ("列表元素 : ", list2)

#set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
list1= ['Google', 'Taobao','Taobao', 'Runoob', 'Baidu']
set1=set(list1)
print(set1)

#dict() 函数用于创建一个字典。

dict()                        # 创建空字典
{}
dic1=dict(a='a', b='b', t='t')     # 传入关键字
print(dic1)
{'a': 'a', 'b': 'b', 't': 't'}
dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
{'three': 3, 'two': 2, 'one': 1} 
dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
{'three': 3, 'two': 2, 'one': 1}

#frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。

a = frozenset(range(10))     # 生成一个新的不可变集合
print(a)
# frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = frozenset('runoob')
print(b)
# frozenset(['b', 'r', 'u', 'o', 'n'])   # 创建不可变集合

#chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
chr1= chr(0x30), chr(0x31), chr(0x61)   # 十六进制
print(chr1)
chr2= chr(48), chr(49), chr(97)         # 十进制
print(chr2)

#ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
ord1=ord('a')
print(ord1)



