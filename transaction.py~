# to import from node.py

from ecdsa import SigningKey
from node import *
from treestruct import *
import block

dummy_none = "456"			#used to test run gethashofblock

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
		self.STAR = 100	#the total number of bitcoins given by the faculty
		self.incount = incount
		self.outcount = outcount
		self.inlist = [inputtrans() for i in range (self.incount)]
		self.outlist = [outputtrans() for i in range (self.outcount)]
		self.sign = None
		self.hash = None
	'''	
	def createinlist(self):
		self.inlist = [inputtrans() for i in range (self.incount)]
		for i in range(self.incount):
			inlist[i].hash = raw_input('Enter the hash of input transaction %d',i+1)
			inlist[i].n = raw_input('Enter the n value of input transaction %d',i+1) 
			inlist[i].pub = raw_input('Enter your public key')
			#inlist[i].sign=sk.sign(inlist[i])(inlist[i] in string format??)

		
	def createoutlist(self):
		self.outlist = [outputtrans() for i in range (self.outcount)]
		
		#requires inlist and outlist data!
		privkey=raw_input('Enter your private key')
					#sk = SigningKey.generate() # uses NIST192p(private key)
					#vk = sk.get_verifying_key()(public key)			
		for i in range(self.outcount):
			outlist[i].value = raw_input('Enter the value of output transaction %d',i+1)
			outlist[i].addr = raw_input('Enter the dest addr of output transaction %d',i+1) 			
						
		self.hash = gethashoftransaction(self)
	'''	
	#to validate transaction; ie, checking the input list of the transaction, ie checking the validity of all the transactions in the input list			
	'''
		Algorithm to validatetrans: 
		
		1. For each transaction (ith) in the input list
				a. find the blockhash of the block to which it belongs (using the mapping stored in the database)
				e. find the block in the blockchain
				b. traverse the block to find the transaction, say inputtransation
				c. value(i) = value of the nth output of that transaction
				d. address(i) = address of the nth output of that transaction
		2. For all i, 
				a. verify the digital signature 					
					sk = SigningKey.generate() # uses NIST192p
					vk = sk.get_verifying_key()
					signature = sk.sign("message")
					assert vk.verify(signature, "message")
				b. output must not already be spent
					ptr = blockhead
					while ptr ! = currentblock
						for each transaction t in the block
							any output of t !=  nth output of the inputtransaction			
				c. address(i) must be equal to public key of the ith transaction in the input list 
				d. sum of value(i) must be stored in a variable called inputsum						
		3. For all outputs, add the value fields to outputsum
		4. Check whether inputsum = outputsum
		
		'''
	def validatetrans(self, node):
		
		# check 1 : check whether the transaction is already present in the outstanding block of the node or in the blockchain	
		# part 1 : checking in the blockchain
		blockptr = node.blockhead
		while blockptr.parent != None and blockptr.propblockhash != 9999:	# ie, search till the genesis block
			for i in range(blockptr.propblock.max_trans_num) :	
				if (blockptr.propblock.translist[i].hash == self.hash) :
					print "Transaction already in the blockchain"
					return False
			blockptr = blockptr.parent
		# end check 1
		# part 2 : checking in the block currently filled by the node
		if node.currentblock != None:
			for i in range(block.block(None).max_trans_num):
				'''
				print "inside for loop"
				print "node.currentblock.translist[i].hash"
				print node.currentblock.translist[i].hash
				print "self.hash"				
				print self.hash
				'''
				if node.currentblock.translist[i].hash == self.hash:
					print "Transaction already received"
					return False		

		#check 2 : checking whether the inlist is empty, ie whether it is a special transaction in whcih the faculty gives STAR bitcoins to a student
		flag = 0
		if self.incount == 0:
			flag = 1 
		# end check 2

		inputsum = 0
		transptr = None
		for l in range(self.incount):	# after each pass, one input transaction from the input list is verified
			transhash = self.inlist[l].hash					

			for j in range(node.top):	# iterate through all transactions in the database ie till 'top' transactions								
				if node.database[ j ] [ 0 ] == transhash:   # if the transaction hash matches, then the block in which 
					blockhash = node.database[ j ] [1 ]
					break

			# finding the block in the blockchain using the blockhash
			blockptr = node.blockhead
			while blockptr.parent != None and blockptr.propblockhash != blockhash:	# ie, search till the genesis block
				blockptr = blockptr.parent					
			# searching for the transaction in the block using transaction hash
			for i in range(block.block(None).max_trans_num) :	
				if (blockptr.propblock != None and blockptr.propblock.translist[i].hash == transhash) :
				    	transptr = blockptr.propblock.translist[i]		# transptr points to the input transaction
				    	break					
			# check 3 : checking whether the inputs are already spent or not
			# checking whether the current transaction's (pointed by transptr) hash is given as the hash of any input to any transaction that comes after that
			ptr = node.blockhead 
			while ptr != blockptr:
				for j in range(blockptr.propblock.max_trans_num):	# every transaction in the block
					for k in range(ptr.propblock.incount):		# every input to the transaction
						if ptr.propblock.inlist[k].hash == transptr.hash:	# if input was spent, return false
							print "Input already spent, possible double spent attempt!"
							return False
			'''
			for j in range(i+1, block.max_trans_num):	# for those transactions that come after the input transaction
				for k in range(ptr.propblock.translist[j].incount):		# every input to the transaction
					if ptr.propblock.translist[j].inlist[k].hash == transptr.hash:	# if input was spent, return false
						print "problem is here and j is %d", j
						return False	
			'''
			# end check 3			
			'''
			#verifying the signature(Not sure if it will work!)
			transstr = self.incount + self.outcount
			
			for i in range (self.incount):
				inliststr = str(self.inlist[i].hash) + str(self.inlist[i].n) + str(self.inlist[i].pub)

				assert node.publickey.verify(self.inlist[i].sign, inliststr)
			

			
				transstr = transstr + str(self.inlist[i].hash) + str(self.inlist[i].n) + str(self.inlist[i].pub) + str(self.inlist[i].sign)
			for i in range (self.outcount) :
				transstr = transstr + str(self.outlist[i].value) + str(self.outlist[i].addr)
			transstr = transstr + self.hash
			assert node.publickey.verify(self.sign, transstr)	
			'''
			if(transptr== None):
				print('transptr is null')
			if flag != 1 and transptr != None:	# ie checking whether its a transcation with empty inlist
				index =  self.inlist[l].n   
				address = self.inlist[l].pub		
				inputsum = inputsum + transptr.outlist[index].value  		
				if transptr.outlist[index].addr != address :					
					return False
			
			
		outputsum = 0
		for i in range(self.outcount) :
			outputsum = outputsum + self.outlist[i].value
			
		if flag == 1:
			if self.outcount == 1 and outputsum != self.STAR:
				print "Invalid transaction, attempt for possible double spent!"
				return False
		
		else:			
			if inputsum < outputsum :
				print 'Balance is less than the requested sum'
				return False
		print "Transaction has been successfully verified"
		return True
						
				
'''
Function to create a transaction object from the text file received

Algorithm:
	
	Create a new object T of type transaction
	T.incount = readline()
	Create an array of type inlist[incount] 
	for i=0; i<T.incount; i++
		Create a new object I of type inputtrans
			I.hash = readline()
			I.n = readline()
			I.sign = readline()
			I.pub = readline()
		Add I to T.inlist[i] 
	T.outcount = readline()
	Create an array of type outlist[outcount] 
	for i=0; i<T.outcount; i++
		Create a new object O of type inputtrans
			O.value = readline()
			O.addr = readline()
		Add O to T.outlist[i] 	
	return T
	
'''			

def filetotrans(filename):			# Verified working
	f = open(filename,  'r')		
	incount = int( block.readword(f.readline()) ) 	# reading incount from the file	
	outcount = int( block.readword(f.readline()) )	# reading outcount from the file

	T = transaction(incount,outcount)		# create a new transaction object					
	T.inlist = [inputtrans() for i in range (T.incount)]	# creating array inlist[]
	T.sign = block.readword(f.readline())
	T.hash = block.readword(f.readline())
	for i in range(T.incount):			
		T.inlist[i].hash = block.readword(f.readline())# reading hash, n, sign and pub values from file ans storing it in inlist[i]
		T.inlist[i].n = int(block.readword(f.readline()))
		T.inlist[i].sign = block.readword(f.readline())
		T.inlist[i].pub = block.readword(f.readline())
	
	T.outlist = [outputtrans() for i in range (T.outcount)]		# creating array outlist[]
	for i in range(T.outcount):
		T.outlist[i].value = int(block.readword(f.readline()))# reading value and addr values from file ans storing it in outlist[i]

		T.outlist[i].addr = block.readword(f.readline())
	
	f.close()
	return T
	
'''		
Function to create a text file from a transaction

Algorithm:

	Input: object T of transaction
	
	write(T.incount)
		
	for i in range 0 to T.incount-1
		write(T.inlist[i].hash)
		write(T.inlist[i].n)
		write(T.inlist[i].sign)
		write(T.inlist[i].pub)
		
	write(T.outcount)
	
	for i in range 0 to T.outcount-1
		write(T.outlist[i].value)
		write(T.outlist[i].addr)
		
'''	


def transtofile(T,filename):		# Verified working
	f = open( filename, 'w' )

	f.write( str(T.incount) + '\n' )
	f.write( str(T.outcount) + '\n' )
	f.write( str(T.sign ) + '\n')
	f.write( str(T.hash ) + '\n')

	for i in range (T.incount) :
		f.write( str(T.inlist[i].hash) + '\n')
		f.write( str(T.inlist[i].n) + '\n')
		f.write( str(T.inlist[i].sign) + '\n')
		f.write( str(T.inlist[i].pub ) + '\n')
		
	
	for i in range (T.outcount) :
		f.write( str(T.outlist[i].value ) + '\n')
		f.write( str(T.outlist[i].addr ) + '\n')	
	f.close	

#function to sign a transaction and transfer to a file
def signtrans(node, filename):		# Verified working
	f = open( filename, 'r' )

	incount = int(block.readword(f.readline()))	# reading incount from the file	
	outcount = int(block.readword(f.readline()))	# reading outcount from the file
	sign = block.readword(f.readline())
	
	T = transaction(incount,outcount)		# create a new transaction object
	T.hash = block.readword(f.readline())
	hashstr = str(T.incount) + str(T.outcount) 
	transstr = str(T.incount) + str(T.outcount)
	T.inlist = [inputtrans() for i in range (T.incount)]	# creating array inlist[]
	for i in range (T.incount) :
		T.inlist[i].hash = block.readword(f.readline())	# reading hash, n, sign and pub values from file ans storing it in inlist[i]
		T.inlist[i].n = int(block.readword(f.readline()))
		T.inlist[i].sign = block.readword(f.readline())
		T.inlist[i].pub = block.readword(f.readline())
		#append each attribute of inlist[i] and sign it
		hashinstr = str(T.inlist[i].n) + str(T.inlist[i].pub)
		hashstr = hashstr + hashinstr
		#T.inlist[i].hash = gethash(hashinstr) #Commented out bcos validation was failing

		inliststr = str(T.inlist[i].hash) + str(T.inlist[i].n) + str(T.inlist[i].pub)
		T.inlist[i].sign = node.privatekey.sign(inliststr)
		#print T.inlist[i].sign
		

		transstr = transstr + str(T.inlist[i].hash) + str(T.inlist[i].n) + str(T.inlist[i].pub) + str(T.inlist[i].sign)
		
	T.outlist = [outputtrans() for i in range (T.outcount)]		# creating array outlist[]
	for i in range (T.outcount) :
		T.outlist[i].value = int(block.readword(f.readline()))	# reading value and addr values from file ans storing it in outlist[i]
		T.outlist[i].addr = block.readword(f.readline())
		transstr = transstr + str(T.outlist[i].value) + str(T.outlist[i].addr)
		hashstr = hashstr + str(T.outlist[i].value) + str(T.outlist[i].addr)

	#T.hash = gethash(hashstr)	commented because of the difficulty in finding hash of the input transaction
	transstr = transstr + str(T.hash)
	T.sign = node.privatekey.sign(transstr)
	#print T.sign
	f.close	
	transtofile(T,"signedtrans4.txt")	

	
# function to add the mapping of all transactions in the newly proposed block to the database
def maptransaction(block, node):
	for i in range(block.max_trans_num):
		node.database [ node.top] [ 0 ] = block.translist[i].hash
		node.database[ node.top] [1] = gethashofblock(block)		# the block hash of the corresponding trasaction hash
		node.top = node.top + 1					# to denote the that one more entry has been added to the database
		

