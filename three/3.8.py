# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/21 下午3:04
# @File   : 3.8.py

# set

'''
set的三种创建方法:
set()       ====>      empty set
set(iter)   ====>      iterable
{}          ====>      字面量创建，比较快速，python会直接使用字节码BUILD_SET来构建
'''

s_string = set('string')
s_iter = set([1,2,3,4,5])
s_zimian = {1,2,3,4,5}

#  查看字节码，python -m dis file.py

a = {1,3,5,7}
b = {1,2,3,4}

print("交集：",a&b)
print("合集：",a|b)
print("a对于b的差集：",a-b)
print("对称差集：",a^b)

