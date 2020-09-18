dict1 = {"a":"aaa","b":["bbb","222"],"c":"ccc"}

print(dict1["b"])

dict2 = {"b":["222","bbb"]}

dict1.update(dict2)

print(dict1["b"])
