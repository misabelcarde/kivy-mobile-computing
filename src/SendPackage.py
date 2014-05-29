from Singleton import *

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5006


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#msg = "'"+str(Singleton().matrix)+"'"


def send (text):
	sock.sendto(bytes(text, 'UTF-8'), (UDP_IP, UDP_PORT))
# class SendPackage(text):
# 	def __init__(self, **kwargs):
# 		super(SendPackage, self).__init__(**kwargs)
# 	def send (self):
# 		pass