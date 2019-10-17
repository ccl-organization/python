# !/usr/bin/python3

a = 21
b = 10

print(a*b)
#取整除 - 向下取接近除数的整数
print(a//b)
#幂 - 返回x的y次幂
print(a**b)

#除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
a = 10
b = 20
list = [1, 2, 3, 4, 5];

if (a in list):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if (b not in list):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if (a in list):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")


# id() 函数用于获取对象内存地址。
a = 20
b = 20
print(id(a),id(b))
if a is b:
    print('o')

#is 与 == 区别：
#is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
a=[1,b]
b=[1,b]
print(a==b)
print(a is b)


