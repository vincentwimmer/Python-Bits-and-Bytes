# Opens CSV, shuffles rows, outputs to new CSV.

import csv
import random

def shuffleCSV(csvInFilePath, csvOutFilePath):
	data = []

	with open(csvInFilePath, encoding='utf-8') as csvf:
		csvReader = csv.reader(csvf)
		for rows in csvReader:
			data.append(rows)

	random.shuffle(data)

	with open(csvOutFilePath, 'w', newline='') as csvf:  
		csvwriter = csv.writer(csvf) 
		csvwriter.writerows(data) 
	

csvInFilePath = r'in.csv'
csvOutFilePath = r'out.csv'

shuffleCSV(csvInFilePath, csvOutFilePath)
