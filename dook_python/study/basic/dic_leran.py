dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

# print("dict['Age']: ", dict['Age1'])

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del dict['Name']  # 删除键 'Name'
print(dict)
dict.clear()  # 清空字典
# del dict  # 删除字典

# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])

#字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

dict = {'Name': 'Zara', 'Age': 7}

print ("字典长度 : %d" %  len(dict))
dict.clear()
print ("字典删除后长度 : %d" %  len(dict))



dict1 = {'user': 'runoob', 'num': [1, 2, 3]}

dict2 = dict1  # 浅拷贝: 引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用

# 修改 data 数据
dict1['user'] = 'root'
dict1['num'].remove(1)

# 输出结果
print(dict1)
print(dict2)
print(dict3)

seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print("新的字典为 : %s" % str(dict))

dict = dict.fromkeys(seq, 10)
print("新的字典为 : %s" % str(dict))


dict = {'Name': 'Runoob', 'Age': 27}

print ("Age 值为 : %s" %  dict.get('Age'))
print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))


dict = {'Name': 'Runoob', 'Age': 7}
for i,j in dict.items():
    print(i, ":\t", j)

dict = {'Name': 'Runoob', 'Age': 7}
dict2 = {'Sex': 'female'}
dict['a']=123

dict.update(dict2)
print("更新字典 dict : ", dict)


site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print(pop_obj)