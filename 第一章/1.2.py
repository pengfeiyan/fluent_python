# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/16 上午10:34
# @File   : 1.2.py

# 模拟数值操作

from math import hypot
# hypot是求两个数字的平方和的方根

class Vector:
    # 向量坐标类

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(other * self.x, other * self.y)


v1 = Vector(1,2)
v2 = Vector(3,4)
print(abs(v1))
print(bool(v1))
print(v1+v2)
print(v1*2)
# 下面这样写会报错,没有支持乘法交换律
print(2*v1)

