# -*- coding:utf-8 -*-

# dump custom class
import json


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "{'name':{}}".format(self.name)


p = Person("patrick")
try:
    print(json.dumps(p))
except TypeError as err:
    print('ERROR:', err)


def custom_converter(obj):
    d = {
        '__class__': obj.__class__.__name__,
        '__module__': obj.__module__,
    }
    d.update(obj.__dict__)
    return d


print("encoding Person:", json.dumps(p, default=custom_converter))


# Encoder,Decoder
