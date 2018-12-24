# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/20 下午3:46
# @File   : 3.3.py

# setdefault

d = {}

l = [1,2,3,4,5,6,7,3,2,4,7,6,2,7,4,2]

for i in l:

    d[i] = d.setdefault(i,0) + 1

print(d)

'''
d[i] = d.setdefault(i,0) + 1 
 =====>
if i not in d.keys():
    d[i] = 1
else:
    d[i] += 1
'''
