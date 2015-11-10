# to import from node.py
from node.py import *


class inputtrans:	#input to a transaction
	def __init__(self):
		self.hash = None
		self.n = 0
		self.sign = None
		self.pub = 0
		
class outputtrans:	#output to a transaction
	def __init__(self):
		self.value = 0
		self.addr = 0

class transaction:
	def __init__(self,hashaddr,incount,outcount):
		self.hash = hashaddr
		self.incount = incount
		self.outcount = outcount
		self.inlist = None
		self.outlist = None
		
	def createinlist(self):
		self.inlist = [inputtrans() for i in range (self.incount)]
		
	def createoutlist(self):
		self.outlist = [outputtrans() for i in range (self.outcount)]
		
		#to validate transaction; ie, checking the input list of the transaction, ie checking the validity of all the transactions in the input list			
		'''
		Algorithm to validatetrans: 
		
		1. For each transaction (ith) in the input list
				a. find the blockhash of the block to which it belongs (using the mapping stored in the database)
				e. find the block in the blockchain
				b. traverse the block to find the transaction 
				c. value(i) = value of the nth output of that transaction
				d. address(i) = address of the nth output of that transaction
		2. For all i, 
				a. address(i) must be equal to public key of the ith transaction in the input list 
				b. sum of value(i) must be stored in a variable called inputsum		
				c. value(i) must not be spent in any transaction after that
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

			#finding the block in the blockchain		
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
			
			

				
			
