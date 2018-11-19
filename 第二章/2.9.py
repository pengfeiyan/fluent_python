# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/19 下午3:12
# @File   : 2.9.py

# 当列表不是首选

from array import array
from random import random

floats = array('d',(random() for i in range(10)))

# 纯数字的集合用array，比list要高效得多
print(floats)

