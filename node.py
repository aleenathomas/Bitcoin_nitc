#\xhh 	Character with hex value hh

from block import *
from proof_of_work import *
from blockchain import *


class node:
	def __init__(self):
		
		self.privatekey = SigningKey.generate()	
		self.publickey = self.privatekey.get_verifying_key()
		self.blockhead = None
		self.maxnumtrans = 1000
		self.database = [[0] * 2 for i in xrange(maxnumtrans)]
		self.top = 0
		self.genesis=NULL
		
'''
#Algorithm:
		
1. proofofwork	( new_block )
2. ver = verify_nonce ( prop_block )
3.	if ver == 1: (i.e, if the nonce is verified by the node)
4. 		traverse to the end of a leaf list till hash of the block = prop_block.prev_hash.( call it hashequalblock ).
5.			prop_block.prev_hash = hashequalblock
6.			Add prop_block in the list of leaves
7.		 	Also, maxheight = check max height in the leaflist.
8.			get the block with max height ( blockmaxheight )
9.		    node.blockhead = blockmaxheight


	'''
	#Algorithm:
		
	1. proofofwork	( new_block )
	2. ver = verify_nonce ( prop_block )
	3.	if ver == 1: (i.e, if the nonce is verified by the node)
	4. 		traverse to the end of a leaf list till hash of the block = prop_block.prev_hash.( call it hashequalblock ).
	5.			prop_block.prev_hash = hashequalblock
	6.			Add prop_block in the list of leaves
	7.		 	Also, maxheight = check max height in the leaflist.
	8.			get the block with max height ( blockmaxheight )
	9.		    node.blockhead = blockmaxheight

	'''

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
	2.inbalance = outbalance = 0
	3.For each block in the chain
		a.For each transaction from bottom to top
			i.If it's a transaction created by self
				i1.outbalance = outbalance + value of output transaction destined to someone else
				
			ii.Else
				ii1.If it contains transaction destined to self.publickey
					inbalance = inbalance + value of its output transaction
				
	4. Return inbalance - outbalance

	'''	
	
	
	def getbalance(self) :
		blockptr = blockhead
		inbalance = 0
		outbalance
		while blockptr != self.genesis :
			for i in range(blockptr.max_trans_num,0,-1) :
				if ( blockptr.translist[i].sign == node.sign ) :
					for j in range(blockptr.translist[i].outcount) :
						 if ( blockptr.translist[i].outlist[j].addr != self.publickey ) :
						 	outbalance = outbalance + blockptr.translist[i].outlist[j].value
						 	
				else : 
					for j in range(blockptr.translist[i].outcount) :
						if ( blockptr.translist[i].outlist[j].addr == self.publickey ) :
							inbalance = inbalance + blockptr.translist[i].outlist[j].value
						
						
		return balance		

'''
Function addblock to add the proposed block to the blockchain maintained by the node



'''
		balance = inbalance - outbalance
		return balance

