#!/usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))

print(host)

s.listen(5)
while True:
	c,addr = s.accept()
	print('Got connection from', addr)
	c.send('Thank you for connecting')
	msg = c.recv(1024)
	if msg == 'ping':
		c.send('pong')
	c.close()

