# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/26 上午9:48
# @File   : 5.8.py

# 获取关于参数的信息

def clip(text,max_len=80,*args,**kwargs):
    """在max_len前面或者后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before > 0:
            end = space_before
        else:
            space_after = text.rfind(' ', 0, max_len)
            if space_after >= 0:
                end = space_after
        if end is None:
            end = len(text)
        return text[:end].rstrip()

print("定位参数和关键字参数的默认值:",clip.__defaults__)
print(clip.__kwdefaults__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)

from inspect import signature
sig = signature(clip)
print(sig)
for name,param in sig.parameters.items():
    print(param.kind,":",name,'=',param.default)

"""
5类参数类型：
1、POSITIONAL_OR_KEYWORD     支持定位和关键字传入的参数
2、VAR_POSITIONAL            定位参数元组，*args
3、VAR_KEYWORD               关键字参数字典 **kwargs
4、KEYWORD_ONLY              仅限关键字参数 *,params
5、POSITIONAL_ONLY           目前python语法不支持
"""
