# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/20 下午5:42
# @File   : 3.6.py

# UserDict

from collections import UserDict

class strDict(UserDict):

    data = {}
    
    def __init__(self,*args,**kwargs):
        super(strDict, self).__init__(*args,**kwargs)

    def update(self,d=None,**kwargs):
        if d is not None:
            for i in d:
                self.data[i] = d[i]
        if len(kwargs):
            for i in kwargs:
                self.data[i] = kwargs[i]


    def __setitem__(self, key, value):
        self.data[str(key)] = value

s = strDict({1:1,"1":2})


a = {1:1,"b":2}
b = {"b":3,"c":4}
c = {**b,**a}  # 3.5之后比较高效的字典合并的方法

print(c)