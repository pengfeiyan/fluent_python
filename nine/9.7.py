# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/12/19 下午3:06
# @File   : 9.7.py

'''
__slots__会以紧实的结构存储实例属性，而不是字典
值得注意的是：
每个子类都要定义__slots__属性，否则解释器会忽略继承的__slots__属性
实例只能拥有__slots__定义的属性，将'__dict__'加入进入就会让实例重新以dict的格式存储实例属性
如果让实例支持弱引用，需要将__weakref__加入进
'''
class Dog:

    __slots__ = ('__name')

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

d1 = Dog('alan')
print(d1.__dict__)


