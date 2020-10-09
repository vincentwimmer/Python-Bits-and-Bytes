import socket

host = socket.gethostname()
ip = socket.gethostbyname(host)

print("Host:",host)
print("IP:",ip)
