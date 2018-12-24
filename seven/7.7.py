# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/29 上午10:32
# @File   : 7.7.py

# 简单的装饰器

import time

def clock(func):
    def wrapper(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return wrapper

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def fact(n):
    return 1 if n<2 else n*fact(n-1)

snooze(1)
print("=====================")
fact(7)

'''
clock装饰器函数有几个缺点:
不支持关键字参数；没有保存原来函数的信息,__name__,__doc__
'''

def new_clock(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args,**kwargs):
        t0 = time.perf_counter()
        result = func(*args,**kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return wrapper