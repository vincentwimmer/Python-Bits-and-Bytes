from PIL import Image
import requests 
from io import BytesIO                                                                      

# Grab the star image from this answer
response = requests.get('https://avatars1.githubusercontent.com/u/9145304?s=460&u=1126a26b2ffac6187f655816e5eb0ffcb55c429b&v=4')                              

# Make it into a PIL image
img = Image.open(BytesIO(response.content))

img.show()
