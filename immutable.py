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

	#logical values of true and false
	a, b = 0, 1

	print(a<b)
	print(type(a))
	a = True
	b = True
	print(type(a))
	print(type(b))
	print(id(a))
	print(id(b))




if __name__ == "__main__": main()