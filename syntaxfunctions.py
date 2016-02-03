#!/usr/bin/python3

def main():
	print("this is the syntax.py file")
	# func(a)#print all the 
	func(1)
	func(3)#start at element 3
	func(5)# at element 5

def func(a):
	for i in range(a, 10):
		print(i)

if __name__ == "__main__": main()