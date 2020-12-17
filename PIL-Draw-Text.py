from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests 
from io import BytesIO     

response = requests.get('https://avatars1.githubusercontent.com/u/9145304?s=460&u=1126a26b2ffac6187f655816e5eb0ffcb55c429b&v=4')  

img = Image.open(BytesIO(response.content))
draw = ImageDraw.Draw(img, "RGBA")
draw.rectangle((20, 20, 100, 70), outline=(33,255,33,255), fill=(33,33,33,150))
font = ImageFont.truetype("./Roboto-Medium.ttf", 24)
draw.text((38, 30),"YEY",(33,255,33),font=font)

img.show()
