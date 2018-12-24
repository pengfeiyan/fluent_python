# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/12/24 上午10:06
# @File   : 10.5.py


from array import array
import reprlib
import math


class Vector:
    '''
    增加动态存取属性
    '''
    typecode = 'd'
    shortcut_names = 'xyzt'

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

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        raise AttributeError(f'{cls.__name__!r} object has no attribute {name!r}.')

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = f'readonly attribute {name!r}.'
            elif name.islower():
                error = f'can`t set attributes "a" to "z" in {cls.__name__!r}'
            else:
                error = ''
            if error:
                raise AttributeError(error)
        super().__setattr__(name, value)

v = Vector(range(5))
print(v)
#v.X = 10
print(v.y)
print(v)
