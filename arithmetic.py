#!/usr/bin/python3

def main():
	v = 5*5
	print(v)

	print(5/3)#double result expected
	print(5//3)#integer division

	print(5%3)

	print(divmod(5, 3))#gives two results together as a tuple

	num = 5
	num += 1
	print(num)

	num -= 1
	print(num)

	num *= 5
	print(num)

	num //= 5
	print(num)

	num *= 5
	num /= 5
	print(num)

if __name__ == "__main__": main()