#!/usr/bin/python3

def main():
	str = 'This is a String'
	print(str)
	print(str.capitalize())
	print(str.upper())
	print('this is a string {}'.format(42))
	print('this is a string %d' %432)
	print('This is a String'.swapcase())
	strg = '  This is a String  '
	print(strg.strip())
	strg1 = 'This is a String\n'
	print(strg1)
	print(strg1.rstrip('\n'))

	string2 = 'thisisastring'.isalnum()
	print(string2)

	string3 = 'thisisastring'.isalpha()
	print(string3)

	string4 = 'thisisastring'.isdigit()
	print(string4)

	# string5 = 'thisisastring'.isprintable()
	# print(string5)
if __name__ == "__main__":main()