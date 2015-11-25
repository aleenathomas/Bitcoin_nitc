#\xhh 	Character with hex value hh

from block.py import *

class node:
	def __init__(self):
		self.publickey = None
		self.privatekey = None	
		self.blockhead = None
		self.maxnumtrans = 1000
		self.database = [[0] * 2 for i in xrange(maxnumtrans)]
		self.top = 0
	
	# function to add the mapping of all transactions in the newly proposed block to the database
	def maptransaction(self, block):
		for i in range(	max_trans_num):
			database [ top, 0 ] = block.translist[i].hash
			database[ top, 1] = block.prevhash		# the block hash of the corresponding trasaction hash
			top = top + 1							# to denote the that one more entry has been added to the database				
			
			
	'''
	On receiving a block proposed by another node:
	1. Verify the POW 
	2. If the block is valid
		a. block.prev_hash=blockhead
		   bloackhead=block
	   else
	   		do nothing 
	   		 
	'''	

	'''
	Function to create a block from a received file
	Create a new object B of type block
	.incount = readline()
	B.publickey = readline()
	B.privatekey = readline()	
	B.blockhead = readline()
	B.maxnumtrans = 1000
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
	'''
		
		
		
