from websocket import create_connection
import json

# Header
headers = json.dumps({
	"Accept-Encoding" : "gzip, deflate, br",
	"Accept-Language" : "en-US,en;q=0.9",
	"Cache-Control" : "no-cache",
	"Connection" : "Upgrade",
	"Host" : "prod-pusher.backend-capital.com",
	"Origin" : "https://capital.com",
	"Pragma" : "no-cache",
	"Sec-WebSocket-Extensions" : "permessage-deflate; client_max_window_bits",
	"Sec-WebSocket-Key" : "0gTLZSs2ALEjQfop9zPNCA==",
	"Sec-WebSocket-Version" : "13",
	"Upgrade" : "websocket",
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
})

# Create Connection
ws = create_connection('wss://prod-pusher.backend-capital.com/app/MvtsstCbm?protocol=7&client=js&version=4.2.2&flash=false',headers=headers)

# Handshake
ws.send('{"event":"pusher:subscribe","data":{"channel":"27236401963685060"}}')


# Print Received Info
while True:
	try:
		result = ws.recv()
		try: 
			b = json.loads(result)
			b = json.loads(b['data'])
			print("XLM - [ Bid:",b['bid'], "] - [ Ask:",b['ask'],"]")
		except:
			print(result)

	except Exception as e:
		print(e)
		break
