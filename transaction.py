# to import from node.py
from node.py import *
from gethash.py import *



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

class transaction:
	def __init__(self,incount,outcount):
		
		self.incount = incount
		self.outcount = outcount
		self.inlist = None
		self.outlist = None
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
		inputsum = 0
		for i in range(self.incount):
			transhash = self.inlist[i].hash
			# checking from the block
			
			for j in range(node.maxnumtrans):	# iterate through all transactions in the database
				if node.database[ j,0 ] == transhash:	# if the transaction hash matches, then the block in which 
					blockhash = node.database[ j,1 ]
					break

			# finding the block in the blockchain		
			blockptr = blockhead
			while blockptr != blockhash:
				blockptr = blockptr.prev_hash		
			for i in range(max_trans_num)	
				if blockptr.translist[i].hash == transhash
			    	transptr = translist[i]
			    	break
			index =  self.inlist[i].n   
			address = self.inlist[i].pub		
			inputsum = inputsum + transptr.outlist[index].value    			
			if 	transptr.outlist[index].addr != address
				return False
		outputsum = 0
		for i in range(self.outcount)
			outputsum = outputsum + self.outlist[i].value
		if inputsum != outputsum
			return False
		return True
						
				
'''
Function to create a transaction from the text file received

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

	def filetotrans(filename):	
		f = open(filename,  'r')		
		T = transaction()	# create a new transaction object
		T.incount = f.readline()	# reading incount from the file			
		T.inlist = [inputtrans() for i in range (T.incount)]	# creating array inlist[]
		for i in range(T.incount):			
			inlist[i].hash = readline()	# reading hash, n, sign and pub values from file ans storing it in inlist[i]
			inlist[i].n = readline()
			inlist[i].sign = readline()
			inlist[i].pub = readline()
		T.outcount = f.readline()	# reading outcount from the file			
		T.outlist = [outputtrans() for i in range (T.outcount)]		# creating array outlist[]
		for i in range(T.outcount):			
			outlist[i].value = readline()	# reading value and addr values from file ans storing it in outlist[i]
			outlist[i].addr = readline()
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


def transtofile(T,filename):
	f = open( filename, 'w' )
	f.write( T.incount + '\n')
	for i in range T.incount
		f.write( T.inlist[i].hash + '\n')
		f.write( T.inlist[i].n + '\n')
		f.write( T.inlist[i].sign + '\n')
		f.write( T.inlist[i].pub + '\n')
		
	f.write( T.outcount + '\n')
	for i in range T.outcount
		f.write( T.outlist[i].value + '\n')
		f.write( T.outlist[i].addr + '\n')
		
	f.close	
	
	
# function to add the mapping of all transactions in the newly proposed block to the database
def maptransaction(self, block):
	for i in range(	max_trans_num):
		database [ top, 0 ] = block.translist[i].hash
		database[ top, 1] = block.prevhash		# the block hash of the corresponding trasaction hash
		top = top + 1					# to denote the that one more entry has been added to the database
		

