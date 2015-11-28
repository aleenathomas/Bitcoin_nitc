#\xhh 	Character with hex value hh

import block
from proof_of_work import *
from blockchain import *
from treestruct import *
from ecdsa import SigningKey


class node:
	def __init__(self):		
		self.privatekey = SigningKey.generate()	
		self.publickey = self.privatekey.get_verifying_key()
		self.blockhead = None
		self.maxnumtrans = 1000
		self.database = [[0] * 2 for i in range(self.maxnumtrans)]
		self.top = 0
		self.currentblock = block.block(None)
		self.blockhead = Treenode()
		self.genesis = Treenode()	# height will be zero for genesis block
		self.leafhead = self.genesis	# head of the list of leaves, points to an empty node initially
	
	
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
		blockptr = self.blockhead
		inbalance = 0
		outbalance = 0
		while blockptr != self.genesis :
			for i in range(blockptr.propblock.max_trans_num) :
				if ( blockptr.propblock.translist[i].sign == node.sign ) :
					for j in range(blockptr.propblock.translist[i].outcount) :
						 if ( blockptr.propblock.translist[i].outlist[j].addr != self.publickey ) :
						 	outbalance = outbalance + blockptr.propblock.translist[i].outlist[j].value
						 	
				else : 
					for j in range(blockptr.propblock.translist[i].outcount) :
						if ( blockptr.propblock.translist[i].outlist[j].addr == self.publickey ) :
							inbalance = inbalance + blockptr.propblock.translist[i].outlist[j].value
						
						
		balance = inbalance - outbalance
		return balance
		
#proofofwork( new_block )
#ver = verify_nonce ( prop_block )
#ver=1 => verified nonce
#if ver == 1: 
#	addblock( propblock )

