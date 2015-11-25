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
	
	
	'''
	To find the balance in our wallet
	
	getbalance()
	1.Traverse the consesus chain
	2.balance = 0
	3.For each block in the chain
		a.For each transaction from bottom to top
			i.If it's a transaction created by self
				i1.balance = balance + value of output transaction destined to self.publickey
				i2.break loop
			ii.Else
				ii1.If it contains transaction destined to self.publickey
					balance = balance + value of its output transaction
					
	4. Return balance
	
	'''		
