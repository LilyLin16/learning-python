#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import sys  # 引入 sys 模块

# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)


list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
for x in it:
    print(x, end=" ")
print("\n")


# generator(生成器)


class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


for n in Fab(5):
    print(n)

# yield 的作用就是把一个函数变成一个generator，带有yield的函数不再是一个普通函数，Python 解释器会将其视为一个generator，
# 调用fab(5)不会执行fab函数，而是返回一个iterable对象！在for循环执行时，每次循环都会执行fab函数内部的代码，
# 执行到yield b时，fab 函数就返回一个迭代值，下次迭代时，代码从yield b的下一条语句继续执行，
# 而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到yield


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1

# 一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，
# 但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行
for n in fab(5):
    print(n)


#另一个 yield 的例子来源于文件读取。
# 如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用。
# 好的方法是利用固定长度的缓冲区来不断读取文件内容。
# 通过 yield，我们不再需要编写读文件的迭代类，就可以轻松实现文件读取：
def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return


#
list = [9, 8, 7, 6]
it = iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()