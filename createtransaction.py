import createnode
import transaction
import block

t = transaction.transaction(1,2)
t.sign = "sign6"
t.hash = 12346
t.inlist[0].hash = 12343
t.inlist[0].n = 0
t.inlist[0].sign = "mysign"
t.inlist[0].pub = createnode.i_am.publickey
t.outlist[0].value = 2
t.outlist[0].addr = 1234567
t.outlist[1].value = 3
t.outlist[1].addr = 56789 

# write the transaction to a file
transaction.transtofile(t, "trans1.txt")
transaction.signtrans(createnode.i_am, "trans1.txt")
newt = transaction.filetotrans("signedtrans.txt")

#add transaction to the currentblock of the node
createnode.i_am.currentblock.add_trans_to_block(newt)
