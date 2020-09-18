import re

#Get Name
name = "Jack cat -red Game Royal Tiger apple"
nameparse = re.split(" |-|/", name.lower())

#Set Keywords
poskeywords = {"red", "Royal", "Cat"}
negkeywords = {"Dog", "Green", "Play"}

if poskeywords & set(nameparse):
     if negkeywords & set(nameparse):
          pass
     else:
          poskeywordsList = str(poskeywords & set(nameparse))
          poskeywordsSplit = re.sub('[}{\']', '', poskeywordsList)
          print('Positive Keywords are:', poskeywordsSplit)
