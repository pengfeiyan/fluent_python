# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2019/1/16 上午11:55
# @File   : 11.6.py

# 抽象基类
# collections.abc
# Iterable，Container，Sized 集合继承这三个抽象基类
# Sequence，Mapping，Set 集合基类
# MappingView，映射方法.items(),.keys(),.values()分别返回ItemsView，KeysView，ValueView的实例。
# Callable,Hashable 安全的方法来检测对象能不能调用或者散列，callable()有已有方法，检验可散列建议使用isinstance(obj,Hashable)
# Iterator Iterable的子类

# numbers包
# Itegral， 接收int、bool的子类
# Real，接收int、float、bool、fractions.Fraction

# 为了代码的设计风险，不建议自己定义抽象基类，使用现有的抽象基类

from collections.abc import Hashable
a = tuple('abc')
print(a)
print(isinstance(a,Hashable))