#import python-bitcoinlib
import transaction
import fileinput

#dummy values to verify working of gethash as None cannot be used
dummy_nonce = 123
dummy_hash = 567
MAXTRANS = 5

class block:
	def __init__(self,prev_hash):
		self.prev_hash = prev_hash
		self.max_trans_num = 5
		self.nonce = dummy_nonce
		self.translist = [transaction.transaction(0,0) for i in range (self.max_trans_num)] 	
		
	'''
	Add transaction to a block:
		1.Verify whether the transaction is valid
		2.If there is an invalid entry in between the list of transactions in the block
			a.copy the transaction in the order to a new block
			b.add the new transaction to the new block
		  Else
		  	a.add the new transaction to the current block
			
	'''
		
	def add_trans_to_block(self,newtrans): 							
		#verify transaction
		invalidtrans = 0
		for i in range (self.max_trans_num-1):
			if (self.translist[i].hash == None) and (self.translist[i+1].hash != None): #if there is an invalid entry in between				
				invalidtrans = 1
				newblock = block (self.prev_hash)		#create a newblock with same contents
				i = 0
				j = 0
				while i < self.max_trans_num :
					if self.translist[i].hash != None :
						newblock.translist[j].hash = self.translist[i].hash
						newblock.translist[j].incount = self.translist[i].incount
						newblock.translist[j].outcount = self.translist[i].outcount
						newblock.translist[j].inlist = self.translist[i].inlist
						newblock.translist[j].outlist = self.translist[i].outlist
						newblock.translist[j].sign = self.translist[i].sign
						#newblock.n = newblock.n + 1
						j = j + 1
					i = i + 1
				newblock.translist[j] = newtrans	#add the new transaction to this new block
				return newblock
				#newblock.n = newblock.n + 1	
		if invalidtrans == 0 :
			for i in range (self.max_trans_num):
				if self.translist[i].hash == None :
					self.translist[i] = newtrans					
					return self

			
	def remove_trans_from_block(self,trans):
		for i in range (self.max_trans_num):
			if trans.hash == self.translist[i].hash:
				self.translist[i].hash = None
				break
				
				
	'''
	Propose block:
		1.If myvalid pointer is not the same as block head
			a.Compare the lengths of each branch.i.e.one ending at blockhead and other at myvalidptr
			b.If blockhead belongs to the longer branch
				i)change myvalidptr to blockhead
		2.Attach the new block to myvalidptr and change blockhead to myvalidptr
	
	'''
	'''	
	def propose_block(self , myvalidptr):
		if myvalidptr != blockhead :
			#decide whether to change it to blockhead !
			l1 = 0
			l2 = 0
			ptr = blockhead
			while ptr.prev_hash != None :
				l1 = l1 + 1
				ptr = ptr.prev_hash
			
			ptr=myvalidptr
			while ptr.prev_hash != None :
				l2 = l2 + 1
				ptr = ptr.prev_hash
				
			if l1 > l2 :
				myvalidptr = blockhead
				
		self.prev_hash=myvalidptr							#myvalidptr points to last block 
		myvalidptr=self									#in the consensus chain
		blockhead=myvalidptr								#add the new block there
		
	'''
	
	'''
	Propose a block:
	1.Attach the block to the longest chain	
	'''
	def propose_block(self , myvalidptr):
		self.prev_hash = blockhead
		block_head = self
		
		
	'''
	Function filetoblock to create a block from a received file

	Algorithm:
	Create a new object B of type block
	B.prev_hash = readline()
	B.max_trans_num = readline()
	B.nonce = readline()
	Create an array translist[max_trans_num]
	for i=0; i<B.max_trans_num; i++
		translist[i].incount = readline()
		Create an array of type inlist[incount] 
		for j=0; j<translist[i].incount; j++
			Create a new object I of type inputtrans
				I.hash = readline()
				I.n = readline()
				I.sign = readline()
				I.pub = readline()
			Add I to translist[i].inlist[j] 
		translist[i].outcount = readline()
		Create an array of type outlist[outcount] 
		for j=0; j<translist[i].outcount; j++
			Create a new object O of type inputtrans
				O.value = readline()
				O.addr = readline()
			Add O to translist[i].outlist[j] 
	return B
	'''
def readword(word):
	word2 = ""
	for c in word:
		if c != '\n':			
			word2 = word2 + c
	return word2
	
def filetoblock(filename) :				
	f = open(filename, 'r')
	prevhash = readword(f.readline())
	B = block(prevhash)
	B.max_trans_num = int(readword(f.readline()))
	B.nonce = int(readword(f.readline()))
	#B.translist = [transaction.transaction(0,0) for i in range (B.max_trans_num)] 	
	for i in range(B.max_trans_num) :		
		incount = int(readword(f.readline()))
		outcount = int(readword(f.readline()))
		T = transaction.transaction(incount,outcount)
		T.inlist = [transaction.inputtrans() for i1 in range (T.incount)]	#Create an array of type inlist[incount]
		T.sign = readword(f.readline())
		T.hash = readword(f.readline())
		for j in range(T.incount) :	# iterating through each input and adding them to the transaction's inlist
			I = transaction.inputtrans()
			I.hash = readword(f.readline())
			I.n = readword(f.readline())
			I.sign = readword(f.readline())
			I.pub = readword(f.readline())
			T.inlist[j] = I
	
		T.outlist = [transaction.outputtrans() for i2 in range (T.outcount)]	   #Create an array of type outlist[outcount] 
		for j in range(T.outcount) :	# iterating through each output and adding them to the transaction's outlist
			O = transaction.outputtrans()
			O.value = int(readword(f.readline()))
			O.addr = readword(f.readline())
			T.outlist[j] = O
	 	B.translist[i] = T	# adding the transaction to the block's translist
	return B
		
		
def blocktofile(B,filename):
	f = open( filename, 'w' )
	f.write(str(B.prev_hash) + '\n')
	f.write(str(B.max_trans_num) + '\n')
	f.write(str(B.nonce) + '\n')
	
	for i in range( B.max_trans_num) :
		f.write(str(B.translist[i].incount) + '\n')
		f.write(str(B.translist[i].outcount) + '\n')
		f.write(str(B.translist[i].sign) + '\n')
		f.write(str(B.translist[i].hash) + '\n')
		for j in range(B.translist[i].incount) :
			f.write(str(B.translist[i].inlist[j].hash) + '\n')
			f.write(str(B.translist[i].inlist[j].n) + '\n')
			f.write(str(B.translist[i].inlist[j].sign) + '\n')
			f.write(str(B.translist[i].inlist[j].pub) + '\n')
			
		for j in range(B.translist[i].outcount) :
			f.write(str(B.translist[i].outlist[j].value) + '\n')
			f.write(str(B.translist[i].outlist[j].addr) + '\n')	
	#rmnewline(filename, "test.txt")
