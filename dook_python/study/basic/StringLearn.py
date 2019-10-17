# !/usr/bin/python3

var1 = 'Hello World!'
var2 = "Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print('\n aaa')
print(r'\n aaa')
print(R'\ naaa')


print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

#python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。实例如下
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

#Python 的字符串内建函数

str = "this is string example from runoob....wow!!!"

print ("str.capitalize() : ", str.capitalize())
str = "[www.runoob.com]"

print ("str.center(40, '*') : ", str.center(40, '*'))

str="www.runoob.com"
sub='o'
print ("str.count('o') : ", str.count(sub))

str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))

#snumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
str = "runoob2016"
print (str.isnumeric())

str = "2344341.34"
print (str.isnumeric())