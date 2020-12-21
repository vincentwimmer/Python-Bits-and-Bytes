from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw   

img = Image.new("RGB", (300, 300), (80, 80, 80))
inputText = "//&&||$$123ABC@@"

# Set it up with Anti-Aliasing like in "PIL-AA-Font.py" - 3x everything's size.
img2 = Image.new("RGBA", (900, 900), (255, 255, 255, 0))
draw = ImageDraw.Draw(img2)
font = ImageFont.truetype("Roboto-Medium.ttf", 72)

# Draw Text in loop while moving the draw position for each iteration. Also add increasing color values for gradient effect.
for x in range(20):
	draw.text(((50 + (x/2)), (50 - (x*2))), inputText, (0,(10 * x),(8 * x)), font=font)

# Draw Text on top of where the loop stopped with a slightly different shade of color for clarity/styling.
draw.text((60, 10), inputText, (130,255,190), font=font)

# Resize and apply AA.
size = 300, 300
img2.thumbnail(img.size, Image.ANTIALIAS)

# Paste created transparent text layer onto BG.
offset = (20, 20)
img.paste(img2, offset,mask=img2)

img.show()
