import math

#Generate a list of prime numbers and output to a file. Uses Sieve of Eratosthenes algorithm https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def gen_list_primes(upper_bound, file):
	primes = [True] * (upper_bound + 1)
	primes[0] = False
	primes[1] = False
	square = math.floor(math.sqrt(upper_bound))
	for i in range(2, square):
		if (primes[i] is True):
			for j in range(i*2, len(primes), i):
				primes[j] = False

	with open(file, 'w') as file_object:
		for i in range(len(primes)):
			if (primes[i]):
				file_object.write(str(i) + '\n')