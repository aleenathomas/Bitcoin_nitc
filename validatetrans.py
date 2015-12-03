import transaction
import createnode


'''
t = transaction.transaction(1,2)
t.sign = "teacher1sign"
t.hash = 12346
t.inlist[0].hash = 100
t.inlist[0].n = 0
t.inlist[0].sign = "teacher1sign"
t.inlist[0].pub = createnode.teacher1publickey
t.outlist[0].value = 5
t.outlist[0].addr = createnode.student1publickey
t.outlist[1].value = 95
t.outlist[1].addr = createnode.teacher1publickey
'''

#validate trans
t = transaction.filetotrans("signedtrans4.txt")
print('In validaate trans.py printing the contents of filetotrans(signedtrans4)')
print(t.outlist[0].value)
print(t.outlist[1].value)
print(t.outlist[2].value)
result = t.validatetrans(createnode.i_am)
print "result in validate trans"
print result
if result == True:
	#add transaction to the current block maintained by the node
	print "before"	
	createnode.i_am.currentblock.add_trans_to_block(t)
	print createnode.i_am.currentblock.prev_hash	
#	block.blocktofile(createnode.i_am.currentblock, "the contents")	
