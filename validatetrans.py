import transaction
import createnode

t = transaction.filetotrans("signedtrans.txt")
result = t.validatetrans(createnode.i_am)
if result == True:
	#add transaction to the current block maintained by the node
	print "before"	
	createnode.i_am.currentblock.add_trans_to_block(t)
	print createnode.i_am.currentblock.prev_hash	
#	block.blocktofile(createnode.i_am.currentblock, "the contents")	
