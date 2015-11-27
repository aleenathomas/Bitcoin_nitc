from gethash import *
import transaction

class Treenode:
	def __init__( self ):
		#parent points to the block whose hash=proposed block's prev_hash
		self.parent = None
		self.height = 0
		self.propblock = None
		self.propblockhash = None
		#self.next to be used only for leaf list
		self.next = None

blockhead = Treenode()
genesis = Treenode()	# height will be zero for genesis block
leafhead = genesis	# head of the list of leaves, points to an empty node initially
 
#function to add a block to blockchain
def addblock(propblock, node):	
	newnode = Treenode()
	newnode.propblock = propblock
	newnode.propblockhash = gethashofblock(propblock)
	
	#traverse to the end of a leaf list till hash of the block = prop_block.prev_hash.( call it hashequalblock ).
	tempnode = leafhead
	while tempnode != None and tempnode.propblockhash != propblock.prev_hash:
		tempnode = tempnode.next
	if tempnode != None:
		newnode.height = tempnode.height + 1
	else:
		newnode.height = 1
	newnode.parent = tempnode


	#update leaflist
	removeleaf(newnode.parent)
	addleaf(newnode)
		

	#find the node with the maximum height in the leaflist (after adding the newnode to the blockchain)
	maxheight = 0
	tempnode = leafhead
	maxheightnode = tempnode
	while tempnode != None:
		if( maxheight < tempnode.height ):
			maxheight = tempnode.height
			maxheightnode = tempnode
		tempnode = tempnode.next 
	#updating blockhead, pointing it to the node with the maximum height
	blockhead = maxheightnode
				
	# updating the database
	transaction.maptransaction(propblock, node)
	
def addleaf( leaf ):
	global leafhead
	leaf.next = leafhead
	leafhead = leaf	
	
def removeleaf(leaf):
	global leafhead
	ptr = leafhead
	while ptr != None and ptr.next != leaf:
		ptr = ptr.next		
	if ptr != None and leaf != None:	
		ptr.next = leaf.next
	else:
		leafhead = None
