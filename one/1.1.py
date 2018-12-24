# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/16 上午10:19
# @File   : 1.1.py

# 一摞python风格的纸牌

import collections

Card = collections.namedtuple('Card',['rank','suit'])


class FrenchDeck:

   #  __slots__ = ('_cards', 'v')

    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suites = 'spades diamonds clubs hearts'.split()

    # data = 1

    def __init__(self):
        self._cards = [Card(rank,suite) for rank in self.ranks
                       for suite in self.suites]

        self.v = '1.0.0'

    def __len__(self):
        # 使得自定义类FrenchDeck能够支持len()方法
        return len(self._cards)

    def __getitem__(self, item):
        # 使得类FrenchDeck支持取值，切片，迭代功能(没有定义__iter__的时候会使用下标迭代，直到出现IndexError)
        return self._cards[item]


    def __contains__(self, item):
        # 使得类FrenchFeck支持in操作

        return item in self._cards

    def __reversed__(self):
        print('reversed')
        return reversed(self._cards)

    # def __iter__(self):  # 返回具有__next__方法的对象
    #     return self
    #
    # def __next__(self):
    #     if self.data > 5:
    #         raise StopIteration
    #
    #     else:
    #         ret = self.data
    #         self.data += 1
    #         return ret


deck = FrenchDeck()

# print(len(deck))
# print(deck[-1])
# print(deck[0::13])
# print(Card('2','spades') in deck)
#
# for i in reversed(deck):
#     print(i)

class Test:

    def test_2(self):
        '''test_2_doc'''
        print('test2')

    def test_1(self):
        '''test_1 doc'''
        print('test1')



