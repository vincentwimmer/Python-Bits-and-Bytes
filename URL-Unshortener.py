import requests
import urllib.parse

url = "https://bit.ly/35RF3kn"

session = requests.Session()
resp = session.head(url, allow_redirects=True)

print(resp.url)
