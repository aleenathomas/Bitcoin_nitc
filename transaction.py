# to import from node.py
from node.py import *

class inputtrans:
	def __init__(self):
		self.hash = None
		self.n = 0
		self.sign = None
		self.pub = 0
		
class outputtrans:
	def __init__(self):
		self.value = 0
		self.addr = 0

class transaction:
	def __init__(self,hashaddr,incount,outcount):
		self.hash = hashaddr
		self.incount = incount
		self.outcount = outcount
		self.inlist = None
		self.outlist = None
		
	def createinlist(self):
		self.inlist = [inputtrans() for i in range (self.incount)]
		
	def createoutlist(self):
		self.outlist = [outputtrans() for i in range (self.outcount)]
		
		#to validate the input list of the transaction, ie checking the validity of the transactions in the input list			
	def validatelist(self, node):	
		for i in range(self.incount):
			findhash = self.inlist[i]
			# checking from the bl
			
			# need to make a distributed database				
			
			
			

				
			
