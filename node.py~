#\xhh 	Character with hex value hh

from block.py import *
from pow.py import *

class node:
	def __init__(self):
		
		self.privatekey = SigningKey.generate()	
		self.publickey = self.privatekey.get_verifying_key()
		self.blockhead = None
		self.maxnumtrans = 1000
		self.database = [[0] * 2 for i in xrange(maxnumtrans)]
		self.top = 0
		self.genesis=NULL
		

#Algorithm:
		
#1. proofofwork	( new_block )
#2. ver = verify_nonce ( prop_block )
#3. maxheight = traverse to the end of a leaf list, check max height.
#4.	get the block with max height 
#5. if ver == 1: (i.e, if the nonce is verified by the node)
#6. 	if node.blockhead.height == maxheight:
#7.			prop_block should point to node.blockhead
#8. 		node.blockhead=prop_block
#9.		else
#10.			 node.blockhead = blockmaxheight
#11.			 prop_block should point to node.blockhead
#12. 			node.blockhead=prop_block
	
<<<<<<< HEAD
				
=======
			
>>>>>>> 2a03eb85237e390fb81038c4557c7f1e0868d111
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
