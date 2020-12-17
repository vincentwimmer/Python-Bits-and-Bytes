from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests 
from io import BytesIO     

# Download and resize image.
response = requests.get('https://avatars1.githubusercontent.com/u/9145304?s=460&u=1126a26b2ffac6187f655816e5eb0ffcb55c429b&v=4')
bg = Image.open(BytesIO(response.content))
bg_resized = bg.resize((200,200))

# Open local image.
fg = Image.open('overlay.png').convert('RGBA')

# Setup Drawing.
draw = ImageDraw.Draw(bg_resized, "RGBA")
# Draw Rectangle.
draw.rectangle((20, 20, 100, 70), outline=(33,255,33,255), fill=(33,33,33,150))
# Set font and write characters.
font = ImageFont.truetype("Roboto-Medium.ttf", 24)
draw.text((38, 30),"YEY",(33,255,33),font=font)

# Bring everything together.
bg_resized.paste(fg,box=(0,0),mask=fg)

bg_resized.show()
#bg_resized.save('result.png')
