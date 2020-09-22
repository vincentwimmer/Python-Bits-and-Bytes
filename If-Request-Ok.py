import requests

url = "http://google.com/"

req = requests.get(url)

if req.ok:
	print(req)
