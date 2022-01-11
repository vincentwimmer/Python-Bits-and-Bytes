import requests

WEBHOOK_URL = 'https://discord.com/api/webhooks/token/token'
requests.post(WEBHOOK_URL, { "content": "test" })
