import hashlib

def gethash(string):
	h = hashlib.sha1()
	h.update(string)
	return h.hexdigest()
	
def gethashofblock(block):
	string = ""
	string =  string + block.nonce + block.prev_hash + block.max_trans_num
	for j in range block.max_trans_num	##for each transaction in the block, concatenate the content to the string	
		string = string + block.translist[j].incount + block.translist[j].outcount
		for i in range(block.translist[j].incount):
			string = string + block.translist[j].inlist[i].hash + block.translist[j].inlist[i].n + block.translist[j].inlist[i].sign + block.translist[j].inlist[i].pub
		
		for i in range(block.translist[j].outcount):
			string = string + block.translist[j].inlist[i].value + block.translist[j].inlist[i].addr
	return gethash(string)
