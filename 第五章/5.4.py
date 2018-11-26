# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/25 下午5:21
# @File   : 5.4.py

'''
python中7种可调用对象
1、用户def或者lambda
2、内置函数
3、内置方法
4、类方法
5、类   __new__
6、类实例  __call__
7、生成器yield
'''
import random

class BingoCage:

    def __init__(self,items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('try to pick from emtry list.')

    def __call__(self, *args, **kwargs):
        return self.pick()




l = list(range(5))
bc = BingoCage(l)
# for i in range(6):
#     print(bc())

'''函数属性'''
def test():
    pass
print(dir(test))

'''函数特有的属性而类没有的'''
print("函数特有的属性而类没有的:",set(dir(test)) - set(dir(BingoCage)))


