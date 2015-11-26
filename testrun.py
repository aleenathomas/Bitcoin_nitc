from transaction import *

trans = filetotrans('transaction.txt')
print( T.incount + '\n')
for i in range( T.incount ):
	print(T.inlist[i].hash + '\n')
	print(T.inlist[i].n + '\n')
	print(T.inlist[i].sign + '\n')
	print(T.inlist[i].pub + '\n')
	
print( T.outcount + '\n' )

for i in range( T.outcount ) :
	print( T.outlist[i].value + '\n' )
	print( T.outlist[i].addr + '\n' ) 
