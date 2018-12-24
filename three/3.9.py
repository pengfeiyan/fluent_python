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

"""
字典和集合是通过散列表实现的，python能够保证散列表有三分之一的空余，当快要满的时候，会开辟一个新的散列区域，
把旧的数据拷贝过去，同时可能会出现新的散列冲突，顺序可能会出现变化，因此字典迭代的时候，不顺序修改size。
"""


