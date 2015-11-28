import block
from treestruct import *
import node

node0 = node.node()
node2 = node.node()
node3 = node.node()
node4 = node.node()
genesis = Treenode()
B = block.block(None)
node0.currentblock = B

#transaction 2 in the block sent by node0 with address 1000
t1 = transaction.transaction(1,2)
t1.sign = "sign2"
t1.hash = 12342
# input trans
t1.inlist = [transaction.inputtrans() for i in range (t1.incount)]
t1.inlist[0].hash = 12341
t1.inlist[0].n = 1
t1.inlist[0].sign = "signofnode0"
t1.inlist[0].pub = node0.publickey	# public key of node 0
# output trans
t1.outlist = [transaction.outputtrans() for i in range (t1.outcount)]
t1.outlist[0].value = 2
t1.outlist[0].addr = node2.publickey
t1.outlist[1].value = 17
t1.outlist[1].addr = node0.publickey

node0.currentblock=node0.currentblock.add_trans_to_block(t1)

#transaction 3 in the block sent by node0 with address 1000
t2 = transaction.transaction(1,2)
t2.sign = "sign3"
t2.hash = 12343
# input trans
t2.inlist = [transaction.inputtrans() for i in range (t1.incount)]
t2.inlist[0].hash = 12342
t2.inlist[0].n = 1
t2.inlist[0].sign = "signofnode0"
t2.inlist[0].pub = node0.publickey	# public key of node 0
# output trans
t2.outlist = [transaction.outputtrans() for i in range (t1.outcount)]
t2.outlist[0].value = 5
t2.outlist[0].addr = node3.publickey
t2.outlist[1].value = 12
t2.outlist[1].addr = node0.publickey



node0.currentblock=node0.currentblock.add_trans_to_block(t2)

#transaction 5 in the block sent by node0 with address 1001
t1 = transaction.transaction(0,2)
t1.sign = "sign5"
t1.hash = 12345
# no input trans
# output trans
t1.outlist = [transaction.outputtrans() for i in range (t1.outcount)]
t1.outlist[0].value = 5
t1.outlist[0].addr = 1002
t1.outlist[1].value = 15
t1.outlist[1].addr = 1001

node0.currentblock=node0.currentblock.add_trans_to_block(t1)

#Printing block contents

for i in range( node0.currentblock.max_trans_num) :
		print(str(node0.currentblock.translist[i].incount) + '\n')
		print(str(node0.currentblock.translist[i].outcount) + '\n')
		print(str(node0.currentblock.translist[i].sign) + '\n')
		print(str(node0.currentblock.translist[i].hash) + '\n')
		for j in range(node0.currentblock.translist[i].incount) :
			print(str(node0.currentblock.translist[i].inlist[j].hash) + '\n')
			print(str(node0.currentblock.translist[i].inlist[j].n) + '\n')
			print(str(node0.currentblock.translist[i].inlist[j].sign) + '\n')
			print(str(node0.currentblock.translist[i].inlist[j].pub) + '\n')
			
		for j in range(node0.currentblock.translist[i].outcount) :
			print(str(node0.currentblock.translist[i].outlist[j].value) + '\n')
			print(str(node0.currentblock.translist[i].outlist[j].addr) + '\n')	

#Rmovetrans

node0.currentblock.remove_trans_from_block(t2)

#Printing

print('After deleting: ')

for i in range( node0.currentblock.max_trans_num) :
		print(str(node0.currentblock.translist[i].incount) + '\n')
		print(str(node0.currentblock.translist[i].outcount) + '\n')
		print(str(node0.currentblock.translist[i].sign) + '\n')
		print(str(node0.currentblock.translist[i].hash) + '\n')
		for j in range(node0.currentblock.translist[i].incount) :
			print(str(node0.currentblock.translist[i].inlist[j].hash) + '\n')
			print(str(node0.currentblock.translist[i].inlist[j].n) + '\n')
			print(str(node0.currentblock.translist[i].inlist[j].sign) + '\n')
			print(str(node0.currentblock.translist[i].inlist[j].pub) + '\n')
			
		for j in range(node0.currentblock.translist[i].outcount) :
			print(str(node0.currentblock.translist[i].outlist[j].value) + '\n')
			print(str(node0.currentblock.translist[i].outlist[j].addr) + '\n')


#Adding a new transaction

#transaction 4 in the block sent by node0 with address 1000
t1 = transaction.transaction(1,2)
t1.sign = "sign3"
t1.hash = 12344
# input trans
t1.inlist = [transaction.inputtrans() for i in range (t1.incount)]
t1.inlist[0].hash = 12343
t1.inlist[0].n = 1
t1.inlist[0].sign = "signofnode0"
t1.inlist[0].pub = node0.publickey	# public key of node 0
# output trans
t1.outlist = [transaction.outputtrans() for i in range (t1.outcount)]
t1.outlist[0].value = 3
t1.outlist[0].addr = node4.publickey
t1.outlist[1].value = 9
t1.outlist[1].addr = node0.publickey

node0.currentblock=node0.currentblock.add_trans_to_block(t1)

#Printing

print('After adding new trans:' )

for i in range( node0.currentblock.max_trans_num) :
		print(str(node0.currentblock.translist[i].incount) + '\n')
		print(str(node0.currentblock.translist[i].outcount) + '\n')
		print(str(node0.currentblock.translist[i].sign) + '\n')
		print(str(node0.currentblock.translist[i].hash) + '\n')
		for j in range(node0.currentblock.translist[i].incount) :
			print(str(node0.currentblock.translist[i].inlist[j].hash) + '\n')
			print(str(node0.currentblock.translist[i].inlist[j].n) + '\n')
			print(str(node0.currentblock.translist[i].inlist[j].sign) + '\n')
			print(str(node0.currentblock.translist[i].inlist[j].pub) + '\n')
			
		for j in range(node0.currentblock.translist[i].outcount) :
			print(str(node0.currentblock.translist[i].outlist[j].value) + '\n')
			print(str(node0.currentblock.translist[i].outlist[j].addr) + '\n')
