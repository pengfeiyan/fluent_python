# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/16 下午12:09
# @File   : 2.3.py

# 元组不仅仅是不可变的列表
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

# 元组拆包来互换变量
a = 1
b = 2
a,b = b,a

# _过滤掉不需要的内容
import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)

# *接收多个参数，元组嵌套拆包
a,b,*r = range(5)

a,b,c,(d,e) = (1,2,3,(4,5))

# 具名元组
import collections
person = collections.namedtuple('person', 'name sex age')
yanpengfei = person('yanpengfei', 'm', 19)
print(yanpengfei)
print(yanpengfei.name)
print(yanpengfei.sex)
print(yanpengfei[2])
# yanpengfei[2] = 20 # 因为有元组的属性，不支持修改
