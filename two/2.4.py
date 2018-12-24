# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/16 下午5:41
# @File   : 2.4.py

# 切片和切片赋值
nums = [1,2,3,4,5]
print(nums[0::2])

nums[0:1] = ['a']  # 切片赋值必须是一个可迭代的对象
print(nums)

# 切片赋值和切片拷贝不一样，切片赋值是引用，切片拷贝是浅拷贝
a = nums
a.append('b')
print(nums) # 直接赋值，也会影响nums


# 序列的+和*
l = [1,2,3]
print(id(5*l),id(l))  # 都会生成一个新的序列

# 序列翻倍之后，内部的元素还是一个地址
m = ['_']
print("m,id",id(m))
board = [m*3 for i in range(3)]
print(board)
for i in board:
    print('i，id',id(i))
    for j in i:
        print('j,id',id(j))




