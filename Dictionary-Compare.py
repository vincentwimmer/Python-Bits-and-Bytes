dict1 = {"a":"aaa","b":["bbb",["222"]],"c":"ccc"}

dict2 = {"a":"aaa","b":["bbb",["222","333"],"bbb"],"c":"ccc","d":"ddd"}

d1b = dict1.get("b")

d2b = dict2.get("b")

d1d = dict1.get("d")

d2d = dict2.get("d")

if len(d2b[1]) > len(d1b[1]):
	print("yey")

if d2d != d1d:
	print("hey")
