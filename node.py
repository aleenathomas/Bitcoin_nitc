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
		
		
		
