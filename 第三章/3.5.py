# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/20 下午5:03
# @File   : 3.5.py

# 字典的变种

from collections import OrderedDict
'''
python3.6以后dict都是保持顺序的，但使用OrderedDict能返回最开始或者最后添加的元素。dict默认没有这两个方法
OrderedDict中popitem()默认删除并返回最后一个添加的元素，popitem(last=False)默认删除并返回第一个添加的元素
'''
d = OrderedDict(dict(zip(['one','two','three'],[1,2,3])))
print(d)
print(d.popitem())
print(d)


from collections import Counter

l = [1,2,4,6,2,5,8,4,6,9,2,4,8]

ct = Counter(l)
print(ct)
'''
    Counter的init
    >>> c = Counter()                           # a new, empty counter
    >>> c = Counter('gallahad')                 # a new counter from an iterable
    >>> c = Counter({'a': 4, 'b': 2})           # a new counter from a mapping
    >>> c = Counter(a=4, b=2)                   # a new counter from keyword args
'''

