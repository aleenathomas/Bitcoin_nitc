import node
import block
import transaction
import treestruct

i_am = node.node()	#creating a node instance for the peer
i_am.blockhead.propblock = block.block(9999)
i_am.publickey = "1"

#teacher's public keys are kept static
teacher1publickey = "1"
teacher2publickey = "2"
teacher3publickey = "3"
teacher4publickey = "4"
teacher5publickey = "5"

student1publickey = "876"
student2publickey = "567"
student3publickey = "563"
student4publickey = "890"
student5publickey = "173"

t1 = transaction.transaction(0,1)
t1.sign = "signadmin"
t1.hash = "100"
t1.outlist = [transaction.outputtrans() for i in range (t1.outcount)]
t1.outlist[0].value = transaction.transaction(0,0).STAR
t1.outlist[0].addr = teacher1publickey
i_am.blockhead.propblock.add_trans_to_block(t1)


t1 = transaction.transaction(0,1)
t1.sign = "signadmin"
t1.hash = "101"
t1.outlist = [transaction.outputtrans() for i in range (t1.outcount)]
t1.outlist[0].value = transaction.transaction(0,0).STAR
t1.outlist[0].addr = teacher2publickey
i_am.blockhead.propblock.add_trans_to_block(t1)

t1 = transaction.transaction(0,1)
t1.sign = "signadmin"
t1.hash = "102"
t1.outlist = [transaction.outputtrans() for i in range (t1.outcount)]
t1.outlist[0].value = transaction.transaction(0,0).STAR
t1.outlist[0].addr = teacher3publickey
i_am.blockhead.propblock.add_trans_to_block(t1)

t1 = transaction.transaction(0,1)
t1.sign = "signadmin"
t1.hash = "103"
t1.outlist = [transaction.outputtrans() for i in range (t1.outcount)]
t1.outlist[0].value = transaction.transaction(0,0).STAR
t1.outlist[0].addr = teacher4publickey
i_am.blockhead.propblock.add_trans_to_block(t1)

t1 = transaction.transaction(0,1)
t1.sign = "signadmin"
t1.hash = "104"
t1.outlist = [transaction.outputtrans() for i in range (t1.outcount)]
t1.outlist[0].value = transaction.transaction(0,0).STAR
t1.outlist[0].addr = teacher5publickey
i_am.blockhead.propblock.add_trans_to_block(t1)

treestruct.addblock(i_am.blockhead.propblock, i_am)
