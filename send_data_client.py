from transaction import *

import pickle
import socket

newtrans=transaction(123,2,1)
newtrans.createinlist()
newtrans.createoutlist()

trans = pickle.dumps ( newtrans )

addr=('255.255.255.255','5005') #added

client = socket.socket ( socket.AF_INET, socket.SOCK_DGRAM ) #SOCK_STREAM
#client.connect (('localhost', 5005))
#client.send(trans)
#client.close()

while True:
	if client.sendto(trans,addr):
		print('Sending... ')
client.close()
