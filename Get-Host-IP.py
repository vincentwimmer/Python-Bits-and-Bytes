import socket

host = socket.gethostname()
ip = socket.gethostbyname(host)
fqdn = socket.getfqdn()

print("Host:",host)
print("IP:",ip)
print("FQDN:", fqdn)
