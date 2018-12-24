# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/19 下午3:12
# @File   : 2.9.py

# 当列表不是首选

from array import array
from random import random

floats = array('d',(random() for i in range(10)))
'''
        Type code   C Type             Minimum size in bytes 
        'b'         signed integer     1 
        'B'         unsigned integer   1 
        'u'         Unicode character  2 (see note) 
        'h'         signed integer     2 
        'H'         unsigned integer   2 
        'i'         signed integer     2 
        'I'         unsigned integer   2 
        'l'         signed integer     4 
        'L'         unsigned integer   4 
        'q'         signed integer     8 (see note) 
        'Q'         unsigned integer   8 (see note) 
        'f'         floating point     4 
        'd'         floating point     8 

'''

# 纯数字的集合用array，比list要高效得多
print(floats)

