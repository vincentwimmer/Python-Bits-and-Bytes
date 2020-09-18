import requests
import re

url = 'https://www.python.org/'

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
	}

getPage = requests.get(url, headers=headers, timeout=(60))

def NameOut():
	getName = getPage.text.find('<title>')
	nameParse = (getPage.text[(getName+7) : (getName+100)])
	nameFixed = re.split("<|\|", nameParse)
	return nameFixed[0]

print(NameOut())
