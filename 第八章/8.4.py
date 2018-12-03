# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/12/1 下午10:01
# @File   : 8.4.py

# 可变参数作为默认值
'''
参数默认值是在函数编译的时候确定，如果默认值为可变参数，那么他们的实例就会共用一个引用。
'''

class Student:

    def __init__(self,passes=list()):
        self.passes = passes

    def pick(self,one):
        self.passes.append(one)

    def drop(self,one):
        self.passes.remove(one)

    def __str__(self):
        return ','.join(self.passes)


print(Student.__init__.__defaults__)

s1 = Student()
s1.pick('ypf')

s2 = Student()
print(s2)
print(s1.__init__.__defaults__)

'''
可变参数直接赋值，也是不可以的，因为类属性和传入的参数公用引用，正确的做法是
self.l = list(l)，而不是self.l = l
'''