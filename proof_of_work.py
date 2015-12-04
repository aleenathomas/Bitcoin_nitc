import gethash
import struct
def proofofwork ( block ) :
	nonce = 0
	guess = 99999999999999999999
	#throttle = 10000000
	#target = 2**64 / throttle
	target = 4000000000000000000
	while guess > target:
		nonce = nonce + 1
		#if nonce % 1000 == 0:
		#print nonce
		block.nonce = nonce
		hashval = gethash.gethashofblock( block )
		guess, = struct.unpack('>Q',hashval[0:8])
	#print "Proof of work has been solved!"	
#	print "%s:%s:%s:%s:%s:%s:%s" % (timestamp, message, nonce, guess, payload, target, end-start)

# verifying nonce value
def verify_nonce ( block ):
	#throttle = 10000000
	#target = 2**64 / throttle
	target = 40000000000000000000
	hashval = gethash.gethashofblock( block )
	guess, = struct.unpack('>Q',hashval[0:8])
	if guess <= target:
		return 1;		#verified
	else :
		return 0;		#incorrect!
