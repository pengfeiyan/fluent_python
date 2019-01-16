# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2019/1/16 上午11:05
# @File   : 11.4.py

# 白鹅类型：只要cls是抽象基类，即cls的元类是abc.ABCMeta，就可以使用isinstance(obj,cls)
# 由于鸭子类型的存在，isinstance，type()就显得非常不好用。

class Struggle:

    def __len__(self):
        return 1

class Seq(list):

    def __setitem__(self, key, value):
        pass
    def __getitem__(self, item):
        pass


from collections import abc
print(isinstance(Struggle(),abc.Sized))
print(isinstance(Seq(),abc.Sequence))
