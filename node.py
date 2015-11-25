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
	
					
			
			
	'''
	On receiving a block proposed by another node:
	1. Verify the POW 
	2. If the block is valid
		a. block.prev_hash=blockhead
		   bloackhead=block
	   else
	   		do nothing 
	   		 
	'''		
