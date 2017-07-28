# -*- coding: utf-8 -*-
import json

data = {
    "first": 1,
    "second": 3,
    "third": [12, 3, 4]
}
"""
dump dict to json string
"""
print("JSON:{}".format(json.dumps(data)))
print(type(json.dumps(data)))

data_list =[{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print("DATA:",repr(data_list))
print("JSON:",json.dumps(data_list))
# convert json string back to python dict
json_str=json.dumps(data)

# load json
result =json.loads(json_str)
print(result)
print(type(result))