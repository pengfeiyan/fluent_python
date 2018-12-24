# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/12/2 下午3:47
# @File   : 9.2.py

from array import array
import math

class Vector2d:

    typecode = 'd'

    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        '''
        @property装饰器可以将方法标记为特性
        '''
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x,self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name,*self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode,self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __hash__(self):
        '''
        只有实现了__hash__和__eq__方法，才可以散列。并且保证参与哈希的值绝不能改变，最好使用位运算符异或
        '''
        return hash(self.x) ^ hash(self.y)

v1 = Vector2d(2,1)
v2 = Vector2d(2,2)


a,b = v1
print(a,b)



