max_trans_num = 5

class block:
	def __init__(self,prev_hash):
		self.prev_hash=prev_hash
		self.translist = [transaction(None,0,0) for i in range (max_trans_num)] 	
		self.n = 0
		
	'''
	Add transaction to a block:
		1.Verify whether the transaction is valid
		2.If there is an invalid entry in between the list of transactions in the block
			a.copy the transaction in the order to a new block
			b.add the new transaction to the new block
		  Else
		  	a.add the new transaction to the current block
			
	'''
		
	def add_trans_to_block(self,newtrans): 							#how do we pass an object
		#verify transaction
		for i in range (max_trans_num-1):
			if (self.translist[i].hash==None) and (self.translist[i+1].hash!=None): #if there is an invalid entry in between
				newblock = block (self.prev_hash)				#create a newblock with same contents
				i=0
				j=0
				while i < max_trans_num :
					if self.translist[i].hash != None :
						newblock.translist[j].hash = self.translist[i].hash
						newblock.translist[j].incount = self.translist[i].incount
						newblock.translist[j].outcount = self.translist[i].outcount
						newblock.n = newblock.n + 1
						j = j + 1
					i = i + 1
				newblock.translist[j] = newtrans				#add the new transaction to this new block
				newblock.n = newblock.n + 1	
			else:
				for i in range (max_trans_num-1):
					if self.translist[i].hash==None :
						self.transalist[i]=newtrans
						self.n=self.n + 1
						
		
		#if self.n == max_trans_num :
			#create a new block and send its hash to the daemon
			
	def remove_trans_from_block(self,trans):
		for i in range (max_trans_num):
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
		self.prev_hash=blockhead
		block_head=self
		
		
		
		
		
		 
