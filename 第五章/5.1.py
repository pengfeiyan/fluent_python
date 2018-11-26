# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/25 下午4:48
# @File   : 5.1.py

# 函数：一等对象

def fact(n):
    '''return n!'''
    return n if n<2 else n*fact(n-1)

'''
__doc__ 
'''
print(fact.__doc__)
f = fact
print(f(42))

l = list(map(fact,range(11)))
print(l)

'''
高阶函数：接收函数作为参数，或者把函数作为返回结果的函数。
'''
fruits = ['strawberry','fiz','apple','cherry','raspberry','banana']
print( sorted(fruits,key=len) )
def reverse(word):
    return word[::-1]
print( sorted(fruits,key=reverse))