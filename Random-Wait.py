import random
import time

def rwait():
	x = 0
	y = 0
	while y != 3:
		y = random.randint(0, (10))
		x = (x + 1)
	return x

while True:
	print("Waiting", rwait(), "seconds.")
	time.sleep(rwait())
