# -- coding:utf-8 --
class Employee:
    empCount = 0

    def __init__(self, name, salary):  # 构造函数
        self.name = name  # 添加实例属性
        self.salary = salary  # 添加实例属性
        Employee.empCount += 1  # 修改类属性

    def displayCount(self):  # 添加实例方法
        print("TotalEmployee %d" % Employee.empCount)  # 读取类属性

    def displayEmployee(self):  # 添加实例方法
        print("Name:", self.name, ", Salary:", self.salary)  # 读取实例属性


# "创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
# "创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
s=emp1.__dict__()
print (s)
print("TotalEmployee %d" % Employee.empCount)
