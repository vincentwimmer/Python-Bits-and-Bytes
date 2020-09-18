import re

string = "Python,Bits_and-Byt!es"

res = re.split(',|_|-|!', string) 

print(str(res))
