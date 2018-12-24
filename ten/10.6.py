# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/12/24 上午10:58
# @File   : 10.6.py


from array import array
import reprlib
import math
import functools
import operator


class Vector:
    '''
    散列和快速等值测试
    '''
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        # return tuple(self) == tuple(other)
        # tuple()构建在分量很多的情况下会很占空间
        if len(self) != len(other):
            return False
        for a, b in zip(self, other):
            if a != b:
                return False
        return True
        # return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        # hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)
        # return functools.reduce(lambda a,b:a^b, hashes, 0)
        # reduce()中第三个参数initial最好是提供，如果序列为空则返回initial而不是抛出异常，通常+，|，^的init为0，*,&的init为1。
    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._components[item])
        elif isinstance(item, int):
            return self._components[item]
        else:
            raise TypeError(f'{cls.__name__} indices must be integers.')

