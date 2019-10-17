#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 这里演示的是去重功能
{'orange', 'banana', 'pear', 'apple'}
'orange' in basket  # 快速判断元素是否在集合内
True
'crabgrass' in basket
False

# 下面展示两个集合间的运算.
...
a = set('abracadabra')
b = set('alacazam')
a
{'a', 'r', 'b', 'c', 'd'}
a - b  # 集合a中包含而集合b中不包含的元素
{'r', 'd', 'b'}
a | b  # 集合a或b中包含的所有元素
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b  # 集合a和b中都包含了的元素
{'a', 'c'}
a ^ b  # 不同时包含于a和b的元素
{'r', 'd', 'b', 'm', 'z', 'l'}




thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
thisset.update('abc')
print(thisset)
{'Taobao', 'Facebook', 'Google', 'Runoob'}

thisset.remove("Taobao")
print(thisset)
l1=len(thisset)
print(l1)
thisset.clear()
print(thisset)

x = {"apple", "banana", "cherry",'cherry'}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

# x.remove('apple')
# 该方法不同于 remove() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会。
x.discard("banana")
print(x,x.__len__())


