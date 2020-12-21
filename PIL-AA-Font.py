from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw   

img = Image.new("RGB", (300, 300), (255, 255, 255))

# Create transparent image/layer at 3x scale of base image
img2 = Image.new("RGBA", (900, 900), (255, 255, 255, 0))
draw = ImageDraw.Draw(img2)
font = ImageFont.truetype("Roboto-Medium.ttf", 72) # 72 divided by 3 = 24.
draw.text((0, 0), "//&&||$$123ABC@@", (0,0,0), font=font)

# Resize to base image width/height and Anti-Alias
img2.thumbnail(img.size, Image.ANTIALIAS)

# Paste image as layer with an offset.
offset = (20, 20)
img.paste(img2, offset,mask=img2)

img.show()
