import random
import threading
import time

def averageData():
	global avOutter
	global avInner
	avOutter = [0] * 20
	avInner = [0] * 20
	while True:
		for y in range(len(avOutter)):
			for z in range(len(avInner)):
				avInner[z] = random.randint(0,9)
				#print(avInner)
				time.sleep(0.05)
			avOutter[y] = round(sum(avInner) / len(avInner))
			print(avOutter)

def main():
	while True:
		print(round(sum(avOutter) / len(avOutter)))
		time.sleep(2)

avdata_thread = threading.Thread(target=averageData)
avdata_thread.start()

main_thread = threading.Thread(target=main)
main_thread.start()
