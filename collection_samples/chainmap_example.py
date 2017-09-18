# -*- coding:utf-8 -*-
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a,b)

print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))

print('Items:')

