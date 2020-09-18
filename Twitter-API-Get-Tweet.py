import requests
import json
import re
import html

getInfo = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=USERNAME&count=1', headers={"Authorization": "Bearer AAAAAA"})
parsedInfo = json.loads(getInfo.text)[0]

print("")
print("---------------------------------------------")
print("@" + str(parsedInfo['user']['screen_name']))
print(str(parsedInfo['user']['profile_image_url']))
print(str(parsedInfo['user']['name']))
print(str(parsedInfo['user']['description']))
print("")
print(str(parsedInfo['created_at']))
msgText = html.unescape(str(parsedInfo['text']))
print(msgText)
print("")
print("---------------------------------------------")
for y in parsedInfo['entities']['urls']:
    print ("Expanded Link:", y.get('expanded_url'))
print("---------------------------------------------")
