import hashlib

def gethash(string):
	h=hashlib.sha1()
	h.update(string)
	return h.hexdigest()
	
def gethashofblock(block):
	string=""
	string =  string + block.nonce + block.prev_hash + block.max_trans_num
	for j in range block.max_trans_num
	
		string=string+translist[j].incount + translist[j].outcount
		for i in range(translist[j].incount):
			string=string + translist[j].inlist[i].hash + translist[j].inlist[i].n + translist[j].inlist[i].sign +	translist[j].inlist[i].pub
		
		for i in range(trans.outcount):
			string=string + translist[j].inlist[i].value + translist[j].inlist[i].addr
		
	return gethash(string)
