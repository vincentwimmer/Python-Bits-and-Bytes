from PIL import Image
import random
import requests
import re
import json

url = 'http://colormind.io/api/'
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
	}
data1 = {'model': 'ui'}
data2 = {'model': 'communist'}
data3 = {'model': 'default'}

def drawImage():
	# Get colors and split them
	rng = random.randrange(1,4)
	if rng == 1:
		data = data1
	if rng == 2:
		data = data2
	if rng == 3:
		data = data3

	getPage = requests.get(url, data=json.dumps(data), headers=headers, timeout=(60))
	colorData = json.loads(getPage.content)
	colorData = colorData['result']

	color1 = re.split("\[|,|]", str(colorData[0]))
	color1List = [color1[1],color1[2],color1[3]]

	color2 = re.split("\[|,|]", str(colorData[1]))
	color2List = [color2[1],color2[2],color2[3]]

	color3 = re.split("\[|,|]", str(colorData[2]))
	color3List = [color3[1],color3[2],color3[3]]

	color4 = re.split("\[|,|]", str(colorData[3]))
	color4List = [color4[1],color4[2],color4[3]]

	color5 = re.split("\[|,|]", str(colorData[4]))
	color5List = [color5[1],color5[2],color5[3]]

	# Resolution Standards
	# 7680 × 4320 8k
	# 15360 x 8640 16k
	# 30720 x 17280 32k
	# 61440 x 34560 64k
	# 122880 x 69120 128k
	# 245760 x 138240 256k

	# Create Image
	testImage = Image.new("RGB", (1000,1000), (255,255,255))
	pixel = testImage.load()

	for latx in range(100):
		latx = latx * 10
		for lony in range(100):
			lony = (lony * 10) - 10

			rng = random.randrange(1,6)

			if rng == 1:
				red = int(color1List[0])
				green = int(color1List[1])
				blue = int(color1List[2])
			if rng == 2:
				red = int(color2List[0])
				green = int(color2List[1])
				blue = int(color2List[2])
			if rng == 3:
				red = int(color3List[0])
				green = int(color3List[1])
				blue = int(color3List[2])
			if rng == 4:
				red = int(color4List[0])
				green = int(color4List[1])
				blue = int(color4List[2])
			if rng == 5:
				red = int(color5List[0])
				green = int(color5List[1])
				blue = int(color5List[2])

			for x in range(10):
				for y in range(10):			
					pixel[x+latx,y+lony]=(red,green,blue)

	return testImage

finalImage = drawImage()
#finalImage.show()

finalImage.save('C:/test.png')
