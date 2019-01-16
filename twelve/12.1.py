# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2019/1/16 下午3:56
# @File   : 12.1.py

# 子类化内置函数的缺点：内置函数不会调用用户定义的类覆盖的特殊方法

class DoppelDict(dict):

    def __setitem__(self, key, value):
        super(DoppelDict, self).__setitem__(key, [value] * 2)


dd = DoppelDict(one=1)
print(dd)   # 没有走自定义的__setitem__

dd['two'] = 2
print(dd)   # 走了自定义的

dd.update(three=3)
print(dd)   # 没有走自定义的
# Dict的__init__和__update__方法会忽略我们覆盖的__setitem__方法

# 建议不要子类化内置方法，用户自定义的类应该继承collections的UserDict，UserList，UserString，这些类做了特殊设计

import collections
class DoppelDict2(collections.UserDict):

    def __setitem__(self, key, value):
        super(DoppelDict2, self).__setitem__(key, [value] * 2)


dd2 = DoppelDict2(one=1)
print(dd2)

dd2['two'] = 2
print(dd2)

dd2.update(three=3)
print(dd2)