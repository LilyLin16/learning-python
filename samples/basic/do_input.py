#!/usr/bin/env python3

# -*- coding: utf-8 -*-

name = input("请输入名字:")
print('Hello,', name)
age = input("请输入年龄：")
# input()返回的是str类型
age = int(age)
if age <= 12:
    print('kid')
elif age <= 19:
    print('teenager')
else:
    print('adult')
