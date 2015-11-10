import hashlib

def gethash(string):
	h=hashlib.sha1()
	h.update(string)
	return h.hexdigest()
	
	
def gethashoftransaction(trans):
	string=""
	string=string+incount+outcount
	for i in range(trans.incount):
		string=string + trans.inlist[i].hash + trans.inlist[i].n + trans.inlist[i].sign +	trans.inlist[i].pub
		
	for i in range(trans.outcount):
		string=string + trans.inlist[i].value + trans.inlist[i].addr
		
	return gethash(string)
