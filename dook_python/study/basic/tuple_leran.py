tup1 = ('Google', 'Runoob', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";   #  不需要括号也可以
type(tup3)
print(tup1,tup2,tup3)

#元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tup1 = (50)
print(type(tup1))
tup1 = (50,)
print(type(tup1))

#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2;
print(tup3)


tup1 = ('Google', 'Runoob', 1997, 2000)
print(tup1)
del tup1
print("删除后的元组 tup : ")
print(tup1)
