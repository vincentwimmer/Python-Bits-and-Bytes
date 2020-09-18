import threading

def Main(thread):
	print("Starting on Thread", thread)
	x = 0
	while True:
		if x < 50:
			x = x + 1
			print("Thread", thread, "Prints:", x)
		else:
			break

for thread in range(10):
	threading.Thread(target=Main,args=(thread,)).start()
