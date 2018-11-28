# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/16 上午11:38
# @File   : 2.2.py

# 列表推导和生成器表达式

# 列表推导式的易读性和高效性
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

codes = [ ord(symbol) for symbol in symbols ]
print(codes)

# 列表推导式不会出现变量的泄漏 ,  有列表推导，集合推导，字典推导。
x = 'ABC'
dummy = [ord(x) for x in x]
print(x)
print(dummy)

# 利用生成器表达式计算笛卡尔积，生成器表达式的优先是不会一次性产出所有的情况，一次性的。
colors = ['blank', 'white']
sizes = ['S', 'M' ,'L']

for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
    print(tshirt)