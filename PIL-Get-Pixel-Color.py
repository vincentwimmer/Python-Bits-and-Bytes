from PIL import Image
  
# Open 24px x 24px image
im = Image.open(r"C:/Out/001.png")
px = im.load()
print (px[1, 1])
print (px[4, 4])
print (px[15, 4])
print (px[4, 15])
print (px[15, 15])
