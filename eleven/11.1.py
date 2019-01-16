# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/12/24 上午11:38
# @File   : 11.1.py

'''
python文化中的接口和协议，python喜欢序列
'''


class Foo:
    '''定义了__getitem__方法就能足够访问元素，迭代和in运算了'''
    def __getitem__(self, item):
        return range(0, 30, 10)[item]


f = Foo()
print(f[1])
for i in f:
    print(i)
print(20 in f,25 in f)

###########################################

class F:
    '''
    该类实现了不可变序列的协议，想要实现可变序列需要定义__setitem__方法，也可以在类外打上猴子补丁
    '''
    def __init__(self):
        self.cards = [ x for x in range(10) ]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, item):
        return self.cards[item]


def set_card(card, key, value):
    card.cards[key] = value


def test():
    print('test')

F.__setitem__ = set_card  # 不需要修改源代码，直接运行时修改类或者模块，这种技术叫做猴子补丁
f = F()

import random
random.shuffle(f)
print(f)

f.test = test
f.test()