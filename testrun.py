from block import *

B = filetoblock('newblock.txt')
print(B.prev_hash)
print(str(B.max_trans_num) + '\n')
print(str(B.nonce) + '\n')
for i in range( B.max_trans_num) :
			print(str(B.translist[i].incount) + '\n')
			print(str(B.translist[i].outcount) + '\n')
			print( T.sign )
			print( T.hash )
			for j in range(B.translist[i].incount) :
				print(B.translist[i].inlist[j].hash)
				print(str(B.translist[i].inlist[j].n) + '\n')
				print(B.translist[i].inlist[j].sign)
				print(B.translist[i].inlist[j].pub)
				
			for j in range(B.translist[i].outcount) :
				print(B.translist[i].outlist[j].value)
				print(B.translist[i].outlist[j].addr)
		
#transtofile(T,'newtrans.txt')
