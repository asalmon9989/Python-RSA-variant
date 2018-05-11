import random

def gen_rand_prime():
	"""Generates random prime number."""
	not_prime = True
	"""These boundary values may be changed, however even slightly
		larger numbers will increase the processing time exponentially."""
	lower_bound = 12
	upper_bound = 1200

	while not_prime:
		rand_num = random.randint(lower_bound, upper_bound)
		not_prime = False
		"""Testing primality ..."""
		for num in range(2, rand_num - 1):
			if rand_num % num == 0:
				not_prime = True
	return rand_num