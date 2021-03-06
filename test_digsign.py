#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ecdsa import SigningKey
from transaction	 import *
from node import *
'''
privatekey = SigningKey.generate()	
publickey = privatekey.get_verifying_key()
message = "Reshma" + "Thomas"
signature = privatekey.sign(message)
#print "Signature is", signature
assert publickey.verify(signature, message)
'''
#checked signing,verification problem
filename = "newtrans.txt"
newnode = node()
#newtrans = filetotrans(filename)
#transtofile(newtrans, "new.txt")
signtrans(newnode, filename)


T = filetotrans("signedtrans.txt")

#verifying the signature(Not sure if it will work!)
transstr = str(T.incount) + str(T.outcount) 
		
for i in range (T.incount):
	
	inliststr = str(T.inlist[i].hash) + str(T.inlist[i].n) + str(T.inlist[i].pub)
	assert newnode.publickey.verify(T.inlist[i].sign, inliststr)
	
	
			
	transstr = transstr + str(T.inlist[i].hash) + str(T.inlist[i].n) + str(T.inlist[i].pub) + str(T.inlist[i].sign)
for i in range (T.outcount) :
	
	transstr = transstr + str(T.outlist[i].value) + str(T.outlist[i].addr)
transstr = transstr + T.hash
assert newnode.publickey.verify(T.sign, transstr)	

