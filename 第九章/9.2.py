# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/12/2 下午3:47
# @File   : 9.2.py

from array import array
import math

class Vector2d:

    typecode = 'd'

    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x,self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name,*self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)])+bytes(array(self.typecode,self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


print(bytes(Vector2d(1,2)))

class Demo:
    '''
    classmethod是类方法；staticmethod为静态方法，和普通函数一样
    '''
    @classmethod
    def clsfunc(cls,*args):
        print(args)

    @staticmethod
    def statfunc(*args):
        print(args)


print(Demo.clsfunc)
print(Demo.statfunc)

d = Demo()
print(d.clsfunc)
print(d.statfunc)

