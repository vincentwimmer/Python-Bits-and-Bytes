import json

getJsonFile = 'testData.json'
with open(getJsonFile) as jsonF:
	jsonObjects = json.load(jsonF)

jsonNames =  jsonObjects['objects']

for item in jsonNames :
	if item['Status'] == "Active":
		print(item['Name'])
