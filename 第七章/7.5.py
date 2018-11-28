# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/28 下午4:04
# @File   : 7.5.py

# 闭包

def make_avg():
    series = []
    def avg(new_value):
        series.append(new_value)
        return sum(series)/len(series)

    return avg

a = make_avg()
print("变量名：",a.__code__.co_varnames)
print("自由变量:",a.__code__.co_freevars)
'''
闭包:引用了自由变量的函数，这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。
闭包中引用的自由变量只能引用不能修改，强行修改会有两个结果，一是报错，二是修改不成功。
python命名空间的查找顺序是LEGB：local->enclosed->global->built-in
'''

def make_avg():
    count = 0
    total = 0
    def avg(new_value):
        nonlocal count,total
        count += 1
        total += new_value
        return total/count
    return avg

a = make_avg()
print(a.__code__.co_freevars)

import dis
dis.dis(make_avg)