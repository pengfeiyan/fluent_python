# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/12/24 上午11:38
# @File   : 11.1.py


l1 = [1,2,3]
l2 = [1,2,3]


all(a == b for a,b in zip(l1,l2))

for a, b in zip(l1,l2):
    if a != b:
        print(False)
