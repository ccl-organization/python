# !/usr/bin/python
# -*- coding: UTF-8 -*-

print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

# str = input("请输入：");
# print ("你输入的内容是: ", str)


# 打开一个文件
path="/Users/chenyahui/codes/dook_python/data/learn/foo.txt"
f = open(path, "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()


f = open(path, "r")

str = f.read()
print(str)

# 关闭打开的文件
# f.close()


str = f.readline()
print(str)

# 关闭打开的文件
# f.close()



# f = open("/tmp/foo.txt", "r")

for line in f:
    print(line, end='')

# 关闭打开的文件
f.close()