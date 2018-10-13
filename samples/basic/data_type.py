#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# number
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
a = 111
print('%d is a int variable' % a, isinstance(a, int))

# isinstance 和 type 的区别在于:type()不会认为子类是一种父类类型


class A:
    pass


class B(A):  # B是A的子类
    pass


print(isinstance(A(), A), end=" ")  # returns True
print(type(A()) == A, end=" ")      # returns True
print(isinstance(B(), A), end=" ")    # returns True
print(type(B()) == A)        # returns False

a = 2 / 4  # 除法，得到一个浮点数
print('2 / 4 = ', a)
a = 2 // 4  # 除法，得到一个整数
print('2 // 4 = ', a)
a = 2 ** 5  # 乘方
print('2 ** 5 = ', a)

# string 索引值以 0 为开始值，-1 为从末尾的开始位置
str = 'Runoob'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])

# list: 内容是可变的
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表
list[1:4] = []
print(list)

# tuple: 元组的元素不能更改
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组
tup1 = ()    # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号

# set: 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
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
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素

# Dictionary: 用"{ }"标识，它是一个无序的键(key) : 值(value)对集合，在同一个字典中，键(key)必须是唯一的
dict = { }
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{x: x**2 for x in (2, 4, 6)}
dict(Runoob=1, Google=2, Taobao=3)
