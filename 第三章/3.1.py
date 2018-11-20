# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/20 下午3:33
# @File   : 3.1.py

from collections import abc

# abc下有两个抽象基类 Mapping MutableMapping，非抽象映射类型一般不会直接继承这些抽象类，这些抽象类主要作用是作为形式化的文档
# 所以用isinstance来判断是不是广义上的映射对象


d = {}

print(isinstance(d, abc.Mapping))
print(isinstance(d, abc.MutableMapping))
