#pip install pyperclip
import pyperclip as pc
import random

tagCount = 4 #Set to number of tags you want. Must be within range of how many tags exist in tagList

tagList = """
#test1
#test2
#test3
#test4
"""

tags = tagList.splitlines()
tags = tags[1:]
random.shuffle(tags)
tagOut = ' '.join(tags[:tagCount])

pc.copy(tagOut)
print(pc.paste())
