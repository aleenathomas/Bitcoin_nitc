from block import *

B = filetoblock('newblock.txt')
print(B.prev_hash)
print(B.max_trans_num )
print(B.nonce )
for i in range( B.max_trans_num) :
			print(str(B.translist[i].incount) + '\n')
			print(str(B.translist[i].outcount) + '\n')
			print( B.translist[i].sign )
			print( B.translist[i].hash )
			for j in range(B.translist[i].incount) :
				print(B.translist[i].inlist[j].hash)
				print(str(B.translist[i].inlist[j].n) + '\n')
				print(B.translist[i].inlist[j].sign)
				print(B.translist[i].inlist[j].pub)
				
			for j in range(B.translist[i].outcount) :
				print(B.translist[i].outlist[j].value)
				print(B.translist[i].outlist[j].addr)
		
#transtofile(T,'newtrans.txt')
