'''

A block b is broadcasted, a node which receives it has to:
	1. validate pow
	2. find the block b-pred in the list of leaves having hash = b.prevhash
	3. if b-pred.height + 1 > blockhead.height
	   		blockhead = b
	4. Attach (b, b-pred)
	
Attach (child, parent)
	1. child.parent = parent
	2. parent.listofchildren.add(child)
	3. listofleaves.remove(parent)
	4. listofleaves.add(child)
	5. child.height = parent.height + 1
	
global variable listofleaves = list of the leaves in the tree	
class blockinablockchain
	listofchildren		   				
	parent
	height

'''
