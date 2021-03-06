#!/usr/bin/python3

def isprime(n):
	if n == 1:#one is never prime
		print("1 is special")
		return False
	for x in range(2, n):
		if n % x == 0:
			print("{} equals {} x {}".format(n, x, n//x))
			return False #found a divisor, not prime
		else:
			return True

def primes(n = 1):
	while(True):
		if isprime(n):yield n
		n += 1

for n in primes(): 
	if n > 100: break
	print(n)