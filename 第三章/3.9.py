# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/21 下午6:28
# @File   : 3.9.py

# dict和set背后的原理

from collections import UserDict

class A(UserDict):

    def __init__(self,d):
        self.data = d

    """ UserDict中实现了__getitem__方法，找不到key的时候会调用__missing__"""
    # def __getitem__(self, item):
    #     return self.data[item]

    def get(self,item):
        return "__get__"

    def __missing__(self, key):
        return "__missing__"

a = A({"a":1,"b":2})
print(a['c'])


class A(object):

    def __eq__(self, other):
        return True


a1 = A()
a2 = A()

print('a1==a2:',a1 == a2)






