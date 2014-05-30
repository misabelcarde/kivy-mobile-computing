from Singleton import *

import socket

#UDP_IP = Singleton().opponentIP
UDP_PORT = 5006


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#msg = "'"+str(Singleton().matrix)+"'"


def send (opponentIP,text):
	sock.sendto(bytes(text, 'UTF-8'), (opponentIP, UDP_PORT))
# class SendPackage(text):
# 	def __init__(self, **kwargs):
# 		super(SendPackage, self).__init__(**kwargs)
# 	def send (self):
# 		pass