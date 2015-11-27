import transaction 
from treestruct import *
import block
import node

'''
to test whether validate trans is working correctly

steps :
1. create a blockchain containing atleast 3 blocks, which has 5 transactions each
2. call validate trans with a transaction as argument
'''

genesis = Treenode()

# adding the block to the blockchain kept by node1, assuming this test is run from the node1's machine
node0 = node.node()
node1 = node.node()
node2 = node.node()
node3 = node.node()
node4 = node.node()

block1 = block.block(9999)	#genesis hash

#transaction 1 in the block sent by node0 with address 1000
t1 = transaction.transaction(0,2)
t1.sign = "sign1"
t1.hash = 12341
# no input trans but has two outputs
t1.outlist = [transaction.outputtrans() for i in range (t1.outcount)]
t1.outlist[0].value = 1
t1.outlist[0].addr = node1.publickey
t1.outlist[1].value = 19
t1.outlist[1].addr = node0.publickey
# adding trans1 to the block
block1.translist[0] = t1

#transaction 2 in the block sent by node0 with address 1000
t1 = transaction.transaction(1,2)
t1.sign = "sign2"
t1.hash = 12342
# input trans
t1.inlist = [transaction.inputtrans() for i in range (t1.incount)]
t1.inlist[0].hash = 12345
t1.inlist[0].n = 1
t1.inlist[0].sign = "signofnode0"
t1.inlist[0].pub = node0.publickey	# public key of node 0
# output trans
t1.outlist = [transaction.outputtrans() for i in range (t1.outcount)]
t1.outlist[0].value = 2
t1.outlist[0].addr = node2.publickey
t1.outlist[1].value = 17
t1.outlist[1].addr = node0.publickey
# adding trans1 to the block
block1.translist[1] = t1

#transaction 3 in the block sent by node0 with address 1000
t1 = transaction.transaction(1,2)
t1.sign = "sign3"
t1.hash = 12343
# input trans
t1.inlist = [transaction.inputtrans() for i in range (t1.incount)]
t1.inlist[0].hash = 12346
t1.inlist[0].n = 1
t1.inlist[0].sign = "signofnode0"
t1.inlist[0].pub = node0.publickey	# public key of node 0
# output trans
t1.outlist = [transaction.outputtrans() for i in range (t1.outcount)]
t1.outlist[0].value = 5
t1.outlist[0].addr = node3.publickey
t1.outlist[1].value = 12
t1.outlist[1].addr = node0.publickey
# adding trans1 to the block
block1.translist[2] = t1

#transaction 4 in the block sent by node0 with address 1000
t1 = transaction.transaction(1,2)
t1.sign = "sign3"
t1.hash = 12344
# input trans
t1.inlist = [transaction.inputtrans() for i in range (t1.incount)]
t1.inlist[0].hash = 12346
t1.inlist[0].n = 1
t1.inlist[0].sign = "signofnode0"
t1.inlist[0].pub = node0.publickey	# public key of node 0
# output trans
t1.outlist = [transaction.outputtrans() for i in range (t1.outcount)]
t1.outlist[0].value = 3
t1.outlist[0].addr = node4.publickey
t1.outlist[1].value = 9
t1.outlist[1].addr = node0.publickey
# adding trans1 to the block
block1.translist[3] = t1

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
# adding trans1 to the block
block1.translist[4] = t1


block.blocktofile(block1, "testblocktofile.txt")
B = block.filetoblock("testblocktofile.txt")
'''Printing:
'''
print('printing block2')
print(str(B.prev_hash) + '\n')
print(str(B.max_trans_num) + '\n')
print(str(B.nonce) + '\n')

for i in range( B.max_trans_num) :
	print(str(B.translist[i].incount) + '\n')
	print(str(B.translist[i].outcount) + '\n')
	print( str(B.translist[i].sign ) + '\n')
	print( str(B.translist[i].hash ) + '\n')
	for j in range(B.translist[i].incount) :
		print(str(B.translist[i].inlist[j].hash) + '\n')
		print(str(B.translist[i].inlist[j].n) + '\n')
		print(str(B.translist[i].inlist[j].sign) + '\n')
		print(str(B.translist[i].inlist[j].pub) + '\n')
		
	for j in range(B.translist[i].outcount) :
		print ("value = %d",B.translist[i].outlist[j].value)
		print(str(B.translist[i].outlist[j].value) + '\n')
		print(str(B.translist[i].outlist[j].addr) + '\n')	




#block.blocktofile(block2, "testblocktofilecompare.txt")
