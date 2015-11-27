import transaction

B = transaction.filetotrans('newtrans.txt')
print(B.incount)
print(B.outcount )
print(B.sign )
print(B.hash )
for i in range( B.incount ) :
			print(B.inlist[i].hash)
			print(B.inlist[i].n)
			print( B.inlist[i].sign )
			print( B.inlist[i].pub )
			
for i in range ( B.outcount ) :
			print(B.outlist[i].value)
			print( B.outlist[i].addr )
		
transaction.transtofile(B,'newtrans1.txt')
