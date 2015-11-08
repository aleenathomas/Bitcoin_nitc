import pickle
import socket
from transaction import *

#TCP_IP = '127.0.0.1'
#TCP_PORT = 5005
#BUFFER_SIZE = 1024

addr = ('',5005) #added #host,port

s = socket.socket ( socket.AF_INET, socket.SOCK_DGRAM ) #SOCK_STREAM
s.bind(addr) #changed
#s.listen(10)

#conn, addr = s.accept()

while True:
	objrcv,addr = pickle.loads ( s.recvfrom(1024))
	print "From addr: '%s', hash: '%s'" % (addr[0], objrcv.hash)

s.close()

#print "conn info: ", conn
#objrcv = pickle.loads ( conn.recv ( 1024 ) )
#print "conn recv: ", objrcv
#print "conn from: ", addr

#print objrcv.hash
#print objrcv.inlist[0].hash




