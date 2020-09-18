
import csv
import json

def make_json(csvFilePath, jsonFilePath):
    data = {'objects': []}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            data['objects'].append(rows)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


csvFilePath = r'oldFile.csv'
jsonFilePath = r'newFile.json'

make_json(csvFilePath, jsonFilePath)
