# -*- coding:utf-8 -*-
import weakref


class ExpensiveObject:
    def __del__(self):
        print("(Deleting {} )")


obj = ExpensiveObject()
r = weakref.ref(obj)

print('obj:', obj)
print('ref:', r)
print('r():', r())
print('deleting obj')
del obj
print('r():', r())
