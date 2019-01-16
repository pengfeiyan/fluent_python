# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2019/1/16 下午3:09
# @File   : 11.7.3.py

import abc
from random import randrange

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self,iterable):
        """从可迭代对象中添加元素
        """

    @abc.abstractmethod
    def pick(self):
        """随机删除元素并返回，如果实例为空，应该抛出LookupError。
        """

    def loaded(self):
        """如果至少有一个元素，返回`True`，否则返回`False`
        """
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元素，由当前的元素构成
        """
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))
# Tombola.resigter(TomboList) python3.3之前的版本

print(issubclass(TomboList,Tombola))
print(isinstance(TomboList(),Tombola))

# __mro__ 方法解析顺序，Method Resolution Order
print(Tombola.__mro__)
print(TomboList.__mro__)