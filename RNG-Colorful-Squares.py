from PIL import Image
import random

def drawImage():
	testImage = Image.new("RGB", (600,600), (255,255,255))
	pixel = testImage.load()

	for latx in range(60):
		latx = latx * 10
		for lony in range(60):
			lony = lony * 10

			red = random.randrange(80,120)
			blue = random.randrange(80,230)
			green = random.randrange(80,200)
			for x in range(10):
				for y in range(10):			
					pixel[x+latx,y+lony]=(red,green,blue)

	return testImage

def main():
	finalImage = drawImage()
	finalImage.show()

if __name__ == "__main__":
	main()
