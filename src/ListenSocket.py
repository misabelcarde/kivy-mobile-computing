from Singleton import *

import socket

UDP_IP = str(socket.gethostbyname(socket.gethostname()))
UDP_PORT = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def splitList(listStr):
    res = []
    l =  listStr.split('[')
    for e in l:
        if e!="":
            aux=[]
            for i in e.split(','):
                if i.split(']')[0] != ' ':
                    aux.append(int(i.split(']')[0]))
            res.append(aux)
    return res

while True:
    data, addr = sock.recvfrom(1024)
    dataProc = data.decode(encoding='UTF-8')
    if(dataProc.split(',')[0] == "1"):
    	Singleton().matrix2 = dataProc
    	print ("split [0]" + dataProc.split(',')[0])
    	print ("received message unoooo: " + dataProc)
    else:
    	Singleton().matrix = dataProc
    	print ("received message nno unoo: " + dataProc)


    
while True:
    data, addr = sock.recvfrom(1024)
    dataProc = data.decode(encoding='UTF-8')
    if(dataProc.split(',')[0] == "1"):
    	print ("split [0]" + dataProc.split(',')[0])
    	print ("received message unoooo: " + dataProc)
    	print(splitList(dataProc.split(',')[1]))
    	Singleton().matrix = splitList(dataProc.split(',')[1])
    else:
    	Singleton().matrix = dataProc
    	#print ("received message nno unoo: " + dataProc)
    	print(dataProc)