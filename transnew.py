from ecdsa import SigningKey
from node import *

class inputtrans:			#input to a transaction
	def __init__(self):
		self.hash = None
		self.n = 0
		self.sign = None	#signature of the sender
		self.pub = 0		#public key of the sender
		
class outputtrans:			#output to a transaction
	def __init__(self):
		self.value = 0
		self.addr = 0

#added sign to transaction class; sign = node.privatekey.sign(transaction); need to initialise this in createtrans function
class transaction:
	def __init__(self,incount,outcount):
		
		self.incount = incount
		self.outcount = outcount
		self.inlist = None
		self.outlist = None
		self.sign = None
		self.hash = None

def filetotrans(filename):			# Verified working
	f = open(filename,  'r')		
	incount = f.readline() 		# reading incount from the file	
	outcount = f.readline()		# reading outcount from the file

	T = transaction(incount,outcount)		# create a new transaction object					
		
	T.sign = f.readline()
	T.hash = f.readline()
	T.inlist = [inputtrans() for i in range (T.incount)]
	for i in range(T.incount):			
		T.inlist[i].hash = f.readline()	# reading hash, n, sign and pub values from file ans storing it in inlist[i]
		T.inlist[i].n = f.readline()
		T.inlist[i].sign = f.readline()
		T.inlist[i].pub = f.readline()
	
	T.outlist = [outputtrans() for i in range (T.outcount)]		# creating array outlist[]
	for i in range(T.outcount):			
		T.outlist[i].value = f.readline()	# reading value and addr values from file ans storing it in outlist[i]
		T.outlist[i].addr = f.readline()
	
	f.close()
	return T

def transtofile(T,filename):		# Verified working
	f = open( filename, 'w' )
	f.write('%d\n' % T.incount)
	f.write('%d\n' % T.outcount)
	f.write( T.sign + '\n' )
	f.write( T.hash )

	for i in range (T.incount) :
		f.write(T.inlist[i].hash)
		f.write(T.inlist[i].n)
		f.write( T.inlist[i].sign + '\n')
		f.write(T.inlist[i].pub )
		
	
	for i in range (T.outcount) :
		f.write( T.outlist[i].value )
		f.write( T.outlist[i].addr )
	
	f.close	

#function to sign a transaction and transfer to a file
def signtrans(node, filename):		# Verified working
	f = open( filename, 'r' )

	incount = int(f.readline())	# reading incount from the file	
	outcount = int(f.readline())	# reading outcount from the file
	sign = f.readline()
	
	T = transaction(incount,outcount)		# create a new transaction object
	T.hash = f.readline()
	transstr = str(T.incount) + str(T.outcount) + str(T.hash)
	T.inlist = [inputtrans() for i in range (T.incount)]	# creating array inlist[]
	for i in range (T.incount) :
		T.inlist[i].hash = f.readline()	# reading hash, n, sign and pub values from file ans storing it in inlist[i]
		T.inlist[i].n = f.readline()
		T.inlist[i].sign = f.readline()
		T.inlist[i].pub = f.readline()
		#append each attribute of inlist[i] and sign it
		inliststr = str(T.inlist[i].hash) + str(T.inlist[i].n) + str(T.inlist[i].pub)
		T.inlist[i].sign = node.privatekey.sign(inliststr)
		print T.inlist[i].sign
		

		transstr = transstr + str(T.inlist[i].hash) + str(T.inlist[i].n) + str(T.inlist[i].pub) + str(T.inlist[i].sign)
		
	T.outlist = [outputtrans() for i in range (T.outcount)]		# creating array outlist[]
	for i in range (T.outcount) :
		T.outlist[i].value = f.readline()	# reading value and addr values from file ans storing it in outlist[i]
		T.outlist[i].addr = f.readline()
		transstr = transstr + str(T.outlist[i].value) + str(T.outlist[i].addr)
	

	
	T.sign = node.privatekey.sign(transstr)
	print T.sign
	f.close	
	transtofile(T,"signedtrans.txt")	
	return T
