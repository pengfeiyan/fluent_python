# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/16 上午10:19
# @File   : 1.1.py

# 一摞python风格的纸牌

import collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:

    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suites = 'spades diamonds clubs hearts'.split()

    def __init__(self):

        self._cards = [Card(rank,suite) for rank in self.ranks
                       for suite in self.suites]


    def __len__(self):
        # 使得自定义类FrenchDeck能够支持len()方法
        return len(self._cards)

    def __getitem__(self, item):
        # 使得类FrenchDeck支持取值，切片，迭代功能
        return self._cards[item]

    def __contains__(self, item):
        # 使得类FrenchFeck支持in操作
        return item in self._cards


deck = FrenchDeck()

print(len(deck))
print(deck[-1])
print(deck[0::13])
print(Card('2','spades') in deck)

for i in deck:
    print(i)



