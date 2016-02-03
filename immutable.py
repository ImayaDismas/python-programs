#!/usr/bin/python3
# integers strings and tuples are immutable
#lists, dictionaries, and other objects are immutable depending upon implemetation

def main():
	x = 42
	print(x)

	print(id(x))

	print(type(x))

	x = 43
	print(x)
	print(id(x))

	x = 42
	print(x) 
	print(id(x))


if __name__ == "__main__": main()