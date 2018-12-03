# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/29 上午10:47
# @File   : 7.8.py

# 标准库中的装饰器

from functools import lru_cache

def clock(func):
    def wrapper(*args):
        import time
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return wrapper

'''
1,1,2,3,5,7,12......
'''
#@clock
@lru_cache()
@clock
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

fibonacci(30)

'''
装饰器的叠放顺序
@d1
@d2
def f:
    pass
    
f = d1(d2(f))
'''