dict1 = {"a":"aaa","b":"bbb","c":"ccc"}

str1 = "The list: \n"

for k,v in dict1.items():
	vals = k + " : " + v
	str1 = str1 + str(vals) + "\n"

print(str1)
