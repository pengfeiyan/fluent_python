# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/30 上午11:10
# @File   : 8.1.py

# 变量不是盒子

class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))

x = Gizmo()
y = Gizmo() * 10
'''
y的右侧会报错，所以y并没有创建。python中的变量都是标签，并不是盒子
'''

x = 0
print(x is None)
print(x is not None)
'''
在做变量和单例值的比较时，应该使用is，is比==要快，因为is不能被重写。
a==b，其实调用的是a.__eq__(b)，对于比较复杂的对象比较，可能需要重写__eq__方法
'''

