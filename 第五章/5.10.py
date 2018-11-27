# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/11/27 下午6:04
# @File   : 5.10.py

# 支持函数式编程
from functools import reduce
def fact(n):
    return reduce(lambda a,b:a*b, range(1,n+1))

print(fact(3))

'''
operator.itemgetter

itemgetter(1)    ===>
lambda field:field[1]
'''
metor_data = [
    ('Tokyo','JP',36.933,(1,1)),
    ('Delhi NCR','IN',21.935,(1,1)),
    ('Mexico City','MX',20.142,(1,1)),
    ('New York','US',20.104,(1,1)),
    ('Sao Paulo','BR',19.649,(1,1))
]
from operator import itemgetter
for city in sorted(metor_data,key=itemgetter(2)):
    print(city)

cc_name = itemgetter(1, 0)
for city in metor_data:
    print(cc_name(city))


from collections import namedtuple
LatLong = namedtuple('LatLong','Lat long')
Metropolis = namedtuple('Metropolis','name cc pop coord')

metor_datas = [
    Metropolis(name,cc,pop,LatLong(x,y))
    for name,cc,pop,(x,y) in metor_data
]
from operator import attrgetter
name_lat = attrgetter('name','pop','coord.Lat')
for city in sorted(metor_datas,key=attrgetter('pop')):
    print(name_lat(city))


'''
methodcaller
'''
from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))
hiphenate = methodcaller('replace',' ','-')
print(hiphenate(s))

