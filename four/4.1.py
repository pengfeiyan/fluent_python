# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/22 下午4:52
# @File   : 4.1.py

s = 'cafe我们'
print(len(s))

b = s.encode('utf8')
print(b)
print(len(b))

print(b[0])
print(b[0:1])

b = bytes([26,56,67,72])
print(b[:1])

