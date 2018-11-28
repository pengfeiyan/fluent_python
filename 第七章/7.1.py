# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/28 下午2:59
# @File   : 7.1.py

# 装饰器

def timer(func):
    def wapper():
        import time
        print('开始时间:',time.time())
        func()
        print('结束时间:',time.time())
    return wapper

@timer
def test():
    print('test')

'''
在test()上面加上@timer等价于 ==>
test = timer(test)

装饰器是在被装饰的函数定义时执行，而不是调用时执行
'''