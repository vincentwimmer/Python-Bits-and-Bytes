#Easily convert images to portable bitmaps and do things like displaying them on a Pi Pico OLED screen.
from PIL import Image

im = Image.open("file.png")
#im = im.convert('L') # Convert to dithered black and white
im = im.convert('1')
im.save("file.pbm")
