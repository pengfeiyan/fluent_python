# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2019/1/16 下午2:36
# @File   : 11.7.py

# 定义一个抽象基类

import abc

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

class Fake(Tombola):

    def pick(self):
        return 13

print(Fake)
# f = Fake()

import random


class BingoCage(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()


