import transaction
import createnode
import proof_of_work
import block


t = transaction.transaction(1,3)
t.sign = "teacher1sign"
t.hash = "12346"
t.inlist[0].hash = "100"
t.inlist[0].n = 0
t.inlist[0].sign = "teacher1sign"
t.inlist[0].pub = createnode.teacher1publickey
t.outlist[0].value = 70
t.outlist[0].addr = createnode.teacher1publickey
t.outlist[1].value = 10
t.outlist[1].addr = createnode.student2publickey
t.outlist[2].value = 20
t.outlist[2].addr = createnode.student1publickey

result = t.validatetrans(createnode.i_am)

if result == True:
	#add transaction to the current block maintained by the node
	createnode.i_am.currentblock.add_trans_to_block(t)
'''
#validate trans
t = transaction.filetotrans("signedtrans5.txt")

result = t.validatetrans(createnode.i_am)

if result == True:
	#add transaction to the current block maintained by the node
	createnode.i_am.currentblock.add_trans_to_block(t)
	
'''
'''
#Invalid input hash given in the input list of the transaction
-----------------------------------------------------------------------
t = transaction.transaction(1,2)
t.sign = "teacher1sign"
t.hash = 12346
t.inlist[0].hash = "110"
t.inlist[0].n = 0
t.inlist[0].sign = "signghf"
t.inlist[0].pub = createnode.teacher1publickey
t.outlist[0].value = 100
t.outlist[0].addr = createnode.student1publickey
t.outlist[1].value = 90
t.outlist[1].addr = createnode.teacher1publickey

Balance is less than the requested sum
-----------------------------------------------------------------------
t = transaction.transaction(1,2)
t.sign = "teacher1sign"
t.hash = 12346
t.inlist[0].hash = "100"
t.inlist[0].n = 0
t.inlist[0].sign = "signghf"
t.inlist[0].pub = createnode.teacher1publickey
t.outlist[0].value = 100
t.outlist[0].addr = createnode.student1publickey
t.outlist[1].value = 90
t.outlist[1].addr = createnode.teacher1publickey

invalid input transaction, ie an input transaction that has not yet made to the blockchain yet
----------------------------------------------------------------------------------------------

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

result = t.validatetrans(createnode.i_am)

if result == True:
	#add transaction to the current block maintained by the node
	createnode.i_am.currentblock.add_trans_to_block(t)

t = transaction.transaction(1,2)
t.sign = "teacher1sign"
t.hash = 12347
t.inlist[0].hash = "12346"
t.inlist[0].n = 0
t.inlist[0].sign = "signghf"
t.inlist[0].pub = createnode.student1publickey
t.outlist[0].value = 4
t.outlist[0].addr = createnode.student2publickey
t.outlist[1].value = 6
t.outlist[1].addr = createnode.student1publickey

Invalid transaction, possible attempt to create coin
----------------------------------------------------------------------
t = transaction.transaction(0,2)
t.sign = "teacher1sign"
t.hash = 12346
t.outlist[0].value = 10
t.outlist[0].addr = createnode.student1publickey
t.outlist[1].value = 90
t.outlist[1].addr = createnode.teacher1publickey

Transaction already received
----------------------------------------------------------------------
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

result = t.validatetrans(createnode.i_am)

if result == True:
	#add transaction to the current block maintained by the node
	createnode.i_am.currentblock.add_trans_to_block(t)
	
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

A valid transaction
---------------------------------------------------------------------

t = transaction.transaction(1,3)
t.sign = "teacher1sign"
t.hash = "12346"
t.inlist[0].hash = "100"
t.inlist[0].n = 0
t.inlist[0].sign = "teacher1sign"
t.inlist[0].pub = createnode.teacher1publickey
t.outlist[0].value = 70
t.outlist[0].addr = createnode.teacher1publickey
t.outlist[1].value = 10
t.outlist[1].addr = createnode.student2publickey
t.outlist[2].value = 20
t.outlist[2].addr = createnode.student1publickey
'''	
