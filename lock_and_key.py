import mkprime

def crypt_keeper():
	"""Generates "lock" and "key" from two randomly generated prime
	numbers. This ensures a unique encryption for each message."""
	prime1 = mkprime.gen_rand_prime()
	prime2 = mkprime.gen_rand_prime()
	"""Unique exponent is an independent variable in creating
		the key."""
	pwr = mkprime.gen_rand_prime()

	"""The encryption is based on modular arithmetic and basic
		knowledge of the mechanics of equivalence relations."""
	lock = prime1*prime2
	sublock = (prime1-1)*(prime2-1)

	"""Euclidean algorithm ..."""
	euc_dict = [{'q': sublock//pwr, 'd': pwr, 'r': sublock%pwr}]
	for i in range(10**10):
		euc_dict.append({'q': euc_dict[i]['d']//euc_dict[i]['r'],
						'd': euc_dict[i]['r'],
						'r': euc_dict[i]['d']%euc_dict[i]['r']})
		if euc_dict[i]['r'] == 1:
			break

	"""Realized recurrence relation ... (took awhile to figure
		that out)"""
	term_list = [euc_dict[0]['q']]
	for i in range(1, len(euc_dict)-1):
		term_list.append(1/term_list[i-1] + euc_dict[i]['q'])

	"""Finally, multiply the terms to make the key."""
	key = 1
	for i in range(len(term_list)):
		key *= term_list[i]
	"""The fractions in the terms throw off the key enough to disrupt
		things. Adding a tenth and truncating to the integer
		mitigates this (though probably inefficient)."""
	key = int(key+0.1)
	if len(term_list)%2 != 0:
		key = sublock - key

	return [lock, pwr, key]