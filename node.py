#\xhh 	Character with hex value hh

from block.py import *

class node:
	def __init__(self):
		self.publickey = None
		self.privatekey = None	
		self.blockhead = None
		self.maxnumtrans = 10000
		self.database = [[0] * 2 for i in xrange(maxnumtrans)]
		
	
	# function to add the mapping of all transactions in the newly proposed block
	def maptransaction(self, block):
		for i in range(	max_trans_num):
			
		
		
		
		
