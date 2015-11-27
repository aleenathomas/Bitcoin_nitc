import hashlib
#from block import block				#only for verification

def gethash(string):				#verified 
	h = hashlib.sha1()
	h.update(string)
	return h.hexdigest()
	
def gethashofblock(block):			#veriried
	string = ""
	string =  string + str(block.nonce) + str(block.prev_hash) + str(block.max_trans_num)
	#for each transaction in the block, concatenate the content to the string
	for j in range (block.max_trans_num) :		
		string = string + str(block.translist[j].incount) + str(block.translist[j].outcount)
		for i in range(block.translist[j].incount):
			string = string + str(block.translist[j].inlist[i].hash) + str(block.translist[j].inlist[i].n) + str(block.translist[j].inlist[i].sign) + str(block.translist[j].inlist[i].pub)
		
		for i in range(block.translist[j].outcount):
			string = string + str(block.translist[j].outlist[i].value) + str(block.translist[j].outlist[i].addr)
	return gethash(string)
	
	
#Verification of working

#hashval=gethash("hel")
#print(hashval)

#hashval = gethash("hel")
#newblock = block (hashval)
#print(gethashofblock(newblock))
