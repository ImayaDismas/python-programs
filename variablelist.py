#!/usr/bin/python3


def main():
	x = (1, 2, 3) #a tuple: cant insert, append and cant change it
	print(type(x), x)
	for i in x:
		print(i)

	x = [1, 2, 3] #list type is mutable
	x.append(5)
	x.insert(2, 7)
	print(type(x), x)

	s = 'string'#an immutable sequence
	print(type(s), s[2:4])
	for c in s:
		print(c)

if __name__ == "__main__": main()
