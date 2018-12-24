# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/12/3 下午4:35
# @File   : 8.6.py
import sys
from weakref import WeakValueDictionary,WeakKeyDictionary,WeakSet
'''
int,string,list,dict,tuple的实例不能作为弱引用的所指对象，set实例可以
string，list，dict的子类实例或者用户自定义实例可以作为弱引用所指对象
int，tuple的子类不行
'''

class Fruit:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name

fs = [ Fruit(name) for name in ['banana','apple','orange'] ]

wkdic = WeakValueDictionary()
for f in fs:
    wkdic[str(f)] = f

print(wkdic.get('apple'))   #  输出：apple
del fs
print(wkdic.get('apple'))   # 输出None,因为fs名称被删除了。弱引用失效了
print(wkdic.get('orange'))  # 输出orange，因为前边迭代的时候f的值是orange，f是全局变量，不显式删除不会自动回收

del f
print(wkdic.get('orange'))  # 输出None



class A:

    @classmethod
    def clsm(cls,a):
        print(cls,a)

    @staticmethod
    def stam(a):
        print(a)


    def selfm(self,a):
        print(self,a)

class B(A):
    pass


a = A()
a.selfm(1)
a.clsm(1)
a.stam(1)

b = B()
b.selfm(2)
b.clsm(2)
b.stam(2)