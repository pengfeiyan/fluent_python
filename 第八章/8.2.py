# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/30 上午11:56
# @File   : 8.2.py

# 元组的不可变性

t1 = (1,2,[30,40])
t2 = (1,2,[30,40])
print(t1==t2)
print(t1 is t2)


# 无限引用
a = [1,2]
b = [a,3]
a.append(b)
print(a)

