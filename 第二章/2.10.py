# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/19 下午4:09
# @File   : 2.10.py

# deque,queue,headp

from collections import deque

d = deque(range(10),maxlen=10)
d.rotate(3) # 右移3位
print(d[5])

d.appendleft('a')
print(d)

from queue import Queue

q = Queue(1)
q.put('a')   #  当queue满的时候调用put，该线程会阻塞，直到queue有线程消费掉了里面的内容，可以指定timeout，使用put_nowait()默认timeout为False
# q.join()
# q.task_done()
print(q.get(0))

# queue的task_done和join方法在多线程中很有用

# 扁平序列,str,bytes,bytearray,array.array,memoryview都是要求序列元素是同一种类型的
# 容器序列list,tuple,collections.deque等


# 插一嘴，python 3.6及以下的缓存机制，小数字缓存和字符串缓存，数字的[-5,256]和20位字符串会做缓存，python3.7以后缓存机制修改了下

#3.6  i is j == False,   3.7 i is j == True
i = 257
j = 258-1