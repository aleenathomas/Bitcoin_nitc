import block
import proof_of_work
import createnode

blocktopropose = "blocktopropose.txt"


flag= False
# current block is full, time to start proof of work
def checkpropose():
	global flag
	for i in range(block.block('None').max_trans_num) :
		if createnode.i_am.currentblock.translist[i] == None:
			print False
			#flag= False
			break
		
		# else we need to propose the current block after solving proof of work
		proof_of_work.proofofwork(createnode.i_am.currentblock)	
		#print "Proof of work has been solved!"
		# convert the current block to file
		block.blocktofile(createnode.i_am.currentblock,blocktopropose)
		#flag= True
		print True
checkpropose()
#exit(flag)									
