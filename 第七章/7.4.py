# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/28 下午3:24
# @File   : 7.4.py

# 变量作用域

from dis import dis

def f1(a):
    print(a)
    print(b)
'''
提示：global name 'b' is not defined。3.5+ 去掉了global
'''
dis(f1)

b = 4
def f2(a):
    print(a)
    print(b)
'''
可以调用成功
'''
dis(f2)
def f3(a):
    print(a)
    print(b)  # 此处报错是因为b被判定为一个局部变量
    b = 4

dis(f3)
'''
即使用全局变量b，但是在函数内部还是报错，提示 local variable 'b' referenced before assignment
因为b在编译函数的时候，判断b是一个局部变量
'''
def f4(a):
    global b  # 声明b是一个全局变量
    print(a)
    print(b)
    b = 100
    print(b)
dis(f4)


x = 1
def foo():
    x = 2
    def innerfoo():
        x = 3               #此处改动：注释掉
        print('locals ', x)
    innerfoo()
    print('enclosing function locals ', x)
foo()
print('global ', x)

