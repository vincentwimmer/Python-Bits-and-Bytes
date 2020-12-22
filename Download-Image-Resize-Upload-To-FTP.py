from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO
from datetime import datetime
import requests
import ftplib

# Configure connection
session = ftplib.FTP('FTPServer','USER','PASS')

# Set Image to download
rUrl = "https://www.python.org/static/img/python-logo.png"

# Create canvas
bg = Image.new("RGBA", (350, 350), (255, 255, 255, 255))

# Download Image and resize to canvas with Anti-Aliasing
response = requests.get(rUrl)
fg = Image.open(BytesIO(response.content))
fgSize = 350, 350
fg.thumbnail(fgSize, Image.ANTIALIAS)

# Paste resized Image to center of canvas.
img_w, img_h = fg.size
bg_w, bg_h = bg.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
bg.paste(fg, offset,mask=fg)

# Set file name with today's date
ftpStr = str(datetime.today().strftime('%Y-%m-%d')+"-test.png")

# Prep byte data for Upload
bg.seek(0)
temp = BytesIO()
bg.save(temp, format='PNG')
temp.seek(0)

# Upload Image to FTP
session.storbinary('STOR '+ftpStr, temp)
session.quit()
