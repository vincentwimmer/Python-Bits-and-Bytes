from dhooks import Webhook, Embed
import requests

#Offline
with open('avatar.png', 'rb') as f:
    image1 = f.read() # bytes

#Online
url = 'https://url.com/avatar.png'
getImage2 = requests.get(url)
image2 = getImage2.content # bytes


hook = Webhook('https://discordapp.com/api/webhooks/hook')

hook.modify(name='Bob', avatar=image1)
hook.send("Hello there! I'm a webhook :open_mouth:")

hook.modify(name='Bob', avatar=image2)
hook.send("Hello there! I'm a webhook :open_mouth:")
