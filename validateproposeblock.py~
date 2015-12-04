import transaction
import createnode
import proof_of_work
import block
import treestruct

#	teacher1 -> student1 == 10
t = transaction.transaction(1,2)
t.sign = "teacher1sign"
t.hash = 12346
t.inlist[0].hash = "100"
t.inlist[0].n = 0
t.inlist[0].sign = "signghf"
t.inlist[0].pub = createnode.teacher1publickey
t.outlist[0].value = 10
t.outlist[0].addr = createnode.student1publickey
t.outlist[1].value = 90
t.outlist[1].addr = createnode.teacher1publickey

createnode.i_am.currentblock.add_trans_to_block(t)

#	teacher2 -> student2 == 10
t = transaction.transaction(1,2)
t.sign = "teacher2sign"
t.hash = 12347
t.inlist[0].hash = "101"
t.inlist[0].n = 0
t.inlist[0].sign = "signghf"
t.inlist[0].pub = createnode.teacher2publickey
t.outlist[0].value = 10
t.outlist[0].addr = createnode.student2publickey
t.outlist[1].value = 90
t.outlist[1].addr = createnode.teacher2publickey

createnode.i_am.currentblock.add_trans_to_block(t)

#	teacher3 -> student3 == 10
t = transaction.transaction(1,2)
t.sign = "teacher3sign"
t.hash = 12348
t.inlist[0].hash = "102"
t.inlist[0].n = 0
t.inlist[0].sign = "signghf"
t.inlist[0].pub = createnode.teacher3publickey
t.outlist[0].value = 10
t.outlist[0].addr = createnode.student3publickey
t.outlist[1].value = 90
t.outlist[1].addr = createnode.teacher3publickey

createnode.i_am.currentblock.add_trans_to_block(t)

#	teacher4 -> student4 == 10
t = transaction.transaction(1,2)
t.sign = "teacher4sign"
t.hash = 12349
t.inlist[0].hash = "103"
t.inlist[0].n = 0
t.inlist[0].sign = "signghf"
t.inlist[0].pub = createnode.teacher4publickey
t.outlist[0].value = 10
t.outlist[0].addr = createnode.student4publickey
t.outlist[1].value = 90
t.outlist[1].addr = createnode.teacher4publickey

createnode.i_am.currentblock.add_trans_to_block(t)

#	teacher5 -> student5 == 10
t = transaction.transaction(1,2)
t.sign = "teacher5sign"
t.hash = 12350
t.inlist[0].hash = "104"
t.inlist[0].n = 0
t.inlist[0].sign = "signghf"
t.inlist[0].pub = createnode.teacher5publickey
t.outlist[0].value = 10
t.outlist[0].addr = createnode.student5publickey
t.outlist[1].value = 90
t.outlist[1].addr = createnode.teacher5publickey

createnode.i_am.currentblock.add_trans_to_block(t)

#####################
for i in range(block.MAXTRANS) :
	if createnode.i_am.currentblock.translist[i].hash == None:
		print "not yet...."
		break
# else we need to propose the current block after solving proof of work
proof_of_work.proofofwork(createnode.i_am.currentblock)	
print "Proof of work has been solved!"
# convert the current block to file
block.blocktofile(createnode.i_am.currentblock,"blocktopropose.txt")
print "Current block is ready to be proposed!"
#####################

# to attach the block to the blockchain
treestruct.addblock(createnode.i_am.currentblock, createnode.i_am)

'''
t = transaction.transaction(1,2)
t.sign = "teacher1sign"
t.hash = 12360
t.inlist[0].hash = "12350"
t.inlist[0].n = 0
t.inlist[0].sign = "signghf"
t.inlist[0].pub = createnode.student5publickey
t.outlist[0].value = 4
t.outlist[0].addr = createnode.student5publickey
t.outlist[1].value = 6
t.outlist[1].addr = createnode.student3publickey

result = t.validatetrans(createnode.i_am)
#####################
'''
