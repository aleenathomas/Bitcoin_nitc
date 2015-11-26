from transaction import *

T = filetotrans('transaction.txt')
print( str(T.incount) )
for i in range( T.incount ):
	print(str(T.inlist[i].hash) )
	print(str(T.inlist[i].n) )
	print(str(T.inlist[i].sign) )
	print(str(T.inlist[i].pub) )
	
print( str(T.outcount)  )

for i in range( T.outcount ) :
	print( str(T.outlist[i].value)  )
	print( str(T.outlist[i].addr)  ) 
