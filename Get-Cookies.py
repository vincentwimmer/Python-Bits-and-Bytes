import requests

cookisession = requests.Session()
cookiresponse = cookisession.get('https://github.com/vincentwimmer/')

print(cookisession.cookies.get_dict())
print(cookiresponse.cookies.get_dict())
