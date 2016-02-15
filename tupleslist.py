#!/usr/bin/python3

def main():
	# tuples are immutable
	# arrays are mutable
	t = 1, 2, 3, 4, 5 #tuple
	print(t)
	print(t[0])
	print(t[-1])#last element
	print(t[4])

	print(len(t))
	print(min(t))
	print(max(t))

	t = (1, 2, 3, 4, 5)
	print(t)

	# a tuple with one element
	t = (1,)
	print(t)

	#list
	x = [1,2,3,4,5,6,7,8,9]
	print(x)

	print(x[0])
	print(x[-1])
	print(len(x))
	print(min(x))
	print(max(x))

	t = tuple(range(25))
	print(t)
	print(type(t))

	#change elements of the tuple
	# t[10] = 42
	# print(t[10])

	x = list(range(25))
	print(x)
	x[10] = 42
	print(x)

if __name__ == "__main__":main() 