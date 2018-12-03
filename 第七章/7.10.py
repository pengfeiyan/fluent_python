# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/29 上午11:45
# @File   : 7.10.py


# 参数化装饰器
#
# registry = []
#
# def register(func):
#     print('running register(%s)' % func.__name__)
#     registry.append(func)
#     return func
#
# @register
# def f1():
#     print('running f1()')
#
# print('running main()')
# print('registry ->', registry)
# f1()

print('====================')
registry = set()

def register(active=True):
    def decorate(func):
        def wrapper(*args,**kwargs):
            if active is not True:
                print('func %s not register' % func.__name__)
                return func
            else:
                print('func %s is register' % func.__name__)
                registry.add(func)
                return func

        return wrapper
    return decorate

@register(True)
def f1():
    pass

@register(False)
def f2():
    pass

@register()
def f3():
    pass

f1()
f2()
f3()
print(registry)

