import block
from treestruct import *

node0 = node.node()
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

node0.currentblock.add_trans_to_block(t1)
