import transaction
import createnode

t = transaction.filetotrans("signedtrans.txt")
result = t.validatetrans(createnode.i_am)
if result == True:
	#add transaction to the current block maintained by the node
	createnode.i_am.currentblock.add_trans_to_block(t)	
