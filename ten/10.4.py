# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/12/20 上午9:53
# @File   : 10.4.py

from array import array
import reprlib
import math


class Vector:
    '''
    具有切片功能的类
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
        return tuple(self) == tuple(other)

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


v = Vector(range(10))
print('v[0] = ',v[0])
print('v[0:3] = ',v[0:3],',type = ',type(v[0:3]))
print('v[0:1,2:5] = ',v[0:1,2:5])
print('v["a"] = ',v['a'])

class MySeq():

    def __getitem__(self, item):
        return item

s = MySeq()
print(s[1])         #   1
print(s[0:4])       #   slice(0, 4, None)
print(s[0:4:2])     #   slice(0, 4, 2)
print(s[1:4:2, 7:9])#   (slice(1, 4, 2), slice(7, 9, None))

string = 'abcdefg'
a = slice(None, 10 ,2)
b = slice(-3, None, None)
print(string[a])
print(string[b])