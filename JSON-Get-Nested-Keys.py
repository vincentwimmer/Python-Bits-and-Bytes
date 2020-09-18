import json

getJsonFile = 'testData.json'
with open(getJsonFile) as jsonF:
	jsonObjects = json.load(jsonF)

jsonNames =  jsonObjects['objects']

for item in jsonNames :
	if item['Status'] == "Active":
		print(item['Name'])
		tags = '\n '.join(item['Tags'])
		print("Tags:", '\n' , tags, '\n', '--------')
