def pow ( block ) :
	nonce = 0
	guess = 99999999999999999999
	throttle = 10000000
	target = 2**64 / throttle

	while guess > target:
		nonce+ = 1
		block.nonce = nonce
		hashval = gethashofblock( block )
		guess, = unpack('>Q',hashval[0:8])
#	print "%s:%s:%s:%s:%s:%s:%s" % (timestamp, message, nonce, guess, payload, target, end-start)
