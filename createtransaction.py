import createnode
import transaction
import block

t = transaction.transaction(1,3)
t.sign = "teacher1sign"
t.hash = 12346
t.inlist[0].hash = 100
t.inlist[0].n = 0
t.inlist[0].sign = "teacher1sign"
t.inlist[0].pub = createnode.teacher1publickey
t.outlist[0].value = 20
t.outlist[0].addr = 1234567
t.outlist[1].value = 70
t.outlist[1].addr = createnode.teacher1publickey
t.outlist[2].value = 30
t.outlist[2].addr = 9876534

# write the transaction to a file
transaction.transtofile(t, "trans1.txt")
transaction.signtrans(createnode.i_am, "trans1.txt")
newt = transaction.filetotrans("signedtrans.txt")

#add transaction to the currentblock of the node
createnode.i_am.currentblock.add_trans_to_block(newt)
