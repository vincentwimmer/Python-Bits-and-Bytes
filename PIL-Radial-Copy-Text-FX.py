# Warning - This will take a while to render on most computers because I added the "3x Anti-Aliasing" to the code. I made a non-AA version and attached it to the bottom of this file if interested.

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw   

img = Image.new("RGB", (400, 400), (0, 0, 0))
inputText = "//&&||$$123ABC@"

font = ImageFont.truetype("C:/Users/vwimmer/Documents/Git/Tests/fonts/Roboto-Medium.ttf", 72)

for x in range(360):
	txt = Image.new("RGBA", (1200, 1200), (255, 255, 255, 0))
	draw = ImageDraw.Draw(txt)
	draw.text((20, 580), inputText, (int((9*(x/20))),int((9*(x/20))),int((9*(x/20)))), font=font)
	w = txt.rotate(-1 - (x*1))
	size = 400, 400
	w.thumbnail(img.size, Image.ANTIALIAS)

	offset = (0,0)
	img.paste(w, offset,mask=w)


txt = Image.new("RGBA", (1200, 1200), (255, 255, 255, 0))
draw = ImageDraw.Draw(txt)
draw.text((20, 580), inputText, (255,255,255), font=font)
size = 400, 400
txt.thumbnail(img.size, Image.ANTIALIAS)
offset = (0,0)
img.paste(txt, offset,mask=txt)


img.show()

# --- No AA version below ---

#from PIL import Image
#from PIL import ImageFont
#from PIL import ImageDraw   
#
#img = Image.new("RGB", (400, 400), (0, 0, 0))
#inputText = "//&&||$$123ABC@"
#
#font = ImageFont.truetype("C:/Users/vwimmer/Documents/Git/Tests/fonts/Roboto-Medium.ttf", 24)
#
#for x in range(360):
#	txt = Image.new("RGBA", (400, 400), (255, 255, 255, 0))
#	draw = ImageDraw.Draw(txt)
#	draw.text((5, 190), inputText, (int((9*(x/20))),int((9*(x/20))),int((9*(x/20)))), font=font)
#	w = txt.rotate(-1 - (x*1))
#
#	offset = (0,0)
#	img.paste(w, offset,mask=w)
#
#
#txt = Image.new("RGBA", (400, 400), (255, 255, 255, 0))
#draw = ImageDraw.Draw(txt)
#draw.text((5, 190), inputText, (255,255,255), font=font)
#offset = (0,0)
#img.paste(txt, offset,mask=txt)
#
#
#img.show()
