# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/12/1 下午10:18
# @File   : 8.5.py

# del和垃圾回收

'''
del是删除名称，而不是删除对象，删除名称可能会导致对象被垃圾回收
'''

import weakref
s1 = {1,2,3}
s2 = s1
def bye():
    print('gone with the wind')

ender = weakref.finalize(s1,bye)  # 监控回掉
print(ender.alive)
del s1  #删除s1的名称
print(ender.alive)
s2 = 'spam' #将引用释放
print(ender.alive)
'''
{1,2,3}的对象被回收了，ender也是把s1的引用传进去了，为什么对象被回收了呢，因为传入的是一个弱引用
弱引用不会增加对象的引用计数，是一个对象的引用缓存。能够被调用，返回引用对象
'''
print('------ 验证弱引用————————————')
a_set = {1,2}

weak = weakref.ref(a_set)
print('弱引用：',weak)
print('调用弱引用：',weak())
a_set = {2,3}
print('弱引用的对象引用计数为0时，弱引用失效：',weak)



