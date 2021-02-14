#Write a Python to find local IP addresses using Python's stdlib.

#02_13_21

import socket

print(socket.gethostbyname(socket.gethostname()))

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

#makes no sense to me????