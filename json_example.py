# -*- coding: utf-8 -*-
import json

data = {
    "first": 1,
    "second": 3,
    "third": [12, 3, 4]
}

print(json.dumps(data))
print(type(json.dumps(data)))

# convert json string back to python dict
json_str=json.dumps(data)
result =json.loads(json_str)
print(result)
print(type(result))