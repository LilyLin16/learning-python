#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# python 函数的参数传递：
# 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。
#             比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
# 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响。


def changeInt(a):
    a = 10
    print(a)

# 实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，
# 按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，
# 则新生成一个 int 值对象 10，并让 a 指向它。
b = 2
changeInt(b)
print(b)   # 结果是 2


def changeme(mylist):
    # "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
print("初始值: ", mylist)
changeme(mylist)
print("函数外取值: ", mylist)


# 可写函数说明
def printinfo(name, age):
    print("名字: ", name)
    print("年龄: ", age)
    return


printinfo(age=50, name="runoob")


# 不定长参数: 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 加了两个星号 ** 的参数会以字典的形式导入。
def printinfo(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    print(vartuple)  # (60,50)
    for var in vartuple:
        print(var)
    return


printinfo(10)
printinfo(70, 60, 50)

total = 0  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    """"返回2个参数的和."""  # 函数的说明文档
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)  # 30
    return total


# 调用sum函数
sum(10, 20)
print(sum.__doc__)
print("函数外是全局变量 : ", total)  # 0


num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)   # 1
    num = 123
    print(num)  # 123


fun1()
print(num)  # 123
