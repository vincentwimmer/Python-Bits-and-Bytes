import random
import threading
import time

def averageData():
	global avList
	avList = [0] * 20
	while True:
		for x in range(len(avList)):
			avList[x] = random.randint(0,9)
			print(avList)
			time.sleep(0.15)

def main():
	while True:
		print(round(sum(avList) / len(avList)))
		time.sleep(2)

avdata_thread = threading.Thread(target=averageData)
avdata_thread.start()

main_thread = threading.Thread(target=main)
main_thread.start()
