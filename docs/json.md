# Python Module - json
 
 json在http协议的调用中使用广泛，python自带的json库基本可以满足使用，json库主要的方法
 其实就这个两个：
 
 - dumps
 - loads
 
 # JSON dumps
 
 dumps 就是把python中的数据结构转换为json string
 
```python
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
```

结果如下：

```python
JSON:{"first": 1, "second": 3, "third": [12, 3, 4]}
<class 'str'> # 是个string 类型
```

