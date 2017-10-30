#!/usr/bin/python
import socket

s = socket.socket()
host = 'cs001.local.host.com'
port = 12345

s.connect((host,port))
print (s.recv(1024))
cmd = 'ping'
s.send(cmd)
result = s.recv(1024)
if result == 'pong':
	print(result)

s.close()

