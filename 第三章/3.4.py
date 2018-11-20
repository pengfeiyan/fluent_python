# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/20 下午4:04
# @File   : 3.4.py

# 映射的弹性键查询：defaultDict或者实现__missing__方法

from collections import defaultdict

dd = defaultdict(list)
'''
defaultdict的参数需要是callable的，比如list，set，tuple，甚至是自定义的function名。   
在调用__getitem__找不到对应的键时，会创建并赋予默认值，直接调用get()不会生效。
'''
print(dd.get('test'))  # None
print(dd['test'])  # []
print(dd.get('test')) # []

class A(dict):

    def __init__(self,l):
        self._l = l
        print(self._l)

    def __missing__(self, key):
        return "missing"

d = dict(one=1,two=2,three=3,four=4,five=5)
a = A(d)
print(a['ones'])
'''
继承了dict类，只需要实现__missing__就可以了，dict里的__getitem__会自动调用__missing__。
但是dict本身没有__missing__方法，但是dict知道有这么个东西存在。
'''

class StrKeyDict(dict):

    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError
        return self[str(key)]

    def get(self,key,default=None):
        try:
            return self[key]
        except Exception:
            return default

s = StrKeyDict({"a":1,"b":2})

print(s['c'])

