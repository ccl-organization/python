# -- coding:utf-8 --
# str = input("请输入:")
# print("你输入的内容是: ", str)

fo = open("/Users/chenyahui/dook_python/data/foo.txt", "wb")

fo.write("www.runoob.com!\nVery good site!\n");

# 关闭打开的文件

fo.close()


fo = open("/Users/chenyahui/dook_python/data/foo.txt", "r+")

str = fo.read(100);     #这里的参数10表示的是被读取的字节数

print("your input  str is  : ", str)

# 关闭打开的文件

fo.close()