from PIL import Image
import random

def drawImage():
	wi = 2000
	hi = 2000

	testImage = Image.new("RGB", (wi,hi), (255,255,255))
	pixel = testImage.load()

	size = 10
	for latx in range(int(wi/size)):
		latx = latx * size
		for lony in range(int(hi/size)):
			lony = lony * size

			#red = random.randrange(50,200)
			#blue = random.randrange(50,200)
			#green = random.randrange(50,200)

			red = int(latx / 8)
			blue = int(lony / 8)
			green = int((int(lony / 8) + int(latx / 8)) / 2)

			for x in range(size):
				for y in range(size):			
					pixel[x+latx,y+lony]=(red,green,blue)

	return testImage

def main():
	finalImage = drawImage()
	finalImage.show()

if __name__ == "__main__":
	main()
